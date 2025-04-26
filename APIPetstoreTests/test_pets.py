from utils.myutils import getAPIData

baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '1'

def test_getPetByID_response():
    url = baseURI + petID
    print(url)
    data, status, time_taken = getAPIData(url)
    assert data.get('id') == int(petID), 'Wrong'
    assert status == 200, 'Wrong'
