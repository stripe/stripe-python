import stripe
from stripe._requestor_options import (
    RequestorOptions,
    _GlobalRequestorOptions,
)


class TestRequestorOptions(object):
    def test_to_dict(self):
        requestor = RequestorOptions(
            api_key="sk_test_123",
            stripe_account="acct_123",
            stripe_version="2019-12-03",
            base_addresses={
                "api": "https://api.example.com",
                "connect": "https://connect.example.com",
                "files": "https://files.example.com",
            },
            max_network_retries=3,
        )
        assert requestor.to_dict() == {
            "api_key": "sk_test_123",
            "stripe_account": "acct_123",
            "stripe_version": "2019-12-03",
            "base_addresses": {
                "api": "https://api.example.com",
                "connect": "https://connect.example.com",
                "files": "https://files.example.com",
            },
            "max_network_retries": 3,
        }

    def test_global_options_get_updated(
        self,
    ):
        global_options = _GlobalRequestorOptions()
        orig_api_key = stripe.api_key
        orig_api_base = stripe.api_base
        orig_connect_base = stripe.connect_api_base
        orig_upload_base = stripe.upload_api_base
        orig_max_network_retries = stripe.max_network_retries
        assert global_options.api_key == orig_api_key
        assert global_options.base_addresses["api"] == orig_api_base
        assert global_options.base_addresses["connect"] == orig_connect_base
        assert global_options.base_addresses["files"] == orig_upload_base
        assert global_options.stripe_account is None
        stripe.api_key = "sk_test_555555555"
        stripe.api_base = "https://api.example.com"
        stripe.connect_api_base = "https://connect.example.com"
        stripe.upload_api_base = "https://upload.example.com"
        stripe.max_network_retries = 3
        assert global_options.api_key == "sk_test_555555555"
        assert (
            global_options.base_addresses["api"] == "https://api.example.com"
        )
        assert (
            global_options.base_addresses["connect"]
            == "https://connect.example.com"
        )
        assert (
            global_options.base_addresses["files"]
            == "https://upload.example.com"
        )
        assert global_options.stripe_account is None
        assert global_options.max_network_retries == 3
        stripe.api_key = orig_api_key
        stripe.api_base = orig_api_base
        stripe.connect_api_base = orig_connect_base
        stripe.upload_api_base = orig_upload_base
        stripe.max_network_retries = orig_max_network_retries
