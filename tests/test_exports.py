# pyright: strict
import stripe


def test_can_import_stripe_object() -> None:
    from stripe.stripe_object import StripeObject as StripeObjectFromStripeStripeObject

    assert stripe.stripe_object.StripeObject is StripeObjectFromStripeStripeObject


def test_can_import_top_level_resource() -> None:
    from stripe import Account as AccountFromStripe
    from stripe.api_resources import Account as AccountFromStripeResources
    from stripe.api_resources.account import Account as AccountFromStripeResourcesAccount

    assert stripe.Account == AccountFromStripe
    assert AccountFromStripe == AccountFromStripeResources
    assert AccountFromStripeResourcesAccount == AccountFromStripeResources


def test_can_import_namespaced_resource() -> None:
    from stripe import tax as TaxPackage
    from stripe.api_resources.tax import Calculation as CalculationFromResources
    from stripe.api_resources.tax.calculation import Calculation as CalculationFromResourcesCalculation

    assert stripe.tax is TaxPackage
    assert stripe.tax.Calculation is TaxPackage.Calculation
    assert stripe.tax.Calculation is CalculationFromResources
    assert CalculationFromResources is CalculationFromResourcesCalculation
