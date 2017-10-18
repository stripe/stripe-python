from stripe.api_resources.abstract import CreateableAPIResource


class Token(CreateableAPIResource):
    OBJECT_NAME = 'token'
