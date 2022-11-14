import configparser
import logging

from allure_commons._allure import step
from tests.utils.http_manager import HttpManager
from tests.utils.json_fixture import JSONFixture


class Api:
    LOGGER = logging.getLogger(__name__)
    parser = configparser.ConfigParser()
    parser.read('simple_config.ini')

    BASE_URL = "https://petstore3.swagger.io/api/v3"
    CREATE_PET = BASE_URL + "/pet"
    DELETE_PET = BASE_URL + "/pet/{0}"
    CREATE_ORDER = BASE_URL + "/store/order"

    @staticmethod
    def create_pet(entityId, name, status="available"):
        with step("Create pet"):
            result = HttpManager.post(Api.CREATE_PET,
                                      JSONFixture.for_create_pet_all_fields(entityId, name, status))
            Api.LOGGER.info('TEST: Create pet. Method: {0}, Data: {1}'.format("POST",
                                                                              JSONFixture.for_create_pet_all_fields(
                                                                                  entityId,
                                                                                  name, status)))
            return result

    @staticmethod
    def delete_pet(pet_id):
        with step("Delete pet by ID"):
            result = HttpManager.delete(Api.DELETE_PET.format(pet_id))
            Api.LOGGER.info(
                'TEST: Delete pet. Method: {0}, URL : {1}'.format("DELETE", Api.DELETE_PET.format(pet_id)))
            return result

    @staticmethod
    def get_pet(pet_id):
        with step("Get pet by ID"):
            result = HttpManager.get(Api.DELETE_PET.format(pet_id))
            Api.LOGGER.info(
                'TEST: Get pet. Method: {0}, URL : {1}'.format("GET", Api.DELETE_PET.format(pet_id)))
            return result

    @staticmethod
    def create_order(requestId, petId, quantity, shipDate, status):
            with step("Create order"):
                result = HttpManager.post(Api.CREATE_ORDER,
                                          JSONFixture.for_create_order_for_pet(requestId, petId, quantity, shipDate, status))
                Api.LOGGER.info('TEST: Create pet. Method: {0}, Data: {1}'.format("POST",
                    JSONFixture.for_create_order_for_pet(requestId, petId, quantity, shipDate, status)))
                return result
