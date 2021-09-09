import requests
import json
from numpy import nan 
# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://80f17d6e-45f2-4949-9628-7bc4ecfae855.westeurope.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'gBNePnVukJOwOYQLxf9UezuQnLXrGu5B'
# A set of data to score, so we get one results back
data = {"data":
        [{'city': 'city_103',
  'city_development_index': 0.92,
  'gender': nan,
  'relevent_experience': 'Has relevent experience',
  'enrolled_university': 'no_enrollment',
  'education_level': 'Graduate',
  'major_discipline': 'STEM',
  'experience': '>20',
  'company_size': '10/49',
  'company_type': 'Pvt Ltd',
  'last_new_job': '>4',
  'training_hours': 140}]
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)
# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'
# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())