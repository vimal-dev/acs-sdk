import asyncio
from unittest.mock import AsyncMock, Mock

from acs_sdk.schemas.request.security_group import (
    AuthorizeSecurityGroupEgressRequest,
    AuthorizeSecurityGroupIngressRequest,
    CreateSecurityGroupRequest,
    DeleteSecurityGroupRequest,
    ListSecurityGroupRequest,
    RevokeSecurityGroupEgressRequest,
    RevokeSecurityGroupIngressRequest,
    UpdateSecurityGroupRequest,
)
from acs_sdk.services.security_group import SecurityGroup


# ---------------------------------------------------------------------------
# list
# ---------------------------------------------------------------------------

def test_security_group_list_parses_list_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "listsecuritygroupsresponse": {
            "securitygroup": [{"id": "sg-1", "name": "web"}],
            "count": 1,
        }
    }

    sg = SecurityGroup(client=mock_client)
    payload = ListSecurityGroupRequest()
    response = sg.list(payload)

    assert response.data == [{"id": "sg-1", "name": "web"}]
    assert response.count == 1
    mock_client.call.assert_called_once_with(
        "listSecurityGroups", payload.model_dump(exclude_none=True)
    )


def test_security_group_list_async_parses_list_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "listsecuritygroupsresponse": {
                "securitygroup": [{"id": "sg-2", "name": "db"}],
                "count": 1,
            }
        }
    )

    sg = SecurityGroup(client=mock_client)
    payload = ListSecurityGroupRequest(securityGroupName="db")
    response = asyncio.run(sg.list_async(payload))

    assert response.data == [{"id": "sg-2", "name": "db"}]
    assert response.count == 1
    mock_client.call_async.assert_called_once_with(
        "listSecurityGroups", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# create
# ---------------------------------------------------------------------------

def test_security_group_create_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "createsecuritygroupresponse": {"id": "sg-new", "name": "web"},
    }

    sg = SecurityGroup(client=mock_client)
    payload = CreateSecurityGroupRequest(name="web")
    response = sg.create(payload)

    assert response.data == {"id": "sg-new", "name": "web"}
    mock_client.call.assert_called_once_with(
        "createSecurityGroup", payload.model_dump(exclude_none=True)
    )


def test_security_group_create_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "createsecuritygroupresponse": {"id": "sg-new", "name": "web"},
        }
    )

    sg = SecurityGroup(client=mock_client)
    payload = CreateSecurityGroupRequest(name="web")
    response = asyncio.run(sg.create_async(payload))

    assert response.data == {"id": "sg-new", "name": "web"}
    mock_client.call_async.assert_called_once_with(
        "createSecurityGroup", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# update
# ---------------------------------------------------------------------------

def test_security_group_update_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "updatesecuritygroupresponse": {"id": "sg-1", "name": "web-updated"},
    }

    sg = SecurityGroup(client=mock_client)
    payload = UpdateSecurityGroupRequest(id="sg-1", name="web-updated")
    response = sg.update(payload)

    assert response.data == {"id": "sg-1", "name": "web-updated"}
    mock_client.call.assert_called_once_with(
        "updateSecurityGroup", payload.model_dump(exclude_none=True)
    )


def test_security_group_update_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "updatesecuritygroupresponse": {"id": "sg-1", "name": "web-updated"},
        }
    )

    sg = SecurityGroup(client=mock_client)
    payload = UpdateSecurityGroupRequest(id="sg-1", name="web-updated")
    response = asyncio.run(sg.update_async(payload))

    assert response.data == {"id": "sg-1", "name": "web-updated"}
    mock_client.call_async.assert_called_once_with(
        "updateSecurityGroup", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# delete
# ---------------------------------------------------------------------------

def test_security_group_delete_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "deletesecuritygroupresponse": {"success": "true"},
    }

    sg = SecurityGroup(client=mock_client)
    payload = DeleteSecurityGroupRequest(id="sg-1")
    response = sg.delete(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("deleteSecurityGroup", {"id": "sg-1"})


def test_security_group_delete_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"deletesecuritygroupresponse": {"success": "true"}}
    )

    sg = SecurityGroup(client=mock_client)
    payload = DeleteSecurityGroupRequest(name="web")
    response = asyncio.run(sg.delete_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("deleteSecurityGroup", {"name": "web"})


# ---------------------------------------------------------------------------
# authorize_ingress
# ---------------------------------------------------------------------------

def test_security_group_authorize_ingress_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "authorizesecuritygroupingressresponse": {"jobid": "job-1"},
    }

    sg = SecurityGroup(client=mock_client)
    payload = AuthorizeSecurityGroupIngressRequest(
        securityGroupId="sg-1", protocol="TCP", cidrList="0.0.0.0/0", startPort=22, endPort=22
    )
    response = sg.authorize_ingress(payload)

    assert response.data == {"jobid": "job-1"}
    mock_client.call.assert_called_once_with(
        "authorizeSecurityGroupIngress", payload.model_dump(exclude_none=True)
    )


