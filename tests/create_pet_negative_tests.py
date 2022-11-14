import pytest
from tests.utils.api import Api


class TestCreatePetNegative:

    @pytest.mark.api
    def test_create_pet_id_is_not_int(self):
        result = Api.create_pet("test", "myPet")

        # Validate new pet is created
        assert 400 == result.status_code
        response_json = result.json()
        assert response_json["message"] == "Input error: unable to convert input to io.swagger.petstore.model.Pet"

    # this test fails, because API work incorrect
    @pytest.mark.api
    def test_create_pet_invalid_status(self):
        result = Api.create_pet(1, "myPet", "invalid_status")

        # Validate new pet is created
        assert 400 == result.status_code
        response_json = result.json()
        assert response_json["message"] == "Status is invalid"
