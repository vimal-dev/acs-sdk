"""Request signing module for Apache CloudStack API authentication.

This module provides cryptographic request signing functionality for the Apache
CloudStack API using HMAC-SHA1 signatures. All API requests require signed
parameters to authenticate with the CloudStack endpoint.
"""

import base64
import hashlib
import hmac
import urllib.parse


class RequestSigner:
    """Signs HTTP requests with HMAC-SHA1 signatures for CloudStack API.

    The RequestSigner class handles the cryptographic signing of API request
    parameters using the provided API credentials. It follows the CloudStack
    API specification for request authentication.

    Attributes:
        api_key (str): The CloudStack API key for authentication.
        api_secret (str): The CloudStack API secret used for HMAC signature generation.
    """

    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret

    def sign(self, params: dict) -> dict:
        """Sign request parameters with HMAC-SHA1 signature.

        This method implements the CloudStack API signing process:
        1. Adds the API key to parameters
        2. Sorts parameters by lowercase key names
        3. Creates URL-encoded query string
        4. Generates HMAC-SHA1 digest using the API secret
        5. Base64 encodes the signature
        6. Adds signature to parameters

        Args:
            params (dict): Request parameters to sign. Dictionary with string
                keys and values that can be converted to strings.

        Returns:
            dict: Modified parameters dictionary with 'apikey' and 'signature' added.

        Example:
            >>> signer = RequestSigner('key123', 'secret456')
            >>> signed = signer.sign({'command': 'listUsers'})
            >>> 'signature' in signed and 'apikey' in signed
            True
        """
        params["apikey"] = self.api_key

        sorted_params = sorted(params.items(), key=lambda x: x[0].lower())

        query_string = "&".join(
            f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in sorted_params
        ).lower()

        digest = hmac.new(self.api_secret.encode(), query_string.encode(), hashlib.sha1).digest()

        signature = base64.b64encode(digest).decode()

        params["signature"] = signature
        return params
