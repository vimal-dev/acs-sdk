import os

from dotenv import load_dotenv

from acs_sdk.schemas.config import ApacheCloudStackConfig  
from acs_sdk.acs import ApacheCloudStack

load_dotenv()  # Load environment variables from .env file


def get_acs_client():

    config = ApacheCloudStackConfig(
        api_user=os.getenv("API_USER", "demo"),
        api_key=os.getenv("API_KEY", "demo"),
        username=os.getenv("API_USERNAME", "demo"),
        client_ip=os.getenv("CLIENT_IP", "127.0.0.1"),
        sandbox=os.getenv("SANDBOX", "false").lower() == "true",  # Set to False for production
    )
    acs_client = ApacheCloudStack(config)
    return acs_client
