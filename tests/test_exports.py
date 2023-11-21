# pyright: strict
from typing import Any
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


def test_can_import_list_search_objects() -> None:
    from stripe.api_resources import (
        ListObject as ListObjectFromApiResources,
        SearchResultObject as SearchObjectFromApiResources,
    )
    from stripe.stripe_object import (
        StripeObject,
    )

    assert (
        ListObjectFromApiResources[StripeObject]
        == stripe.ListObject[StripeObject]
    )
    assert (
        SearchObjectFromApiResources[StripeObject]
        == stripe.SearchResultObject[StripeObject]
    )


def test_can_import_misc_resources() -> None:
    from stripe.api_resources import ErrorObject, OAuthErrorObject, FileUpload

    assert ErrorObject is stripe.ErrorObject
    assert OAuthErrorObject is stripe.OAuthErrorObject
    assert FileUpload is stripe.FileUpload


def test_can_import_abstract() -> None:
    # fmt: off
    from stripe.api_resources.abstract import APIResource as APIResourceFromAbs
    from stripe.api_resources.abstract import SingletonAPIResource as SingletonFromAbs
    from stripe.api_resources.abstract import CreateableAPIResource as CreateableFromAbs
    from stripe.api_resources.abstract import UpdateableAPIResource as UpdateableFromAbs
    from stripe.api_resources.abstract import DeletableAPIResource as DeletableFromAbs
    from stripe.api_resources.abstract import ListableAPIResource as ListableFromAbs
    from stripe.api_resources.abstract import SearchableAPIResource as SearchableFromAbs
    from stripe.api_resources.abstract import VerifyMixin as VerifyMixinFromAbstract
    from stripe.api_resources.abstract import custom_method as custom_methodFromAbstract
    from stripe.api_resources.abstract import APIResourceTestHelpers as APIResourceTestHelpersFromAbstract
    from stripe.api_resources.abstract import nested_resource_class_methods as nested_resource_class_methodsFromAbstract
    # fmt: on

    from stripe.stripe_object import (
        StripeObject,
    )

    assert (
        APIResourceFromAbs[StripeObject]
        == stripe.abstract.APIResource[StripeObject]
    )
    assert (
        stripe.abstract.SingletonAPIResource[StripeObject]
        == SingletonFromAbs[StripeObject]
    )
    assert (
        stripe.abstract.CreateableAPIResource[StripeObject]
        == CreateableFromAbs[StripeObject]
    )
    assert (
        stripe.abstract.UpdateableAPIResource[StripeObject]
        == UpdateableFromAbs[StripeObject]
    )
    assert (
        stripe.abstract.DeletableAPIResource[StripeObject]
        == DeletableFromAbs[StripeObject]
    )
    assert (
        stripe.abstract.ListableAPIResource[StripeObject]
        == ListableFromAbs[StripeObject]
    )
    assert (
        stripe.abstract.SearchableAPIResource[StripeObject]
        == SearchableFromAbs[StripeObject]
    )
    assert stripe.abstract.VerifyMixin is VerifyMixinFromAbstract
    assert stripe.abstract.custom_method is custom_methodFromAbstract
    assert (
        stripe.abstract.APIResourceTestHelpers[Any]
        is APIResourceTestHelpersFromAbstract[Any]
    )
    assert (
        stripe.abstract.nested_resource_class_methods
        is nested_resource_class_methodsFromAbstract
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
