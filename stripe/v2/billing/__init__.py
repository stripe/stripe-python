# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing import (
        bill_settings as bill_settings,
        collection_settings as collection_settings,
    )
    from stripe.v2.billing._bill_setting import BillSetting as BillSetting
    from stripe.v2.billing._bill_setting_service import (
        BillSettingService as BillSettingService,
    )
    from stripe.v2.billing._bill_setting_version import (
        BillSettingVersion as BillSettingVersion,
    )
    from stripe.v2.billing._cadence import Cadence as Cadence
    from stripe.v2.billing._cadence_service import (
        CadenceService as CadenceService,
    )
    from stripe.v2.billing._collection_setting import (
        CollectionSetting as CollectionSetting,
    )
    from stripe.v2.billing._collection_setting_service import (
        CollectionSettingService as CollectionSettingService,
    )
    from stripe.v2.billing._collection_setting_version import (
        CollectionSettingVersion as CollectionSettingVersion,
    )
    from stripe.v2.billing._meter_event import MeterEvent as MeterEvent
    from stripe.v2.billing._meter_event_adjustment import (
        MeterEventAdjustment as MeterEventAdjustment,
    )
    from stripe.v2.billing._meter_event_adjustment_service import (
        MeterEventAdjustmentService as MeterEventAdjustmentService,
    )
    from stripe.v2.billing._meter_event_service import (
        MeterEventService as MeterEventService,
    )
    from stripe.v2.billing._meter_event_session import (
        MeterEventSession as MeterEventSession,
    )
    from stripe.v2.billing._meter_event_session_service import (
        MeterEventSessionService as MeterEventSessionService,
    )
    from stripe.v2.billing._meter_event_stream_service import (
        MeterEventStreamService as MeterEventStreamService,
    )
    from stripe.v2.billing._profile import Profile as Profile
    from stripe.v2.billing._profile_service import (
        ProfileService as ProfileService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "bill_settings": ("stripe.v2.billing.bill_settings", True),
    "collection_settings": ("stripe.v2.billing.collection_settings", True),
    "BillSetting": ("stripe.v2.billing._bill_setting", False),
    "BillSettingService": ("stripe.v2.billing._bill_setting_service", False),
    "BillSettingVersion": ("stripe.v2.billing._bill_setting_version", False),
    "Cadence": ("stripe.v2.billing._cadence", False),
    "CadenceService": ("stripe.v2.billing._cadence_service", False),
    "CollectionSetting": ("stripe.v2.billing._collection_setting", False),
    "CollectionSettingService": (
        "stripe.v2.billing._collection_setting_service",
        False,
    ),
    "CollectionSettingVersion": (
        "stripe.v2.billing._collection_setting_version",
        False,
    ),
    "MeterEvent": ("stripe.v2.billing._meter_event", False),
    "MeterEventAdjustment": (
        "stripe.v2.billing._meter_event_adjustment",
        False,
    ),
    "MeterEventAdjustmentService": (
        "stripe.v2.billing._meter_event_adjustment_service",
        False,
    ),
    "MeterEventService": ("stripe.v2.billing._meter_event_service", False),
    "MeterEventSession": ("stripe.v2.billing._meter_event_session", False),
    "MeterEventSessionService": (
        "stripe.v2.billing._meter_event_session_service",
        False,
    ),
    "MeterEventStreamService": (
        "stripe.v2.billing._meter_event_stream_service",
        False,
    ),
    "Profile": ("stripe.v2.billing._profile", False),
    "ProfileService": ("stripe.v2.billing._profile_service", False),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()
