from stripe.api_resources.abstract import ListableAPIResource


class OrderReturn(ListableAPIResource):
    OBJECT_NAME = 'order_return'

    @classmethod
    def class_url(cls):
        return '/v1/order_returns'
