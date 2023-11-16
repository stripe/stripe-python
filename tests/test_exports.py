# pyright: strict
import stripe


def test_can_import_stripe_object() -> None:
    from stripe.stripe_object import (
        StripeObject as StripeObjectFromStripeStripeObject,
    )

    assert (
        stripe.stripe_object.StripeObject is StripeObjectFromStripeStripeObject
    )


def test_can_import_webhook_members() -> None:
    from stripe import (
        Webhook,
        WebhookSignature,
    )

    assert Webhook is not None
    assert WebhookSignature is not None


def test_can_import_abstract() -> None:
    from stripe.api_resources.abstract import (
        APIResource as APIResourceFromApiResourcesAbstract,
    )
    from stripe.stripe_object import (
        StripeObject,
    )

    assert (
        APIResourceFromApiResourcesAbstract[StripeObject]
        == stripe.abstract.APIResource[StripeObject]
    )


def test_can_import_app_info() -> None:
    from stripe.app_info import AppInfo as AppInfoFromStripeAppInfo
    from stripe import AppInfo as AppInfoFromStripe

    assert AppInfoFromStripeAppInfo is AppInfoFromStripe
    assert AppInfoFromStripeAppInfo is stripe.AppInfo


def test_can_import_stripe_response() -> None:
    from stripe.stripe_response import (
        StripeResponse as StripeResponseFromStripeResponse,
    )

    assert (
        StripeResponseFromStripeResponse
        is stripe.stripe_response.StripeResponse
    )


def test_can_import_oauth_members() -> None:
    from stripe import (
        OAuth,
    )

    assert OAuth is not None


def test_can_import_errors() -> None:
    from stripe.error import (
        StripeError as StripeErrorFromStripeError,
    )

    assert StripeErrorFromStripeError is not None


def test_can_import_top_level_resource() -> None:
    from stripe import Account as AccountFromStripe
    from stripe.api_resources import Account as AccountFromStripeResources
    from stripe.api_resources.account import (
        Account as AccountFromStripeResourcesAccount,
    )

    assert stripe.Account == AccountFromStripe
    assert AccountFromStripe == AccountFromStripeResources
    assert AccountFromStripeResourcesAccount == AccountFromStripeResources


def test_can_import_namespaced_resource() -> None:
    from stripe import tax as TaxPackage
    from stripe.api_resources.tax import (
        Calculation as CalculationFromResources,
    )
    from stripe.api_resources.tax.calculation import (
        Calculation as CalculationFromResourcesCalculation,
    )

    assert stripe.tax is TaxPackage
    assert stripe.tax.Calculation is TaxPackage.Calculation
    assert stripe.tax.Calculation is CalculationFromResources
    assert CalculationFromResources is CalculationFromResourcesCalculation
