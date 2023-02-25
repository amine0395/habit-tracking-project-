import requests
from datetime import *
TOKEN=#Ur_token a.k.a a password u've choosen
USERNAME=#ur_username
pixela_endpoint="https://pixe.la/v1/users"
user_param = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}
#response=requests.post(url=pixela_endpoint, json=user_param)
#print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":"graph1",
    "name":"sleep graph",
    "unit":"hour",
    "type":"float",
    "color":"ichou"
}
headers={
    "X-USER-TOKEN": TOKEN

}

#response=requests.post(url=graph_endpoint, json=graph_config,headers=headers)
#print(response.text)
pixel_creation=f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_data= {
    "date": str(datetime.now().strftime("%Y%m%d")),
    "quantity": "8",
}

#requests.post(url=pixel_creation, json=pixel_data,headers=headers)