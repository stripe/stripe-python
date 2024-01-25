# pyright: strict
# we specifically test various import patterns
from typing import Any
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


def test_can_import_stripe_object() -> None:
    from stripe.stripe_object import StripeObject as StripeObjectFromStripeStripeObject  # type: ignore
    from stripe import (
        StripeObject as StripeObjectFromStripe,
    )

    assert (
        stripe.stripe_object.StripeObject is StripeObjectFromStripeStripeObject  # type: ignore
    )
    assert stripe.StripeObject is StripeObjectFromStripeStripeObject
    assert StripeObjectFromStripe is StripeObjectFromStripeStripeObject


def test_can_import_request_options() -> None:
    from stripe.request_options import RequestOptions as RequestOptionsStripeRequestOptions  # type: ignore
    from stripe import (
        RequestOptions as RequestOptionsFromStripe,
    )

    assert stripe.RequestOptions is RequestOptionsStripeRequestOptions
    assert RequestOptionsFromStripe is RequestOptionsStripeRequestOptions


def test_can_import_http_client() -> None:
    from stripe.http_client import HTTPClient as HTTPClientFromStripeHTTPClient  # type: ignore
    from stripe.http_client import PycurlClient as PycurlClientFromStripeHTTPClient  # type: ignore
    from stripe.http_client import RequestsClient as RequestsClientFromStripeHTTPClient  # type: ignore
    from stripe.http_client import UrlFetchClient as UrlFetchClientFromStripeHTTPClient  # type: ignore
    from stripe.http_client import new_default_http_client as new_default_http_clientFromStripeHTTPClient  # type: ignore

    from stripe import (
        HTTPClient as HTTPClientFromStripe,
        PycurlClient as PycurlClientFromStripe,
        RequestsClient as RequestsClientFromStripe,
        UrlFetchClient as UrlFetchClientFromStripe,
        new_default_http_client as new_default_http_clientFromStripe,
    )

    assert HTTPClientFromStripe is HTTPClientFromStripeHTTPClient
    assert PycurlClientFromStripe is PycurlClientFromStripeHTTPClient
    assert RequestsClientFromStripe is RequestsClientFromStripeHTTPClient
    assert UrlFetchClientFromStripe is UrlFetchClientFromStripeHTTPClient
    assert (
        new_default_http_clientFromStripe
        is new_default_http_clientFromStripeHTTPClient
    )

    assert stripe.HTTPClient is HTTPClientFromStripeHTTPClient
    assert stripe.PycurlClient is PycurlClientFromStripeHTTPClient
    assert stripe.RequestsClient is RequestsClientFromStripeHTTPClient
    assert stripe.UrlFetchClient is UrlFetchClientFromStripeHTTPClient
    assert (
        stripe.new_default_http_client
        is new_default_http_clientFromStripeHTTPClient
    )


def test_can_import_webhook_members() -> None:
    from stripe.webhook import Webhook as WebhookFromStripeWebhook  # type: ignore
    from stripe.webhook import WebhookSignature as WebhookSignatureFromStripeWebhook  # type: ignore

    from stripe import (
        Webhook,
        WebhookSignature,
    )

    assert Webhook is not None
    assert WebhookSignature is not None

    assert WebhookFromStripeWebhook is Webhook
    assert WebhookSignatureFromStripeWebhook is WebhookSignature


def test_can_import_list_search_objects() -> None:

    # This import has to be single line, mypy and pyright are producing errors
    # on different lines of multiline import
    # fmt: off
    from stripe.api_resources import ListObject as ListObjectFromResources  # type: ignore
    from stripe import ListObject as LOFromStripe
    from stripe.api_resources import SearchResultObject as SearchObjectFromResources  # type: ignore
    from stripe import SearchResultObject as SOFromStripe
    # fmt: on

    from stripe import StripeObject

    assert (
        ListObjectFromResources[StripeObject]
        == stripe.ListObject[StripeObject]
    )
    assert (
        SearchObjectFromResources[StripeObject]
        == stripe.SearchResultObject[StripeObject]
    )
    assert ListObjectFromResources[StripeObject] == LOFromStripe[StripeObject]
    assert (
        SearchObjectFromResources[StripeObject] == SOFromStripe[StripeObject]
    )


