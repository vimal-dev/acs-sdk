import pprint

from .dependencies import get_acs_client
import click

from acs_sdk.schemas.request.virtual_machine import (
    RebootVirtualMachineRequest,
    StartVirtualMachineRequest,
    StopVirtualMachineRequest,
    DestroyVirtualMachineRequest,
    ExpungeVirtualMachineRequest,
    RecoverVirtualMachineRequest,
    GetVMPasswordRequest,
    GetVMUserdataRequest,
)


COMMAND_MAP = {
    "reboot": ("reboot_vm", RebootVirtualMachineRequest),
    "start": ("start_vm", StartVirtualMachineRequest),
    "stop": ("stop_vm", StopVirtualMachineRequest),
    "destroy": ("destroy_vm", DestroyVirtualMachineRequest),
    "expunge": ("expunge_vm", ExpungeVirtualMachineRequest),
    "recover": ("recover_vm", RecoverVirtualMachineRequest),
    "get-password": ("get_vm_password", GetVMPasswordRequest),
    "get-userdata": ("get_vm_userdata", GetVMUserdataRequest),
}


def _call_vm_action(client, cmd: str, vm_id: str):
    if cmd not in COMMAND_MAP:
        raise ValueError(f"Unknown command: {cmd}")

    method_name, req_cls = COMMAND_MAP[cmd]
    payload = req_cls(id=vm_id)
    method = getattr(client.vm, method_name)
    return method(payload)


@click.command()
@click.argument("cmds", nargs=-1, required=True, metavar="CMD")
@click.option("--vm-id", "vm_ids", multiple=True, required=True, help="One or more VM IDs")
def handle(cmds: tuple[str, ...], vm_ids: tuple[str, ...]):
    """Execute one or more CMDs against the provided --vm-id(s).

    Examples:
      vm_act.py reboot --vm-id <id>
      vm_act.py start stop --vm-id id1 --vm-id id2
    """
    acs_client = get_acs_client()

    # normalize cmds: allow comma-separated in single arg
    expanded_cmds: list[str] = []
    for c in cmds:
        for part in c.split(","):
            part = part.strip()
            if part:
                expanded_cmds.append(part)

    for vm in vm_ids:
        for cmd in expanded_cmds:
            try:
                response = _call_vm_action(acs_client, cmd, vm)
                pprint.pp({"vm": vm, "cmd": cmd, "result": getattr(response, 'data', None)})
            except Exception as e:
                pprint.pp({"vm": vm, "cmd": cmd, "error": str(e)})


if __name__ == "__main__":
    handle()