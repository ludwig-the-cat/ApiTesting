from utils.myutils import *
from utils.confparser import *

#baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '1'
baseURI = getPetAPIURL()

def test_getPetByID_response():
    url = baseURI + petID
    print(url)
    data, status, time_taken = getAPIData(url)
    assert data.get('id') == int(petID), 'Wrong'
    assert status == 200, 'Wrong'

# обновляем данные по pet
def test_updatePet():
    payload = {"id": int(petID),"category":{"id":0,"name":"string"},"name":"Zelda","photoUrls":["string"],"tags":[{"id":0,"name":"string"}],"status":"pending"}
    data, status, time_taken = putData(baseURI, payload)
    assert data.get('id') == int(petID)
    assert data.get('name') == 'Zelda'
    assert status == 200