def test_can_import_misc_resources() -> None:
    from stripe.api_resources import ErrorObject, OAuthErrorObject  # type: ignore
    from stripe import (
        ErrorObject as ErrorObjectFromStripe,
        OAuthErrorObject as OAuthErrorObjectFromStripe,
    )
    from stripe.api_resources.error_object import ErrorObject as ErrorObjectFromStripeApiResources  # type: ignore
    from stripe.api_resources.error_object import OAuthErrorObject as OAuthErrorObjectFromStripeApiResources  # type: ignore

    # FileUpload is an old alias for File, time to hide it
    from stripe.api_resources import FileUpload as FileUploadFromApiResources  # type: ignore
    from stripe import FileUpload as FileUploadFromStripe  # type: ignore

    assert ErrorObject is stripe.ErrorObject
    assert ErrorObjectFromStripe is stripe.ErrorObject
    assert ErrorObjectFromStripe is ErrorObjectFromStripeApiResources

    assert OAuthErrorObject is stripe.OAuthErrorObject
    assert OAuthErrorObjectFromStripe is stripe.OAuthErrorObject
    assert OAuthErrorObject is OAuthErrorObjectFromStripeApiResources

    assert FileUploadFromApiResources is stripe.FileUpload  # type: ignore
    assert FileUploadFromApiResources is FileUploadFromStripe

    assert_output("stripe.error is not None", "True")


def test_can_import_abstract() -> None:
    # fmt: off
    from stripe.api_resources.abstract import APIResource as APIResourceFromAbstract  # type: ignore
    from stripe.api_resources.abstract import SingletonAPIResource as SingletonFromAbstract  # type: ignore
    from stripe.api_resources.abstract import CreateableAPIResource as CreateableFromAbstract  # type: ignore
    from stripe.api_resources.abstract import UpdateableAPIResource as UpdateableFromAbstract  # type: ignore
    from stripe.api_resources.abstract import DeletableAPIResource as DeletableFromAbstract  # type: ignore
    from stripe.api_resources.abstract import ListableAPIResource as ListableFromAbstract  # type: ignore
    from stripe.api_resources.abstract import SearchableAPIResource as SearchableFromAbstract  # type: ignore
    from stripe.api_resources.abstract import VerifyMixin as VerifyMixinFromAbstract  # type: ignore
    from stripe.api_resources.abstract import APIResourceTestHelpers as APIResourceTestHelpersFromAbstract  # type: ignore
    from stripe.api_resources.abstract import custom_method as custom_methodFromAbstract
    from stripe.api_resources.abstract import nested_resource_class_methods as nested_resource_class_methodsFromAbstract
    from stripe import APIResource as APIResourceFromStripe
    from stripe import SingletonAPIResource as SingletonFromStripe
    from stripe import CreateableAPIResource as CreateableFromStripe
    from stripe import UpdateableAPIResource as UpdateableFromStripe
    from stripe import DeletableAPIResource as DeletableFromStripe
    from stripe import ListableAPIResource as ListableFromStripe
    from stripe import SearchableAPIResource as SearchableFromStripe
    from stripe import VerifyMixin as VerifyMixinFromStripe
    from stripe import APIResourceTestHelpers as APIResourceTestHelpersFromStripe
    from stripe import custom_method as custom_methodFromStripe  # pyright: ignore[reportDeprecated]
    from stripe import nested_resource_class_methods as nested_resource_class_methodsFromStripe
    # fmt: on

    from stripe.stripe_object import StripeObject  # type: ignore

    assert (
        APIResourceFromAbstract[StripeObject]
        == stripe.abstract.APIResource[StripeObject]  # type: ignore
    )
    assert (
        stripe.abstract.SingletonAPIResource[StripeObject]  # type: ignore
        == SingletonFromAbstract[StripeObject]
    )
    assert (
        stripe.abstract.CreateableAPIResource[StripeObject]  # type: ignore
        == CreateableFromAbstract[StripeObject]
    )
    assert (
        stripe.abstract.UpdateableAPIResource[StripeObject]  # type: ignore
        == UpdateableFromAbstract[StripeObject]
    )
    assert (
        stripe.abstract.DeletableAPIResource[StripeObject]  # type: ignore
        == DeletableFromAbstract[StripeObject]
    )
    assert (
        stripe.abstract.ListableAPIResource[StripeObject]  # type: ignore
        == ListableFromAbstract[StripeObject]
    )
    assert (
        stripe.abstract.SearchableAPIResource[StripeObject]  # type: ignore
        == SearchableFromAbstract[StripeObject]
    )
    assert stripe.abstract.VerifyMixin is VerifyMixinFromAbstract  # type: ignore
    assert (
        stripe.abstract.custom_method is custom_methodFromAbstract  # type: ignore
    )
    assert (
        stripe.abstract.APIResourceTestHelpers[Any]  # type: ignore
        is APIResourceTestHelpersFromAbstract[Any]
    )
    assert (
        stripe.abstract.nested_resource_class_methods  # type: ignore
        is nested_resource_class_methodsFromAbstract
    )

    assert APIResourceFromStripe is APIResourceFromAbstract
    assert SingletonFromStripe is SingletonFromAbstract
    assert CreateableFromStripe is CreateableFromAbstract
    assert UpdateableFromStripe is UpdateableFromAbstract
    assert DeletableFromStripe is DeletableFromAbstract
    assert ListableFromStripe is ListableFromAbstract
    assert SearchableFromStripe is SearchableFromAbstract
    assert VerifyMixinFromStripe is VerifyMixinFromAbstract
    assert (
        APIResourceTestHelpersFromStripe is APIResourceTestHelpersFromAbstract
    )
    assert custom_methodFromStripe is custom_methodFromAbstract
    assert (
        nested_resource_class_methodsFromStripe
        is nested_resource_class_methodsFromAbstract
    )


