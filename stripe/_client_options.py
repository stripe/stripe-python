from stripe._requestor_options import RequestorOptions
from typing import Optional


class _ClientOptions(RequestorOptions):
    client_id: Optional[str]

    def __init__(
        self,
        requestor_options: RequestorOptions,
        client_id: Optional[str] = None,
        proxy: Optional[str] = None,
        verify_ssl_certs: Optional[bool] = None,
    ):
        super().__init__(**requestor_options.to_dict())
        self.client_id = client_id
        self.proxy = proxy
        self.verify_ssl_certs = verify_ssl_certs
