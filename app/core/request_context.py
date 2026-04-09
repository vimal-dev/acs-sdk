# core/request_context.py
from contextvars import ContextVar

request_id_ctx = ContextVar("request_id", default=None)
user_ctx = ContextVar("user", default=None)
tenant_ctx = ContextVar("tenant", default=None)


def set_request_context(request_id, user_id, tenant_id):
    request_id_ctx.set(request_id)
    user_ctx.set(user_id)
    tenant_ctx.set(tenant_id)


def get_request_context():
    return {
        "request_id": request_id_ctx.get(),
        "user_id": user_ctx.get(),
        "tenant_id": tenant_ctx.get(),
    }