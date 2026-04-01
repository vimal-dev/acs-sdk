# Apache Cloud Stack Python SDK

A Python SDK for the Apache Cloudstack API that provides a simple and type-safe interface to manage resources.

## Features

- 🔐 **Type-Safe** - Built with Pydantic for request/response validation
- 🚀 **Async Support** - Built on httpx for modern async HTTP requests
- 📦 **Easy Configuration** - Simple configuration management
- 🧪 **Well Tested** - Comprehensive test suite with pytest

## Requirements

- Python >= 3.12

## Installation

```bash
pip install acs-sdk
```

## Getting Started

### Basic Setup

```python
from acs_sdk import Namecheap, NamecheapConfig

# Create a configuration
config = NamecheapConfig(
    api_user="your_api_user",
    api_key="your_api_key",
    username="your_username",
    client_ip="your_client_ip"
)

# Initialize the Namecheap client
namecheap = Namecheap(config)
```

### SSL Certificate Operations

```python
from namecheap_sdk.schemas.request.ssl import CreateSSLRequest, ListSSLRequest

# Create an SSL certificate
create_request = CreateSSLRequest(
    domain="example.com",
    years=1
)
response = namecheap.ssl.create(create_request)

# List SSL certificates
list_request = ListSSLRequest()
certificates = namecheap.ssl.list(list_request)

# Get SSL certificate information
from namecheap_sdk.schemas.request.ssl import GetSSLInfoRequest
info_request = GetSSLInfoRequest(certificate_id="12345")
cert_info = namecheap.ssl.get_info(info_request)
```

## Project Structure

```
src/
├── app/                    # CLI application examples
├── namecheap_sdk/
│   ├── client/            # HTTP client implementation
│   ├── schemas/           # Request/response schemas
│   │   ├── request/       # Request models
│   │   └── response/      # Response models
│   ├── services/          # Service implementations
│   └── exceptions/        # Custom exceptions
tests/
├── unit/                  # Unit tests
└── conftest.py           # Pytest configuration
```

## Development

### Setup Development Environment

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies with dev tools
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests with coverage
pytest

# Run specific test file
pytest tests/unit/test_namecheap.py

# Run with coverage report
pytest --cov=namecheap_sdk --cov-report=html
```

### Code Structure

- **Client** - Handles HTTP requests to Namecheap API
- **Services** - High-level API for specific operations (SSL, etc.)
- **Schemas** - Pydantic models for request/response validation

## Dependencies

- **httpx** (>=0.28.1) - Modern HTTP client for async support
- **pydantic** (>=2.12.5) - Data validation and serialization

## License

MIT

## Author

Vimal Saini - vimal.saini25@gmail.com