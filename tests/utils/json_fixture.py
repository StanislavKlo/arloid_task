class JSONFixture:

    @staticmethod
    def for_create_pet_all_fields(entityId, name, status="available"):
        json = {
            "id": entityId,
            "name": name,
            "category": {
                "id": 1,
                "name": ""
            },
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": status
        }
        return json

    # This is bad example, we need to pass some object as method parameter. Didn't have time to elaborate on this.
    # Moreover, json object should be a py object with appropriate fields
    @staticmethod
    def for_create_order_for_pet(requestId, petId, quantity, shipDate, status):
        json = {
            "id": requestId,
            "petId": petId,
            "quantity": quantity,
            "shipDate": shipDate,
            "status": status,
            "complete": True
        }
        return json