def test_can_import_app_info() -> None:
    from stripe.app_info import AppInfo as AppInfoFromStripeAppInfo  # type: ignore
    from stripe import AppInfo as AppInfoFromStripe

    assert AppInfoFromStripeAppInfo is AppInfoFromStripe
    assert AppInfoFromStripeAppInfo is stripe.AppInfo


def test_can_import_stripe_response() -> None:
    from stripe.stripe_response import StripeResponse as StripeResponseFromStripeResponse  # type: ignore
    from stripe.stripe_response import StripeResponseBase as StripeResponseBaseFromStripeResponse  # type: ignore
    from stripe.stripe_response import StripeStreamResponse as StripeStreamResponseFromStripeResponse  # type: ignore

    from stripe import (
        StripeResponse as StripeResponseFromStripe,
        StripeResponseBase as StripeResponseBaseFromStripe,
        StripeStreamResponse as StripeStreamResponseFromStripe,
    )

    assert (
        StripeResponseFromStripeResponse
        is stripe.stripe_response.StripeResponse  # type: ignore
    )

    assert StripeResponseFromStripe is StripeResponseFromStripeResponse

    assert StripeResponseFromStripe is stripe.StripeResponse

    assert StripeResponseBaseFromStripe is StripeResponseBaseFromStripeResponse

    assert StripeResponseBaseFromStripe is stripe.StripeResponseBase

    assert (
        StripeStreamResponseFromStripe
        is StripeStreamResponseFromStripeResponse
    )

    assert StripeStreamResponseFromStripe is stripe.StripeStreamResponse


def test_can_import_oauth_members() -> None:
    from stripe.oauth import OAuth as OAuthFromStripeOAuth  # type: ignore
    from stripe import (
        OAuth,
    )

    assert OAuth is not None
    assert OAuthFromStripeOAuth is OAuth
    assert OAuthFromStripeOAuth is stripe.OAuth


def test_can_import_util() -> None:
    from stripe.util import convert_to_stripe_object as convert_to_stripe_objectFromStripeUtil  # type: ignore
    from stripe import (
        convert_to_stripe_object as convert_to_stripe_objectFromStripe,
    )

    assert (
        stripe.convert_to_stripe_object is convert_to_stripe_objectFromStripe
    )
    assert (
        convert_to_stripe_objectFromStripe
        is convert_to_stripe_objectFromStripeUtil
    )
    assert stripe.util.io is not None  # type: ignore
    assert_output("stripe.util is not None", "True")


