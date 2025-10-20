# pyright: strict
# we specifically test various import patterns
import stripe
import subprocess
import sys


def assert_output(code: str, expected: str) -> None:
    process = subprocess.Popen(
        [sys.executable, "-c", f"import stripe; print({code})"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    stdout, stderr = process.communicate()

    assert not stderr, f"Error: {stderr.decode()}"

    output = stdout.decode().strip()
    # assert the output
    assert output == expected


def test_can_import_request_options() -> None:
    from stripe import RequestOptions  # pyright: ignore[reportUnusedImport]


def test_can_import_http_client() -> None:
    from stripe import (
        HTTPClient,  # pyright: ignore[reportUnusedImport]
        PycurlClient,  # pyright: ignore[reportUnusedImport]
        RequestsClient,  # pyright: ignore[reportUnusedImport]
        UrlFetchClient,  # pyright: ignore[reportUnusedImport]
        new_default_http_client,  # pyright: ignore[reportUnusedImport]
    )


def test_can_import_webhook_members() -> None:
    from stripe import (
        Webhook,  # pyright: ignore[reportUnusedImport]
        WebhookSignature,  # pyright: ignore[reportUnusedImport]
    )


def test_can_import_abstract() -> None:
    from stripe import (
        APIResource,  # pyright: ignore[reportUnusedImport]
        SingletonAPIResource,  # pyright: ignore[reportUnusedImport]
        CreateableAPIResource,  # pyright: ignore[reportUnusedImport]
        UpdateableAPIResource,  # pyright: ignore[reportUnusedImport]
        DeletableAPIResource,  # pyright: ignore[reportUnusedImport]
        ListableAPIResource,  # pyright: ignore[reportUnusedImport]
        SearchableAPIResource,  # pyright: ignore[reportUnusedImport]
        VerifyMixin,  # pyright: ignore[reportUnusedImport]
        APIResourceTestHelpers,  # pyright: ignore[reportUnusedImport]
        custom_method,  # pyright: ignore[reportDeprecated, reportUnusedImport]
        nested_resource_class_methods,  # pyright: ignore[reportUnusedImport]
    )


def test_can_import_infrastructure() -> None:
    from stripe import (
        StripeContext,  # pyright: ignore[reportUnusedImport]
        StripeObject,  # pyright: ignore[reportUnusedImport]
        ListObject,  # pyright: ignore[reportUnusedImport]
        BaseAddress,  # pyright: ignore[reportUnusedImport]
    )
    from stripe.v2 import DeletedObject  # pyright: ignore[reportUnusedImport]


def test_can_import_app_info() -> None:
    from stripe import AppInfo  # pyright: ignore[reportUnusedImport]


def test_can_import_stripe_response() -> None:
    from stripe import (
        StripeResponse,  # pyright: ignore[reportUnusedImport]
        StripeResponseBase,  # pyright: ignore[reportUnusedImport]
        StripeStreamResponse,  # pyright: ignore[reportUnusedImport]
        StripeStreamResponseAsync,  # pyright: ignore[reportUnusedImport]
    )


def test_can_import_oauth_members() -> None:
    from stripe import OAuth

    assert OAuth is not None


def test_can_import_util() -> None:
    from stripe import convert_to_stripe_object  # pyright: ignore[reportUnusedImport]


def test_can_import_errors() -> None:
    # fmt: off
    from stripe import StripeError  # pyright: ignore[reportUnusedImport]
    from stripe import APIError  # pyright: ignore[reportUnusedImport]
    from stripe import OAuthErrorObject  # pyright: ignore[reportUnusedImport]
    from stripe import APIConnectionError  # pyright: ignore[reportUnusedImport]
    from stripe import StripeErrorWithParamCode  # pyright: ignore[reportUnusedImport]
    from stripe import CardError  # pyright: ignore[reportUnusedImport]
    from stripe import IdempotencyError  # pyright: ignore[reportUnusedImport]
    from stripe import InvalidRequestError  # pyright: ignore[reportUnusedImport]
    from stripe import AuthenticationError  # pyright: ignore[reportUnusedImport]
    from stripe import PermissionError  # pyright: ignore[reportUnusedImport]
    from stripe import RateLimitError  # pyright: ignore[reportUnusedImport]
    from stripe import SignatureVerificationError  # pyright: ignore[reportUnusedImport]
    # fmt: on


def test_can_import_namespaced_resource() -> None:
    from stripe import tax as TaxPackage
    from stripe.tax import (
        Calculation as CalculationFromStripe,
    )

    assert stripe.tax is TaxPackage
    assert stripe.tax.Calculation is CalculationFromStripe
    assert stripe.tax.Calculation is TaxPackage.Calculation

    assert_output("stripe.tax is not None", "True")
    assert_output("stripe.tax.Calculation is not None", "True")


def test_can_import_top_level_service() -> None:
    from stripe import AccountService as AccountServiceFromStripe

    assert stripe.AccountService == AccountServiceFromStripe

    assert_output("stripe.AccountService is not None", "True")


def test_can_import_namespaced_service() -> None:
    from stripe import tax as TaxPackage
    from stripe.tax import (
        CalculationService as CalculationServiceFromStripe,
    )

    assert stripe.tax is TaxPackage
    assert stripe.tax.CalculationService is CalculationServiceFromStripe
    assert stripe.tax.CalculationService is TaxPackage.CalculationService

    assert_output("stripe.tax is not None", "True")
    assert_output("stripe.tax.CalculationService is not None", "True")


def test_can_import_deeply_namespaced_service() -> None:
    from stripe import v2 as V2Package
    from stripe.v2 import billing as BillingPackage
    from stripe.v2.billing import (
        MeterEventService as MeterEventServiceFromStripe,
    )
    from stripe.v2.billing._meter_event_service import (
        MeterEventService as MeterEventServiceFromModule,
    )

    assert stripe.v2 is V2Package
    assert stripe.v2.billing is BillingPackage
    assert stripe.v2.billing.MeterEventService is MeterEventServiceFromStripe
    assert stripe.v2.billing.MeterEventService is MeterEventServiceFromModule

    assert_output("stripe.v2.billing.MeterEventService is not None", "True")
    assert_output("stripe.v2.billing.MeterEventService is not None", "True")


def test_can_import_nested_params_types() -> None:
    from stripe.params.checkout import (
        SessionCreateParamsLineItem,
    )
    from stripe.params import AccountSessionCreateParamsComponents

    assert SessionCreateParamsLineItem is not None
    assert AccountSessionCreateParamsComponents is not None
