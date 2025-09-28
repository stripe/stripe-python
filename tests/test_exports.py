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
    from stripe import RequestOptions  # type: ignore[reportUnusedImport]


def test_can_import_http_client() -> None:
    from stripe import (
        HTTPClient,  # type: ignore[reportUnusedImport]
        PycurlClient,  # type: ignore[reportUnusedImport]
        RequestsClient,  # type: ignore[reportUnusedImport]
        UrlFetchClient,  # type: ignore[reportUnusedImport]
        new_default_http_client,  # type: ignore[reportUnusedImport]
    )


def test_can_import_webhook_members() -> None:
    from stripe import (
        Webhook,  # type: ignore[reportUnusedImport]
        WebhookSignature,  # type: ignore[reportUnusedImport]
    )


def test_can_import_abstract() -> None:
    from stripe import (
        APIResource,  # type: ignore[reportUnusedImport]
        SingletonAPIResource,  # type: ignore[reportUnusedImport]
        CreateableAPIResource,  # type: ignore[reportUnusedImport]
        UpdateableAPIResource,  # type: ignore[reportUnusedImport]
        DeletableAPIResource,  # type: ignore[reportUnusedImport]
        ListableAPIResource,  # type: ignore[reportUnusedImport]
        SearchableAPIResource,  # type: ignore[reportUnusedImport]
        VerifyMixin,  # type: ignore[reportUnusedImport]
        APIResourceTestHelpers,  # type: ignore[reportUnusedImport]
        custom_method,  # type: ignore[reportUnusedImport]
        nested_resource_class_methods,  # type: ignore[reportUnusedImport]
    )


def test_can_import_app_info() -> None:
    from stripe import AppInfo  # type: ignore[reportUnusedImport]


def test_can_import_stripe_response() -> None:
    from stripe import (
        StripeResponse,  # type: ignore[reportUnusedImport]
        StripeResponseBase,  # type: ignore[reportUnusedImport]
        StripeStreamResponse,  # type: ignore[reportUnusedImport]
    )


def test_can_import_oauth_members() -> None:
    from stripe import OAuth

    assert OAuth is not None


def test_can_import_util() -> None:
    from stripe import convert_to_stripe_object  # type: ignore[reportUnusedImport]


def test_can_import_errors() -> None:
    # fmt: off
    from stripe import StripeError  # type: ignore[reportUnusedImport]
    from stripe import APIError  # type: ignore[reportUnusedImport]
    from stripe import APIConnectionError  # type: ignore[reportUnusedImport]
    from stripe import StripeErrorWithParamCode  # type: ignore[reportUnusedImport]
    from stripe import CardError  # type: ignore[reportUnusedImport]
    from stripe import IdempotencyError  # type: ignore[reportUnusedImport]
    from stripe import InvalidRequestError  # type: ignore[reportUnusedImport]
    from stripe import AuthenticationError  # type: ignore[reportUnusedImport]
    from stripe import PermissionError  # type: ignore[reportUnusedImport]
    from stripe import RateLimitError  # type: ignore[reportUnusedImport]
    from stripe import SignatureVerificationError  # type: ignore[reportUnusedImport]
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
