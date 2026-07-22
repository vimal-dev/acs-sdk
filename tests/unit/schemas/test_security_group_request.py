import pytest
from pydantic import ValidationError

from acs_sdk.schemas.request.security_group import (
    AuthorizeSecurityGroupEgressRequest,
    AuthorizeSecurityGroupIngressRequest,
    CreateSecurityGroupRequest,
    DeleteSecurityGroupRequest,
    ListSecurityGroupRequest,
    RevokeSecurityGroupEgressRequest,
    RevokeSecurityGroupIngressRequest,
    UpdateSecurityGroupRequest,
    UserSecurityGroupEntry,
)


# ---------------------------------------------------------------------------
# ListSecurityGroupRequest
# ---------------------------------------------------------------------------


def test_list_security_group_defaults_from_pagination_mixin():
    req = ListSecurityGroupRequest()
    dumped = req.model_dump(exclude_none=True)
    assert dumped["page"] == 1
    assert dumped["pagesize"] == 50


def test_list_security_group_virtualmachineid_alias():
    req = ListSecurityGroupRequest(virtualMachineId="vm-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["virtualmachineid"] == "vm-1"


def test_list_security_group_optional_fields_excluded_when_none():
    req = ListSecurityGroupRequest()
    dumped = req.model_dump(exclude_none=True)
    assert "id" not in dumped
    assert "securitygroupname" not in dumped
    assert "virtualmachineid" not in dumped


# ---------------------------------------------------------------------------
# CreateSecurityGroupRequest
# ---------------------------------------------------------------------------


def test_create_security_group_required_name_serializes():
    req = CreateSecurityGroupRequest(name="web")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"name": "web"}


