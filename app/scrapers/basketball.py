from app.utils.convert_to_json import convert_data_to_json

from app.utils.make_http_request import make_api_request


def basketball_data():
    api_url = 'https://global.flashscore.ninja/22/x/feed/to_SKoyDpU8_YZEnCJej_1'

    api_headers = {
    'authority': 'global.flashscore.ninja',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,mr;q=0.6',
    'cache-control': 'no-cache',
    'origin': 'https://www.flashscore.com.au',
    'pragma': 'no-cache',
    'referer': 'https://www.flashscore.com.au/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
    'x-fsign': 'SW9D1eZo',
}

    # Make the API request and get the JSON data
    api_response = make_api_request(api_url, api_headers)
    json_data = convert_data_to_json(api_response)

    # Save the JSON data to a file
    if json_data:
        file_path = "output.txt"

        # Write the JSON string to a text file
        with open(file_path, "w") as file:
            file.write(json_data)

        print(f"JSON data has been saved to {file_path}")
        # with open('output.json', 'w') as json_file:
        #     json.dump(api_response, json_file, indent=2)

        print('Data successfully saved to output.json')
