import json

from app.utils.make_http_request import make_api_request
from app.utils.parse_basketball_team_stats import parse_team_stats


def get_team_stats(feed_id):
    try:
        api_url = f"https://global.flashscore.ninja/22/x/feed/df_st_1_{feed_id}"

        api_headers = {
        'authority': 'global.flashscore.ninja',
        'accept': '*/*',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,mr;q=0.6',
        'origin': 'https://www.flashscore.com.au',
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
        # print("API response: ", api_response)
        data_dict = parse_team_stats(api_response)
        
        json_data = json.dumps(data_dict, indent=2)

        return json_data
    except Exception as e:
        print("Exception in team stats: ", e)

    # Save the JSON data to a file
    # if json_data:
    #     file_path = "team_stats.txt"
        
    #     with open(file_path, "w") as file:
    #         file.write(json_data)

        # print(f"JSON data has been saved to {file_path}")
