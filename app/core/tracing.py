# core/tracing.py
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter


def setup_tracing():
    resource = Resource.create({
        "service.name": "cloudstack.app"
    })

    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    exporter = ConsoleSpanExporter()

    provider.add_span_processor(
        BatchSpanProcessor(exporter)
    )