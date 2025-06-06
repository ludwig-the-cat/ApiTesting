import requests
import pytest

baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '1'

@pytest.mark.skip
def test_get_pet_by_id():
    url = baseURI + petID
    resp = requests.get(url)
    data = resp.json()
    assert len(data) != 0, 'Response is empty'

@pytest.mark.skip
def test_get_pet_by_id_check_id():
    url = baseURI + petID
    resp = requests.get(url)
    data = resp.json()
    assert data.get('id') == 1, 'ID is wrong'

@pytest.mark.skip
def test_add_new_pet():
    url = baseURI
    body = {
  "id": 191,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Cuttie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
    }
    resp = requests.post(url=url, json=body)
    data = resp.json()
    assert data.get('id') == 191, 'ID is wrong'
    assert len(data) != 0, 'Response is empty'
