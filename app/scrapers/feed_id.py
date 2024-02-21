

import json

from tqdm import tqdm
from app.scrapers.team_box_score import get_team_box_score
from app.scrapers.team_stats import get_team_stats
from app.utils.make_http_request import make_api_request
from app.utils.parse_feed_ids import extract_feed_ids


def feed_ids():
    api_url = 'https://global.flashscore.ninja/22/x/feed/f_1_0_11_en-au_1'

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
    'x-geoip': '1',
}
    # Make the API request and get the JSON data
    api_response = make_api_request(api_url, api_headers)

    feed_ids = extract_feed_ids(api_response)
    print("Feed_ids: ", feed_ids)

    # print("Feed_id: ", feed_ids)

    # data = []

    # try:
    #     with tqdm(total=len(feed_ids)) as pbar:
    #         for feed_id in feed_ids:
    #             box_score = get_team_box_score(feed_id)
    #             team_stats = get_team_stats(feed_id)
    #             ob = {
    #                 box_score: box_score,
    #                 team_stats: team_stats
    #             }
    #             data.append(ob)
    #             pbar.update(1)
            
    #         json_data = json.dumps(data, indent=2)

    #         # Save the JSON data to a file
    #         if json_data:
    #             file_path = "feed_data.txt"

    #         # Write the JSON string to a text file
    #             with open(file_path, "w") as file:
    #                 file.write(json_data)

    # except Exception as e:
    #     print("Feed Exception: ",e)

    