import requests

# get
def getAPIData(url):
    response = requests.get(url)
    data = response.json()
    assert len(data) != 0, 'empty response'
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken

# put
def putData(url, body):
    response = requests.post(url, json=body)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken

def deleteData(url, opHeader=None):
    header = opHeader if isinstance(opHeader, dict) else ''
    response = requests.delete(url)
    print(response.headers)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken

