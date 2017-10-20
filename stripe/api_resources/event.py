from stripe.api_resources import abstract


class Event(abstract.ListableAPIResource):
    OBJECT_NAME = 'event'
