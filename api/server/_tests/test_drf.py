import requests

SERVER_URL = {
    "localhost": "http://127.0.0.1:8080/api/v1/foods/",
}


def test_food_categories(server_type):
    response = requests.get(SERVER_URL[server_type])
    assert response.status_code is 200
    assert response.json() is not None