def test_create_security_group_optional_scoping_fields_serialize():
    req = CreateSecurityGroupRequest(
        name="web", description="Web tier", account="acct1", domainId="dom-1", projectId="proj-1"
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["description"] == "Web tier"
    assert dumped["account"] == "acct1"
    assert dumped["domainid"] == "dom-1"
    assert dumped["projectid"] == "proj-1"


def test_create_security_group_missing_name_raises():
    with pytest.raises(ValidationError):
        CreateSecurityGroupRequest()


# ---------------------------------------------------------------------------
# UpdateSecurityGroupRequest
# ---------------------------------------------------------------------------


def test_update_security_group_required_id_serializes():
    req = UpdateSecurityGroupRequest(id="sg-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "sg-1"}


def test_update_security_group_customid_alias():
    req = UpdateSecurityGroupRequest(id="sg-1", customId="custom-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["customid"] == "custom-1"


def test_update_security_group_missing_id_raises():
    with pytest.raises(ValidationError):
        UpdateSecurityGroupRequest()


# ---------------------------------------------------------------------------
# DeleteSecurityGroupRequest
# ---------------------------------------------------------------------------


def test_delete_security_group_by_id():
    req = DeleteSecurityGroupRequest(id="sg-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "sg-1"}


def test_delete_security_group_by_name():
    req = DeleteSecurityGroupRequest(name="web")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"name": "web"}


def test_delete_security_group_id_and_name_mutually_exclusive():
    with pytest.raises(ValidationError):
        DeleteSecurityGroupRequest(id="sg-1", name="web")


def test_delete_security_group_optional_scoping_fields_serialize():
    req = DeleteSecurityGroupRequest(
        id="sg-1", account="acct1", domainId="dom-1", projectId="proj-1"
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["account"] == "acct1"
    assert dumped["domainid"] == "dom-1"
    assert dumped["projectid"] == "proj-1"


# ---------------------------------------------------------------------------
# AuthorizeSecurityGroupIngressRequest
# ---------------------------------------------------------------------------


def test_authorize_ingress_by_securitygroupid():
    req = AuthorizeSecurityGroupIngressRequest(
        securityGroupId="sg-1", protocol="TCP", cidrList="0.0.0.0/0"
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["securitygroupid"] == "sg-1"
    assert dumped["protocol"] == "TCP"
    assert dumped["cidrlist"] == "0.0.0.0/0"


def test_authorize_ingress_by_securitygroupname():
    req = AuthorizeSecurityGroupIngressRequest(securityGroupName="web", protocol="TCP")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["securitygroupname"] == "web"


def test_authorize_ingress_protocol_is_optional():
    req = AuthorizeSecurityGroupIngressRequest(securityGroupName="web")
    dumped = req.model_dump(exclude_none=True)
    assert "protocol" not in dumped


def test_authorize_ingress_securitygroupid_and_name_mutually_exclusive():
    with pytest.raises(ValidationError):
        AuthorizeSecurityGroupIngressRequest(securityGroupId="sg-1", securityGroupName="web")


def test_authorize_ingress_usersecuritygrouplist_flattens_to_indexed_keys():
    req = AuthorizeSecurityGroupIngressRequest(
        securityGroupName="web",
        protocol="TCP",
        userSecurityGroupList=[
            UserSecurityGroupEntry(account="acct1", group="db-servers"),
            UserSecurityGroupEntry(account="acct2", group="cache-servers"),
        ],
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["usersecuritygrouplist[0].account"] == "acct1"
    assert dumped["usersecuritygrouplist[0].group"] == "db-servers"
    assert dumped["usersecuritygrouplist[1].account"] == "acct2"
    assert dumped["usersecuritygrouplist[1].group"] == "cache-servers"
    assert "usersecuritygrouplist" not in dumped


def test_authorize_ingress_projectid_alias():
    req = AuthorizeSecurityGroupIngressRequest(securityGroupName="web", projectId="proj-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped["projectid"] == "proj-1"


# ---------------------------------------------------------------------------
# AuthorizeSecurityGroupEgressRequest
# ---------------------------------------------------------------------------


def test_authorize_egress_by_securitygroupid():
    req = AuthorizeSecurityGroupEgressRequest(
        securityGroupId="sg-1", protocol="TCP", cidrList="10.0.0.0/8"
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["securitygroupid"] == "sg-1"
    assert dumped["cidrlist"] == "10.0.0.0/8"


def test_authorize_egress_protocol_is_optional():
    req = AuthorizeSecurityGroupEgressRequest(securityGroupName="web")
    dumped = req.model_dump(exclude_none=True)
    assert "protocol" not in dumped


def test_authorize_egress_securitygroupid_and_name_mutually_exclusive():
    with pytest.raises(ValidationError):
        AuthorizeSecurityGroupEgressRequest(securityGroupId="sg-1", securityGroupName="web")


def test_authorize_egress_usersecuritygrouplist_flattens_to_indexed_keys():
    req = AuthorizeSecurityGroupEgressRequest(
        securityGroupName="web",
        userSecurityGroupList=[UserSecurityGroupEntry(account="acct1", group="db-servers")],
    )
    dumped = req.model_dump(exclude_none=True)
    assert dumped["usersecuritygrouplist[0].account"] == "acct1"
    assert dumped["usersecuritygrouplist[0].group"] == "db-servers"
    assert "usersecuritygrouplist" not in dumped


# ---------------------------------------------------------------------------
# RevokeSecurityGroupIngressRequest / RevokeSecurityGroupEgressRequest
# ---------------------------------------------------------------------------


def test_revoke_ingress_required_id_serializes():
    req = RevokeSecurityGroupIngressRequest(id="rule-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "rule-1"}


def test_revoke_ingress_missing_id_raises():
    with pytest.raises(ValidationError):
        RevokeSecurityGroupIngressRequest()


def test_revoke_egress_required_id_serializes():
    req = RevokeSecurityGroupEgressRequest(id="rule-1")
    dumped = req.model_dump(exclude_none=True)
    assert dumped == {"id": "rule-1"}


def test_revoke_egress_missing_id_raises():
    with pytest.raises(ValidationError):
        RevokeSecurityGroupEgressRequest()
