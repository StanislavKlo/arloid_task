import pytest
import random
from requests import Response
from tests.utils.api import Api


class TestIssueRefactored:

    # Just example, here we can apply some preconditions
    @staticmethod
    def setup():
        assert 1 == 1

    # Just example, here we can remove some garbage
    @staticmethod
    def teardown():
        assert 1 == 1

    @pytest.mark.api
    def test_create_pet_and_order(self):
        petId = random.randint(1, 1000)
        result: Response = Api.create_pet(petId, "myPet")

        # Validate new pet is created
        assert 200 == result.status_code
        response_json = result.json()
        assert response_json["name"] == "myPet"
        assert response_json["id"] == petId

        # Validate order can be created for a newly created pet
        orderResponse = Api.create_order(10, petId, 7, "2022-11-16T11:43:23.869+00:00", "approved")
        order_json = orderResponse.json()
        assert 200 == orderResponse.status_code
        assert order_json["id"] == 10
        assert order_json["petId"] == petId
        assert order_json["quantity"] == 7
        assert order_json["shipDate"] == "2022-11-16T11:43:23.869+00:00"
        assert order_json["status"] == "approved"
        assert order_json["complete"] is True

        # Good, if we can delete all garbage afterwards
        pet_id = response_json["id"]
        result = Api.delete_pet(pet_id)
        assert 200 == result.status_code
