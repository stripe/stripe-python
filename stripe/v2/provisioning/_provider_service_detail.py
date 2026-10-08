# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import Any, ClassVar, List, Optional
from typing_extensions import Literal


class ProviderServiceDetail(StripeObject):
    """
    The `ProviderServiceDetail` resource represents a service offered by a
    provider in the catalog.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.provisioning.provider_service_detail"]
    ] = "v2.provisioning.provider_service_detail"

    class AllowedUpdate(StripeObject):
        direction: Literal["any", "down", "up"]
        """
        Whether the target service appears in upgrade flows, downgrade flows, or both.
        """
        service: str
        """
        Identifier of a service to which a resource can be updated.
        """

    class Constraint(StripeObject):
        class Count(StripeObject):
            at_most: int
            """
            Maximum number of active resources for the service within its scope.
            """

        count: Optional[Count]
        """
        Limit on the number of active resources for the service.
        """
        mutual_exclusion_allowed_updates: Optional[bool]
        """
        Whether provisioning is blocked when an allowed-update target is active in the same scope.
        """
        type: Literal["count", "mutual_exclusion_allowed_updates"]
        """
        Kind of constraint represented by this entry.
        """
        _inner_class_types = {"count": Count}

    class Pricing(StripeObject):
        class Component(StripeObject):
            class Option(StripeObject):
                class Paid(StripeObject):
                    description: Optional[str]
                    """
                    Additional display information about the price.
                    """
                    freeform: Optional[str]
                    """
                    Provider-supplied pricing terms, set when `type` is `freeform`.
                    """
                    type: Literal["free", "freeform"]
                    """
                    Kind of pricing represented by this entry.
                    """

                is_default: Optional[bool]
                """
                Whether this option applies when no parent-service-specific option matches.
                """
                paid: Paid
                """
                Pricing details for this option, set when `type` is `paid`.
                """
                parent_services: List[str]
                """
                Identifiers of active parent services for which this option applies.
                """
                type: Literal["free", "paid"]
                """
                Whether the component is free or paid when this option applies.
                """
                _inner_class_types = {"paid": Paid}

            options: List[Option]
            """
            Pricing options selected according to the resource's active parent services.
            """
            _inner_class_types = {"options": Option}

        class Paid(StripeObject):
            description: Optional[str]
            """
            Additional display information about the price.
            """
            freeform: Optional[str]
            """
            Provider-supplied pricing terms, set when `type` is `freeform`.
            """
            type: Literal["free", "freeform"]
            """
            Kind of pricing represented by this entry.
            """

        class PaidPricing(StripeObject):
            configuration: UntypedStripeObject[Any]
            """
            Service configuration values for which this pricing entry applies.
            """
            description: Optional[str]
            """
            Additional display information about the price.
            """
            freeform: Optional[str]
            """
            Provider-supplied pricing terms, set when `type` is `freeform`.
            """
            is_default: Optional[bool]
            """
            Whether this entry is the fallback when no configuration-specific entry matches.
            """
            type: Literal["free", "freeform"]
            """
            Kind of pricing represented by this entry.
            """

        component: Component
        """
        Parent-service-dependent pricing details, set when `type` is `component`.
        """
        paid: Paid
        """
        Legacy compatibility field for top-level paid pricing.
        Mirrors the single paid pricing entry when only one exists, or the entry marked
        `is_default`. If multiple paid pricing entries exist and none is default, this field
        is unset.
        """
        paid_pricing: List[PaidPricing]
        """
        Canonical top-level paid pricing entries for this service.
        When multiple entries are present, callers should read this field instead of `paid`.
        """
        type: Literal["component", "free", "paid"]
        """
        Pricing model for the service: free, paid, or dependent on a parent service.
        """
        _inner_class_types = {
            "component": Component,
            "paid": Paid,
            "paid_pricing": PaidPricing,
        }

    allowed_updates: List[AllowedUpdate]
    """
    Updates allowed for resources using this service.
    """
    availability: Literal["available", "not_in_country", "unavailable"]
    """
    Availability of the service.
    """
    categories: List[str]
    """
    Categories the service belongs to.
    """
    configuration_schema: UntypedStripeObject[Any]
    """
    Schema describing the configuration accepted by this service.
    """
    constraints: List[Constraint]
    """
    Constraints on resources using this service.
    """
    created: str
    """
    Time at which the service was created.
    """
    description: str
    """
    Description of the service.
    """
    development: bool
    """
    Denormalized from the parent Provider. If a Provider's partition changes, re-sync its services.
    proto3 scalar defaults apply: if unset, this value is `false`.
    """
    group: Optional[str]
    """
    Group the service belongs to, used to organize related services.
    """
    id: str
    """
    Unique identifier for the provider service.
    """
    kind: Literal["deployable", "plan"]
    """
    Kind of the service.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    llm_context: Optional[str]
    """
    URL of additional context about the service intended for LLM consumption.
    """
    object: Literal["v2.provisioning.provider_service_detail"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    pricing: Pricing
    """
    Pricing details for the service.
    """
    provider: str
    """
    Identifier of the provider that offers this service.
    """
    provider_name: str
    """
    Human-readable name of the provider that offers this service.
    """
    scope: Literal["account", "project"]
    """
    Scope of the service.
    """
    service_id: str
    """
    Identifier of the service, unique within its provider.
    """
    updateable_to: List[str]
    """
    Deprecated: use allowed_updates instead.
    """
    _inner_class_types = {
        "allowed_updates": AllowedUpdate,
        "constraints": Constraint,
        "pricing": Pricing,
    }
