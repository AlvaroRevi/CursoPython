import requests
import datetime


USERNAME = "revi2"
TOKEN = "aaa3333aaa"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "username": USERNAME,
    "token": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

today = datetime.datetime.now()
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "My first graph",
    "unit": "Kg",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_config = {
    "quantity": "15",
}

response = requests.put(url=update_endpoint, json=new_pixel_config, headers=headers)
print(response.text)