from concurrent.futures import ThreadPoolExecutor
import stripe

stripe.api_key = "sk_test_xyz"


def create_customer(i):
    try:
        stripe.Customer.create()
    except:
        pass


stripe.reuse_sessions = False
print("reuse_sessions:", stripe.reuse_sessions)
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(create_customer, range(20))
