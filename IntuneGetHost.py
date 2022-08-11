import requests

def get_token():
    body = {
        "resource": "https://api.manage.microsoft.com/",
        "client_id": azure_appId,
        "client_secret": azure_appSecret,
        "grant_type": "client_credentials"
    }
    response = requests.post("https://login.windows.net/" + azure_tenantId + "/oauth2/token", data=body)
    return response.json()["access_token"]
    
    def get_devices(auth_token):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': "Bearer " + auth_token
    }
    skip = 0
    top = 1000
    results = list()
    processing_machines_continue = True
    while processing_machines_continue:
        url = "https://XXXX.manage.microsoft.com/ReportingService/DataWarehouseFEService/devices?api-version=v1.0&$skip= " + str(
            skip) + " &$top=" + str(top)
        response = requests.get(url, headers=headers)
        if response.json()['value'] != list():
            results += response.json()['value']
            skip += top
        else:
            processing_machines_continue = False
    return results
