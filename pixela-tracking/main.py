import requests
from datetime import  datetime
TOKEN = "ComeOn2007"
USER_NAME = "emiliocliff54"
TODAY = datetime.now().strftime("%Y%m%d")
HEADER = {
    "X-USER-TOKEN": TOKEN
}
creating_user_endpoint = "https://pixe.la/v1/users"
creating_user_parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url="https://pixe.la/v1/users", json=creating_user_parameters)
# print(response.text)
create_graph_endpoint = f"https://pixe.la//v1/users/{USER_NAME}/graphs"
create_graph_params = {
    "id": "mygraph1",
    "name": "Habit",
    "unit": "commit",
    "type": "int",
    "color": "momiji"
}
# response = requests.post(url=create_graph_endpoint, headers=HEADER, json=create_graph_params)
# print(response.text)
update_graph_endpoint = f"https://pixe.la//v1/users/{USER_NAME}/graphs/{create_graph_params['id']}"
update_graph_params = {
    "name": f"{create_graph_params['name']}",
    "unit": "commit"
}
# response = requests.put(url=update_graph_endpoint, headers=HEADER, json=update_graph_params)
# print(response.text)
post_pixel_endpoint = f"https://pixe.la//v1/users/{USER_NAME}/graphs/{create_graph_params['id']}"
post_pixel_params = {
    "date": f"{TODAY}",
    # "date": "20230910",
    "quantity": "4"
}
response = requests.post(url=post_pixel_endpoint, headers=HEADER, json=post_pixel_params)
print(response.text)
delete_graph_endpoint = f"https://pixe.la//v1/users/{USER_NAME}/graphs/{create_graph_params['id']}"
# response = requests.delete(url=delete_graph_endpoint, headers=HEADER)
# print(response.text)