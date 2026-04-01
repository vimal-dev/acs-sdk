# Apache CloudStack Python SDK

A Python SDK for the Apache CloudStack API that provides a simple and type-safe interface to manage resources.

## Features

- 🔐 **Type-Safe** - Built with Pydantic for request/response validation
- 🚀 **Async Support** - Built on httpx for modern async HTTP requests
- 📦 **Easy Configuration** - Simple configuration management
- 🧪 **Well Tested** - Comprehensive test suite with pytest
- 🔄 **Automatic Retry** - Built-in retry logic with exponential backoff
- 🔑 **Request Signing** - Automatic HMAC-SHA1 request signing

## Requirements

- Python >= 3.12

## Installation

```bash
pip install acs-sdk
```

## Getting Started

### Basic Setup

```python
from acs_sdk import ApacheCloudStackClient, ApacheCloudStackConfig

# Create a configuration
config = ApacheCloudStackConfig(
    endpoint="https://your-cloudstack-endpoint/api",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

# Initialize the CloudStack client
client = ApacheCloudStackClient(config)
```

### Making API Calls

```python
# List users
response = client.call('listUsers')

# Get user with parameters
user_response = client.call('getUser', {'userid': '123'})

# Don't forget to close the client
client.close()
```

## Project Structure

```
src/
├── acs_sdk/
│   ├── client/            # HTTP client implementation
│   ├── core/              # Retry logic and request signing
│   ├── schemas/           # Configuration schemas
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
pytest tests/unit/test_client.py

# Run with coverage report
pytest --cov=acs_sdk --cov-report=html
```

### Code Structure

- **Client** - Handles HTTP requests to Apache CloudStack API
- **Core** - Retry logic and request signing utilities
- **Schemas** - Pydantic models for configuration validation

## Dependencies

- **httpx** (>=0.28.1) - Modern HTTP client for async support
- **pydantic** (>=2.12.5) - Data validation and serialization

## License

MIT

## Author

Vimal Saini - vimal.saini25@gmail.com