def test_can_import_errors() -> None:
    # fmt: off
    from stripe.error import StripeError as StripeErrorFromStripeError  # type: ignore
    from stripe.error import APIError as APIErrorFromStripeError  # type: ignore
    from stripe.error import APIConnectionError as APIConnectionErrorFromStripeError  # type: ignore
    from stripe.error import StripeErrorWithParamCode as StripeErrorWithParamCodeFromStripeError  # type: ignore
    from stripe.error import CardError as CardErrorFromStripeError  # type: ignore
    from stripe.error import IdempotencyError as IdempotencyErrorFromStripeError  # type: ignore
    from stripe.error import InvalidRequestError as InvalidRequestErrorFromStripeError  # type: ignore
    from stripe.error import AuthenticationError as AuthenticationErrorFromStripeError  # type: ignore
    from stripe.error import PermissionError as PermissionErrorFromStripeError  # type: ignore
    from stripe.error import RateLimitError as RateLimitErrorFromStripeError  # type: ignore
    from stripe.error import SignatureVerificationError as SignatureVerificationErrorFromStripeError  # type: ignore
    # fmt: on

    from stripe import StripeError as StripeErrorFromStripe
    from stripe import APIError as APIErrorFromStripe
    from stripe import APIConnectionError as APIConnectionErrorFromStripe
    from stripe import (
        StripeErrorWithParamCode as StripeErrorWithParamCodeFromStripe,
    )
    from stripe import CardError as CardErrorFromStripe
    from stripe import IdempotencyError as IdempotencyErrorFromStripe
    from stripe import InvalidRequestError as InvalidRequestErrorFromStripe
    from stripe import AuthenticationError as AuthenticationErrorFromStripe
    from stripe import PermissionError as PermissionErrorFromStripe
    from stripe import RateLimitError as RateLimitErrorFromStripe
    from stripe import (
        SignatureVerificationError as SignatureVerificationErrorFromStripe,
    )

    assert StripeErrorFromStripeError is StripeErrorFromStripe
    assert APIErrorFromStripeError is APIErrorFromStripe
    assert APIConnectionErrorFromStripeError is APIConnectionErrorFromStripe
    assert (
        StripeErrorWithParamCodeFromStripeError
        is StripeErrorWithParamCodeFromStripe
    )
    assert CardErrorFromStripeError is CardErrorFromStripe
    assert IdempotencyErrorFromStripeError is IdempotencyErrorFromStripe
    assert InvalidRequestErrorFromStripeError is InvalidRequestErrorFromStripe
    assert AuthenticationErrorFromStripeError is AuthenticationErrorFromStripe
    assert PermissionErrorFromStripeError is PermissionErrorFromStripe
    assert RateLimitErrorFromStripeError is RateLimitErrorFromStripe
    assert (
        SignatureVerificationErrorFromStripeError
        is SignatureVerificationErrorFromStripe
    )


def test_can_import_top_level_resource() -> None:
    from stripe import Account as AccountFromStripe
    from stripe.api_resources import Account as AccountFromStripeResources  # type: ignore

    # This import has to be single line, mypy and pyright are producing errors
    # on different lines of multiline import
    from stripe.api_resources.account import Account as AccFromModule  # type: ignore

    assert stripe.Account == AccountFromStripe
    assert AccountFromStripe == AccountFromStripeResources
    assert AccFromModule == AccountFromStripeResources

    assert_output("stripe.api_resources.Account is not None", "True")
    assert_output("stripe.api_resources.account is not None", "True")
    assert_output("stripe.api_resources.account.Account is not None", "True")


def test_can_import_namespaced_resource() -> None:
    from stripe import tax as TaxPackage
    from stripe.tax import (
        Calculation as CalculationFromStripe,
    )

    # This import has to be single line, mypy and pyright are producing errors
    # on different lines of multiline import
    from stripe.api_resources.tax import Calculation as CalcFromResources  # type: ignore

    # This import has to be single line, mypy and pyright are producing errors
    # on different lines of multiline import
    from stripe.api_resources.tax.calculation import Calculation as CalcFromModule  # type: ignore

    assert stripe.tax is TaxPackage
    assert stripe.tax.Calculation is CalculationFromStripe
    assert stripe.tax.Calculation is TaxPackage.Calculation
    assert stripe.tax.Calculation is CalcFromResources
    assert CalcFromResources is CalcFromModule

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
