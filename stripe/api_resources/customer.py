from __future__ import absolute_import, division, print_function

import warnings

from stripe import api_requestor, util
from stripe.api_resources.charge import Charge
from stripe.api_resources.invoice import Invoice
from stripe.api_resources.invoice_item import InvoiceItem
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods(
    'source',
    operations=['create', 'retrieve', 'update', 'delete', 'list']
)
class Customer(CreateableAPIResource, UpdateableAPIResource,
               ListableAPIResource, DeletableAPIResource):
    OBJECT_NAME = 'customer'
