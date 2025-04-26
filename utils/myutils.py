import requests

def getAPIData(url):
    response = requests.get(url)
    data = response.json()
    assert len(data) != 0, 'empty response'
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken
