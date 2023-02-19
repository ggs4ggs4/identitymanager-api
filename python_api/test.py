import requests
api_url = 'https://api.api-ninjas.com/v1/imagetotext'

image_file_descriptor = open('aadhar1.jpg', 'rb')
files = {'image': image_file_descriptor}
r = requests.post(api_url, files=files)
print(r.json())