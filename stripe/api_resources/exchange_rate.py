from stripe.api_resources.abstract import ListableAPIResource


class ExchangeRate(ListableAPIResource):
    OBJECT_NAME = 'exchange_rate'

    @classmethod
    def class_name(cls):
        return 'exchange_rate'
