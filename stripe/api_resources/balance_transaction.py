from stripe.api_resources.abstract import ListableAPIResource


class BalanceTransaction(ListableAPIResource):
    OBJECT_NAME = 'balance_transaction'

    @classmethod
    def class_url(cls):
        return '/v1/balance/history'
