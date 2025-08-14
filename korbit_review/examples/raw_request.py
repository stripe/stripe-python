from stripe import StripeClient

# Set your API key here
api_key = "{{API_KEY}}"

client = StripeClient(api_key)
response = client.raw_request(
    "post",
    "/v1/beta_endpoint",
    param=123,
    stripe_version="2022-11-15; feature_beta=v3",
)

# (Optional) response is a StripeResponse. You can use `client.deserialize` to get a StripeObject.
deserialized_resp = client.deserialize(response, api_mode="V1")
