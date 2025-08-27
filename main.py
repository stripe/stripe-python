from stripe import StripeClient

client = StripeClient("sk_test_123")

customers = client.customers.list()

print(customers)
