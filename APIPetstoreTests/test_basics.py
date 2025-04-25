import requests
import json

baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '2'

def test_get_pet_by_id():
    url = baseURI + petID
    resp = requests.get(url)
    data = resp.json()
    assert len(data) != 0, 'Response is empty'

def test_get_pet_by_id_check_id():
    url = baseURI + petID
    resp = requests.get(url)
    data = resp.json()
    assert data.get('id') == 2, 'Response is empty'