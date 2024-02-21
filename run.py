from app.scrapers.basketball import basketball_data
from app.scrapers.feed_id import feed_ids
from app.scrapers.team_box_score import get_team_box_score
from app.scrapers.team_stats import get_team_stats
from app.utils.generate_sha_256 import generate_checksum



if __name__ == "__main__":
    # feed_ids()

    # Example usage:
#     payload = {
#   "merchantId": "M1GF4OPVGZBN",
#   "merchantTransactionId": "MT7850590068188100",
#   "merchantUserId": "MUID100",
#   "amount": 200,
#   "redirectUrl": "https://webhook.site/redirect-url",
#   "redirectMode": "REDIRECT",
#   "callbackUrl": "https://webhook.site/callback-url",
#   "mobileNumber": "9083972802",
#   "paymentInstrument": {
#     "type": "PAY_PAGE"
#   }
# }
#     salt_key = "c149c785-77e6-4ff9-b270-5b64d183f900"
#     salt_index = 1  # Replace with your actual salt index

#     result = generate_checksum(payload, 'pay', salt_key, salt_index)
#     generate_checksum(payload, endpoint, salt_key, salt_index):
#     print(result)
    # print(generate_uuid())

    json_data = get_team_box_score("CW350B68")
    if json_data:
        file_path = "feed_data.txt"

            # Write the JSON string to a text file
        with open(file_path, "w") as file:
            file.write(json_data)

    get_team_stats()