def test_security_group_authorize_ingress_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "authorizesecuritygroupingressresponse": {"jobid": "job-1"},
        }
    )

    sg = SecurityGroup(client=mock_client)
    payload = AuthorizeSecurityGroupIngressRequest(securityGroupId="sg-1", protocol="TCP")
    response = asyncio.run(sg.authorize_ingress_async(payload))

    assert response.data == {"jobid": "job-1"}
    mock_client.call_async.assert_called_once_with(
        "authorizeSecurityGroupIngress", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# authorize_egress
# ---------------------------------------------------------------------------

def test_security_group_authorize_egress_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "authorizesecuritygroupegressresponse": {"jobid": "job-2"},
    }

    sg = SecurityGroup(client=mock_client)
    payload = AuthorizeSecurityGroupEgressRequest(securityGroupId="sg-1", protocol="TCP")
    response = sg.authorize_egress(payload)

    assert response.data == {"jobid": "job-2"}
    mock_client.call.assert_called_once_with(
        "authorizeSecurityGroupEgress", payload.model_dump(exclude_none=True)
    )


def test_security_group_authorize_egress_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={
            "authorizesecuritygroupegressresponse": {"jobid": "job-2"},
        }
    )

    sg = SecurityGroup(client=mock_client)
    payload = AuthorizeSecurityGroupEgressRequest(securityGroupId="sg-1", protocol="TCP")
    response = asyncio.run(sg.authorize_egress_async(payload))

    assert response.data == {"jobid": "job-2"}
    mock_client.call_async.assert_called_once_with(
        "authorizeSecurityGroupEgress", payload.model_dump(exclude_none=True)
    )


# ---------------------------------------------------------------------------
# revoke_ingress
# ---------------------------------------------------------------------------

def test_security_group_revoke_ingress_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "revokesecuritygroupingressresponse": {"success": "true"},
    }

    sg = SecurityGroup(client=mock_client)
    payload = RevokeSecurityGroupIngressRequest(id="rule-1")
    response = sg.revoke_ingress(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("revokeSecurityGroupIngress", {"id": "rule-1"})


def test_security_group_revoke_ingress_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"revokesecuritygroupingressresponse": {"success": "true"}}
    )

    sg = SecurityGroup(client=mock_client)
    payload = RevokeSecurityGroupIngressRequest(id="rule-1")
    response = asyncio.run(sg.revoke_ingress_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("revokeSecurityGroupIngress", {"id": "rule-1"})


# ---------------------------------------------------------------------------
# revoke_egress
# ---------------------------------------------------------------------------

def test_security_group_revoke_egress_parses_response():
    mock_client = Mock()
    mock_client.call.return_value = {
        "revokesecuritygroupegressresponse": {"success": "true"},
    }

    sg = SecurityGroup(client=mock_client)
    payload = RevokeSecurityGroupEgressRequest(id="rule-1")
    response = sg.revoke_egress(payload)

    assert response.data == {"success": "true"}
    mock_client.call.assert_called_once_with("revokeSecurityGroupEgress", {"id": "rule-1"})


def test_security_group_revoke_egress_async_parses_response():
    mock_client = Mock()
    mock_client.call_async = AsyncMock(
        return_value={"revokesecuritygroupegressresponse": {"success": "true"}}
    )

    sg = SecurityGroup(client=mock_client)
    payload = RevokeSecurityGroupEgressRequest(id="rule-1")
    response = asyncio.run(sg.revoke_egress_async(payload))

    assert response.data == {"success": "true"}
    mock_client.call_async.assert_called_once_with("revokeSecurityGroupEgress", {"id": "rule-1"})
