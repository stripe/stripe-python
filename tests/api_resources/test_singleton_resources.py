import pytest
from typing_extensions import Type

import stripe
from stripe._api_resource import APIResource


SINGLETON_RESOURCES = [
    (stripe.Balance, "/v1/balance"),
    (stripe.BalanceSettings, "/v1/balance_settings"),
    (
        stripe.billing.CreditBalanceSummary,
        "/v1/billing/credit_balance_summary",
    ),
    (stripe.tax.Settings, "/v1/tax/settings"),
]


@pytest.mark.parametrize(("resource_class", "path"), SINGLETON_RESOURCES)
def test_singleton_resource_retrieve(
    resource_class: Type[APIResource], path: str, http_client_mock
) -> None:
    http_client_mock.stub_request("get", path=path, rbody="{}")

    resource = resource_class.retrieve()

    assert resource.instance_url() == path
    http_client_mock.assert_requested("get", path=path)


@pytest.mark.anyio
@pytest.mark.parametrize(("resource_class", "path"), SINGLETON_RESOURCES)
async def test_singleton_resource_retrieve_async(
    resource_class: Type[APIResource], path: str, http_client_mock
) -> None:
    http_client_mock.stub_request("get", path=path, rbody="{}")

    resource = await resource_class.retrieve_async()

    assert resource.instance_url() == path
    http_client_mock.assert_requested("get", path=path)
