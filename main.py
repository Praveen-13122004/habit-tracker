import requests
import json
pixela_end="https://pixe.la/v1/users"
user_parameter = {
    "token":"oij45pijqkne89wqi",
    "username":"praveensakthivel",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
response=requests.post(url=pixela_end,json=user_parameter)
print(response.text)