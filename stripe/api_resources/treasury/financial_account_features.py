# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal


class FinancialAccountFeatures(StripeObject):
    """
    Encodes whether a FinancialAccount has access to a particular Feature, with a `status` enum and associated `status_details`.
    Stripe or the platform can control Features via the requested field.
    """

    OBJECT_NAME = "treasury.financial_account_features"

    class CardIssuing(StripeObject):
        class StatusDetail(StripeObject):
            code: Literal[
                "activating",
                "capability_not_requested",
                "financial_account_closed",
                "rejected_other",
                "rejected_unsupported_business",
                "requirements_past_due",
                "requirements_pending_verification",
                "restricted_by_platform",
                "restricted_other",
            ]
            resolution: Optional[
                Literal[
                    "contact_stripe",
                    "provide_information",
                    "remove_restriction",
                ]
            ]
            restriction: Optional[Literal["inbound_flows", "outbound_flows"]]

        requested: bool
        status: Literal["active", "pending", "restricted"]
        status_details: List[StatusDetail]
        _inner_class_types = {"status_details": StatusDetail}

    class DepositInsurance(StripeObject):
        class StatusDetail(StripeObject):
            code: Literal[
                "activating",
                "capability_not_requested",
                "financial_account_closed",
                "rejected_other",
                "rejected_unsupported_business",
                "requirements_past_due",
                "requirements_pending_verification",
                "restricted_by_platform",
                "restricted_other",
            ]
            resolution: Optional[
                Literal[
                    "contact_stripe",
                    "provide_information",
                    "remove_restriction",
                ]
            ]
            restriction: Optional[Literal["inbound_flows", "outbound_flows"]]

        requested: bool
        status: Literal["active", "pending", "restricted"]
        status_details: List[StatusDetail]
        _inner_class_types = {"status_details": StatusDetail}

    class FinancialAddresses(StripeObject):
        class Aba(StripeObject):
            class StatusDetail(StripeObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                resolution: Optional[
                    Literal[
                        "contact_stripe",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]

            requested: bool
            status: Literal["active", "pending", "restricted"]
            status_details: List[StatusDetail]
            _inner_class_types = {"status_details": StatusDetail}

        aba: Optional[Aba]
        _inner_class_types = {"aba": Aba}

    class InboundTransfers(StripeObject):
        class Ach(StripeObject):
            class StatusDetail(StripeObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                resolution: Optional[
                    Literal[
                        "contact_stripe",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]

            requested: bool
            status: Literal["active", "pending", "restricted"]
            status_details: List[StatusDetail]
            _inner_class_types = {"status_details": StatusDetail}

        ach: Optional[Ach]
        _inner_class_types = {"ach": Ach}

    class IntraStripeFlows(StripeObject):
        class StatusDetail(StripeObject):
            code: Literal[
                "activating",
                "capability_not_requested",
                "financial_account_closed",
                "rejected_other",
                "rejected_unsupported_business",
                "requirements_past_due",
                "requirements_pending_verification",
                "restricted_by_platform",
                "restricted_other",
            ]
            resolution: Optional[
                Literal[
                    "contact_stripe",
                    "provide_information",
                    "remove_restriction",
                ]
            ]
            restriction: Optional[Literal["inbound_flows", "outbound_flows"]]

        requested: bool
        status: Literal["active", "pending", "restricted"]
        status_details: List[StatusDetail]
        _inner_class_types = {"status_details": StatusDetail}

    class OutboundPayments(StripeObject):
        class Ach(StripeObject):
            class StatusDetail(StripeObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                resolution: Optional[
                    Literal[
                        "contact_stripe",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]

            requested: bool
            status: Literal["active", "pending", "restricted"]
            status_details: List[StatusDetail]
            _inner_class_types = {"status_details": StatusDetail}

        class UsDomesticWire(StripeObject):
            class StatusDetail(StripeObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                resolution: Optional[
                    Literal[
                        "contact_stripe",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]

            requested: bool
            status: Literal["active", "pending", "restricted"]
            status_details: List[StatusDetail]
            _inner_class_types = {"status_details": StatusDetail}

        ach: Optional[Ach]
        us_domestic_wire: Optional[UsDomesticWire]
        _inner_class_types = {"ach": Ach, "us_domestic_wire": UsDomesticWire}

    class OutboundTransfers(StripeObject):
        class Ach(StripeObject):
            class StatusDetail(StripeObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                resolution: Optional[
                    Literal[
                        "contact_stripe",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]

            requested: bool
            status: Literal["active", "pending", "restricted"]
            status_details: List[StatusDetail]
            _inner_class_types = {"status_details": StatusDetail}

        class UsDomesticWire(StripeObject):
            class StatusDetail(StripeObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                resolution: Optional[
                    Literal[
                        "contact_stripe",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]

            requested: bool
            status: Literal["active", "pending", "restricted"]
            status_details: List[StatusDetail]
            _inner_class_types = {"status_details": StatusDetail}

        ach: Optional[Ach]
        us_domestic_wire: Optional[UsDomesticWire]
        _inner_class_types = {"ach": Ach, "us_domestic_wire": UsDomesticWire}

    card_issuing: Optional[CardIssuing]
    deposit_insurance: Optional[DepositInsurance]
    financial_addresses: Optional[FinancialAddresses]
    inbound_transfers: Optional[InboundTransfers]
    intra_stripe_flows: Optional[IntraStripeFlows]
    object: Literal["treasury.financial_account_features"]
    outbound_payments: Optional[OutboundPayments]
    outbound_transfers: Optional[OutboundTransfers]

    _inner_class_types = {
        "card_issuing": CardIssuing,
        "deposit_insurance": DepositInsurance,
        "financial_addresses": FinancialAddresses,
        "inbound_transfers": InboundTransfers,
        "intra_stripe_flows": IntraStripeFlows,
        "outbound_payments": OutboundPayments,
        "outbound_transfers": OutboundTransfers,
    }
