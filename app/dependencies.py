import os

from dotenv import load_dotenv

from acs_sdk.schemas.config import ApacheCloudStackConfig
from acs_sdk.acs import ApacheCloudStack
from app.core.logger import setup_logger
from app.core.request_context import set_request_context

load_dotenv()  # Load environment variables from .env file


from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter


def setup_tracing():
    resource = Resource.create({
        "service.name": "cloudstack-gateway"
    })

    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    exporter = ConsoleSpanExporter()

    provider.add_span_processor(BatchSpanProcessor(exporter))


def get_tracer(name: str):
    return trace.get_tracer(name)


def get_acs_client() -> ApacheCloudStack:
    config = ApacheCloudStackConfig(
        api_endpoint=os.getenv("CLOUDSTACK_ENDPOINT", "https://api.cloudstack.com/client/api"),
        api_key=os.getenv("CLOUDSTACK_API_KEY", "your-api-key"),
        api_secret=os.getenv("CLOUDSTACK_API_SECRET", "your-api-secret"),
        timeout=int(os.getenv("CLOUDSTACK_TIMEOUT", "30")),
    )
    set_request_context(request_id="static-request-id", user_id="static-user-id", tenant_id="static-tenant-id")
    setup_tracing()
    tracer = get_tracer(__name__)
    logger = setup_logger()
    logger.info("Creating ApacheCloudStack client with endpoint: %s", config.api_endpoint)
    acs_client = ApacheCloudStack(config, tracer=tracer, logger=logger)
    return acs_client
