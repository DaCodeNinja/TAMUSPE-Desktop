import requests

WORKER_URL = "https://d1-tamuspe-users.llamas09-mango4089.workers.dev/"


def send(auth_key, user_id, app_version, os, date):

    headers = {'Auth-Key': auth_key, 'UID': user_id, 
               'Version': app_version, 'OS': os, 'DateFirstOpened': date}
    
    response = requests.get(WORKER_URL, headers=headers)

    if response.status_code == 200:
        # Assuming the response contains the file content
        print(f"Response: {response.content.decode('utf-8')}")
        return
    else:
        print(f"Status code: {response.status_code}")
        print(response.content.decode('utf-8'))
        return 'error'
