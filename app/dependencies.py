import os

from dotenv import load_dotenv

from acs_sdk.schemas.config import ApacheCloudStackConfig
from acs_sdk.acs import ApacheCloudStack

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
        api_endpoint=os.getenv("API_ENDPOINT", "https://api.cloudstack.com/client/api"),
        api_key=os.getenv("API_KEY", "your-api-key"),
        api_secret=os.getenv("API_SECRET", "your-api-secret"),
        timeout=int(os.getenv("TIMEOUT", "30")),
    )
    acs_client = ApacheCloudStack(config)
    return acs_client
