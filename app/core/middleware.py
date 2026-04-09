# middleware/observability.py
import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from opentelemetry import trace

from core.request_context import set_request_context
from core.logger import logger


tracer = trace.get_tracer(__name__)


class ObservabilityMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        start_time = time.time()

        # 🔑 Correlation ID
        request_id = str(uuid.uuid4())

        # 👤 Extract user context (JWT / headers)
        user_id = request.headers.get("x-user-id", "anonymous")
        tenant_id = request.headers.get("x-tenant-id", "default")

        # store context
        set_request_context(request_id, user_id, tenant_id)

        # 🔥 Start trace span
        with tracer.start_as_current_span(
            f"{request.method} {request.url.path}"
        ) as span:

            span.set_attribute("http.method", request.method)
            span.set_attribute("http.route", request.url.path)
            span.set_attribute("user.id", user_id)
            span.set_attribute("tenant.id", tenant_id)
            span.set_attribute("request.id", request_id)

            # 📥 Log request
            logger.info(f"Incoming request {request.method} {request.url.path}")

            try:
                response = await call_next(request)

                duration = time.time() - start_time

                span.set_attribute("http.status_code", response.status_code)
                span.set_attribute("http.duration_ms", int(duration * 1000))

                # 📤 Log response
                logger.info(
                    f"Response {response.status_code} in {duration:.3f}s"
                )

                # attach request id to response
                response.headers["X-Request-ID"] = request_id

                return response

            except Exception as e:
                span.record_exception(e)
                span.set_status(trace.Status(trace.StatusCode.ERROR))

                logger.error(f"Request failed: {str(e)}")

                raise