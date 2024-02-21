import json

from app.utils.make_http_request import make_api_request
from app.utils.parse_basket_ball_box_score import parse_box_score


def get_team_box_score(feed_id):
    try:
        api_url = f"https://global.flashscore.ninja/22/x/feed/df_sur_1_{feed_id}"

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
        data_dict = parse_box_score(api_response)
        # Iterate through each key and value pair
        for key, value in data_dict.items():
            # Remove "\u00ac" from the key
            data_dict[key.replace("\u00ac", "")] = data_dict.pop(key)

            # Separate the "PC" value into a list for each item
            for item in data_dict[key.replace("\u00ac", "")]:
                pc_values = item["PC"].split('|')
                item["PC"] = {
                    "field_goals_made": pc_values[0],
                    "field_goals_attempted": pc_values[1],
                    "2-point_made": pc_values[2],
                    "2-point_attempted": pc_values[3],
                    "3-point_made": pc_values[4],
                    "3-point_attempted": pc_values[5],
                    "free_throws_made": pc_values[6],
                    "free_throws_attempted": pc_values[7],
                    "plus_minus": pc_values[8],
                    "offensive_rebounds": pc_values[9],
                    "defensive_rebounds": pc_values[10],
                    "personal_fouls": pc_values[11],
                    "steals": pc_values[12],
                    "turnovers": pc_values[13],
                    "blocked_shots": pc_values[14],
                    "blocks_against": pc_values[15],
                    "technical_fouls": pc_values[16],
                }
        json_data = json.dumps(data_dict, indent=2)

        return json_data

    except Exception as e:
        print("Box Score Exception: ", e)
    # if json_data:
    #     file_path = "box_score.txt"

    #     with open(file_path, "w") as file:
    #         file.write(json_data)

        # print(f"JSON data has been saved to {file_path}")
