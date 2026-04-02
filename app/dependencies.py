import os

from dotenv import load_dotenv

from acs_sdk.schemas.config import ApacheCloudStackConfig
from acs_sdk.acs import ApacheCloudStack

load_dotenv()  # Load environment variables from .env file


def get_acs_client() -> ApacheCloudStack:

    config = ApacheCloudStackConfig(
        api_endpoint=os.getenv("API_ENDPOINT", "https://api.cloudstack.com/client/api"),
        api_key=os.getenv("API_KEY", "your-api-key"),
        api_secret=os.getenv("API_SECRET", "your-api-secret"),
        timeout=int(os.getenv("TIMEOUT", "30")),
    )
    acs_client = ApacheCloudStack(config)
    return acs_client
