import requests

from app.utils.convert_to_json import convert_data_to_json


def make_api_request(url, headers):

    # Make the HTTP request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert the response text to JSON
        data = response.text
        return data
    else:
        print(f'Request failed with status code {response.status_code}')
        return None