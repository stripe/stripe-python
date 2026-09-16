# this file is typechecked since it's mostly here to cover type errors
# as a result, the actual assertions are pretty basic

import pytest
from typing_extensions import assert_type

from stripe._stripe_object import UntypedStripeObject, StripeObject
from stripe._subscription import Subscription


def test_metadata_typing():
    # the exact class doesn't matter here, just something with a `metadata` property
    obj = Subscription.construct_from({"metadata": {"some": "value"}}, "mykey")

    # metadata has special type handling
    assert_type(obj.metadata, UntypedStripeObject[str])

    # but it's just a stripeobject at runtime
    assert obj.metadata.to_dict() == {"some": "value"}

    # but it also allows arbitrary read-write-del without type errors
    obj.metadata.other = "thing"

    assert obj.metadata.other == "thing"

    del obj.metadata.other

    assert not hasattr(obj.metadata, "other")

    # other types are an error (though they _do_ work)
    obj.metadata.whatever = 3  # type: ignore[reportArgumentType]

    # put this last so it doesn't affect typechecking in this test
    assert isinstance(obj.metadata, StripeObject)
    # it's a type-only class without runtime impact
    assert not isinstance(obj.metadata, UntypedStripeObject)

    # and will error if ever used
    with pytest.raises(ValueError):
        UntypedStripeObject()
