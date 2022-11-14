import pytest
from tests.utils.api import Api
import random


class TestGetPetNegative:

    @pytest.mark.api
    def test_get_pet_by_id_given_non_existing_id(self):
        result = Api.get_pet(random.randint(14523, 45436))

        assert 404 == result.status_code
        assert result.text == "Pet not found"

    @pytest.mark.api
    def test_get_pet_which_was_deleted(self):
        petId = random.randint(100, 150)

        # create pet to delete
        Api.create_pet(petId, "newPet")

        # delete pet
        Api.delete_pet(petId)

        # get deleted pet and validate it's not found
        result = Api.get_pet(petId)
        assert 404 == result.status_code
        assert result.text == "Pet not found"



