import requests

# url = "http://localhost:8000/api/users_list/"

# response = requests.get(url)
# print(response.text)

#Get Authentication token 
 
url = "http://localhost:8000/auth/token/login"
response = requests.post(url,data = {"username":"raka","password":"tech"})
print(response.text)
