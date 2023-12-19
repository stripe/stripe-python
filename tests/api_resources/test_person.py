import pytest

import stripe


TEST_RESOURCE_ID = "trr_123"


class TestPerson(object):
    def construct_resource(self):
        person_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "person",
            "account": "acct_123",
        }
        return stripe.Person.construct_from(person_dict, stripe.api_key)

    def test_has_instance_url(self):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/v1/accounts/acct_123/persons/%s" % TEST_RESOURCE_ID
        )

    def test_is_not_modifiable(self):
        with pytest.raises(NotImplementedError):
            stripe.Person.modify(TEST_RESOURCE_ID, first_name="John")

    def test_is_not_retrievable(self):
        with pytest.raises(NotImplementedError):
            stripe.Person.retrieve(TEST_RESOURCE_ID)

    def test_is_saveable(self, http_client_mock):
        resource = self.construct_resource()
        resource.first_name = "John"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_123/persons/%s" % TEST_RESOURCE_ID,
            post_data="first_name=John",
        )
