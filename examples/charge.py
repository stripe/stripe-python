"""
charge.py - Modern Stripe charge creation example

This example demonstrates:
  - Using the modern StripeClient (recommended approach)
  - Creating charges with proper error handling
  - Using current API parameters (source/payment_method instead of deprecated 'card')
  - Both one-time and saved payment method examples

Note: Direct charge creation is less common now. Most applications use:
  - Payment Intents (recommended for most use cases)
  - Checkout Sessions (for hosted payment pages)
  - Setup Intents (for saving payment methods)

Prerequisites:
  - Set STRIPE_SECRET_KEY environment variable
  - For testing, use test tokens like 'tok_visa'
"""

import os
from stripe import StripeClient

# Initialize the modern StripeClient
api_key = os.environ.get("STRIPE_SECRET_KEY")
if not api_key:
    print("Error: Please set STRIPE_SECRET_KEY environment variable")
    exit(1)

client = StripeClient(api_key)

def create_simple_charge():
    """Create a simple charge using a test token"""
    print("Creating simple charge...")

    try:
        charge = client.charges.create(
            amount=2000,  # $20.00 in cents
            currency="usd",
            source="tok_visa",  # Test token for Visa card
            description="Example charge for customer@example.com",
        )

        print("Charge successful!")
        print(f"Charge ID: {charge.id}")
        print(f"Amount: ${charge.amount/100:.2f}")
        print(f"Status: {charge.status}")
        print(f"Receipt URL: {charge.receipt_url}")

        return charge

    except Exception as e:
        print(f"Charge failed: {str(e)}")
        return None

def create_charge_with_customer():
    """Create a charge for an existing customer"""
    print("\nCreating charge for existing customer...")

    try:
        # First, create a customer (in real app, you'd retrieve existing customer)
        customer = client.customers.create(
            email="customer@example.com",
            name="Example Customer",
            source="tok_visa"
        )
        print(f"   Created customer: {customer.id}")

        # Now create charge for this customer
        charge = client.charges.create(
            amount=1500,  # $15.00
            currency="usd",
            customer=customer.id,  # Charge the customer's default source
            description="Charge for existing customer",
        )

        print("Customer charge successful!")
        print(f"Charge ID: {charge.id}")
        print(f"Customer: {charge.customer}")
        print(f"Amount: ${charge.amount/100:.2f}")

        return charge

    except Exception as e:
        print(f"Customer charge failed: {str(e)}")
        return None

def create_charge_with_metadata():
    """Create a charge with custom metadata"""
    print("\n📋 Creating charge with metadata...")

    try:
        charge = client.charges.create(
            amount=3000,  # $30.00
            currency="usd",
            source="tok_visa",
            description="Order #12345 - Premium Plan",
            metadata={
                "order_id": "12345",
                "customer_id": "cus_example",
                "plan": "premium",
                "campaign": "summer_sale"
            }
        )

        print("Charge with metadata successful!")
        print(f"Charge ID: {charge.id}")
        print(f"Metadata: {charge.metadata}")

        return charge

    except Exception as e:
        print(f"❌ Metadata charge failed: {str(e)}")
        return None

def demonstrate_error_handling():
    """Show different types of charge errors"""
    print("\nDemonstrating error handling...")

    # Example 1: Invalid card
    try:
        charge = client.charges.create(
            amount=1000,
            currency="usd",
            source="tok_chargeDeclined",  # This will be declined
            description="This charge will be declined",
        )
    except Exception as e:
        print(f"   Expected decline: {str(e)}")

    # Example 2: Invalid amount
    try:
        charge = client.charges.create(
            amount=-100,  # Negative amount is invalid
            currency="usd",
            source="tok_visa",
            description="Invalid amount",
        )
    except Exception as e:
        print(f"   Expected invalid amount: {str(e)}")

def modern_payment_intent_example():
    """Show the modern recommended approach using Payment Intents"""
    print("\nModern approach - Payment Intent (RECOMMENDED):")
    print("   For new applications, use Payment Intents instead of direct charges:")

    try:
        payment_intent = client.payment_intents.create(
            amount=2500,  # $25.00
            currency="usd",
            automatic_payment_methods={"enabled": True},
            description="Modern payment using Payment Intent",
        )

        print("Payment Intent created!")
        print(f"Payment Intent ID: {payment_intent.id}")
        print(f"Status: {payment_intent.status}")
        print(f"Client Secret: {payment_intent.client_secret[:20]}...")
        print("Use client_secret on frontend to complete payment")

        return payment_intent

    except Exception as e:
        print(f"Payment Intent failed: {str(e)}")
        return None

if __name__ == "__main__":
    print("Stripe Charge Examples")
    print("=" * 50)

    # Run examples
    create_simple_charge()
    create_charge_with_customer()
    create_charge_with_metadata()
    demonstrate_error_handling()
    modern_payment_intent_example()

    print("\n" + "=" * 50)
    print("All examples completed!")
    print("\nRemember:")
    print("   - For new apps, use Payment Intents instead of direct charges")
    print("   - Always handle errors gracefully")
    print("   - Use metadata to track business information")
    print("   - Test with Stripe's test tokens before going live")
