# services/ssl_cert.py
from typing import Dict, List

from acs_sdk.schemas.request.ssl_cert import (
    DeleteSslCertRequest,
    ListSslCertsRequest,
    UploadSslCertRequest,
)

from .base import BaseService
from ..schemas.response.base import APIResponse


class SslCert(BaseService):
    def upload(self, payload: UploadSslCertRequest) -> APIResponse[Dict]:
        """Upload an SSL certificate."""
        return self._execute(
            "uploadSslCert",
            payload,
            envelope="uploadsslcertresponse",
        )

    async def upload_async(self, payload: UploadSslCertRequest) -> APIResponse[Dict]:
        """Asynchronously upload an SSL certificate."""
        return await self._execute_async(
            "uploadSslCert",
            payload,
            envelope="uploadsslcertresponse",
        )

    def list(self, payload: ListSslCertsRequest) -> APIResponse[List[Dict]]:
        """List SSL certificates."""
        return self._execute(
            "listSslCerts",
            payload,
            envelope="listsslcertsresponse",
            entity="sslcert",
        )

    async def list_async(self, payload: ListSslCertsRequest) -> APIResponse[List[Dict]]:
        """Asynchronously list SSL certificates."""
        return await self._execute_async(
            "listSslCerts",
            payload,
            envelope="listsslcertsresponse",
            entity="sslcert",
        )

    def delete(self, payload: DeleteSslCertRequest) -> APIResponse[Dict]:
        """Delete an SSL certificate."""
        return self._execute(
            "deleteSslCert",
            payload,
            envelope="deletesslcertresponse",
        )

    async def delete_async(self, payload: DeleteSslCertRequest) -> APIResponse[Dict]:
        """Asynchronously delete an SSL certificate."""
        return await self._execute_async(
            "deleteSslCert",
            payload,
            envelope="deletesslcertresponse",
        )
