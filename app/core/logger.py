# core/logger.py
import logging
from app.core.request_context import get_request_context
from opentelemetry.trace import get_current_span


class ContextFormatter(logging.Formatter):
    def format(self, record):
        ctx = get_request_context()

        span = get_current_span()
        trace_id = span.get_span_context().trace_id

        record.request_id = ctx["request_id"]
        record.user_id = ctx["user_id"]
        record.tenant_id = ctx["tenant_id"]
        record.trace_id = format(trace_id, "032x") if trace_id else None

        return super().format(record)


def setup_logger():
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = ContextFormatter(
        "[%(asctime)s] [%(levelname)s] "
        "trace_id=%(trace_id)s "
        "request_id=%(request_id)s "
        "user=%(user_id)s tenant=%(tenant_id)s "
        "%(funcName)s:%(lineno)d - "
        "%(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


logger = setup_logger()