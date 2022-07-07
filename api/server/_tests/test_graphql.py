import pytest
import requests
from _tests.queries import food_categories

SERVER_URL = {
    "localhost": "http://127.0.0.1:8080/api/graphql/",
}


def test_food_categories(server_type):
    all_categories = requests.get(SERVER_URL[server_type], json={"query": food_categories})
    query_data = all_categories.json().get('data')
    assert query_data is not None


