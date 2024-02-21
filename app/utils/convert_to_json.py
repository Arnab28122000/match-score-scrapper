import re
import json

def convert_data_to_json(data):
    # Define regular expressions for extracting information
    team_info_pattern = re.compile(r'IPI÷(.*?)¬IPU÷(.*?)¬IPI÷(.*?)¬IPU÷(.*?)¬IPI÷(.*?)¬IPU÷(.*?)¬IPI÷(.*?)¬IPU÷(.*?)¬IPI÷(.*?)¬IPU÷(.*?)¬IPI÷(.*?)¬IPU÷(.*?)¬IPI÷(.*?)¬IPU÷(.*?)¬IPI÷(.*?)¬IPU÷(.*?)¬IPI÷(.*?)¬IPU÷(.*?)¬~TZ÷(.*?)¬TZS÷(.*?)¬~TA÷(.*?)¬TT÷(.*?)¬~TB÷(.*?)¬TC÷(.*?)¬~ETI÷(.*?)¬~TR÷(.*?)¬TU÷(.*?)¬TUC÷(.*?)¬TN÷(.*?)¬TI÷(.*?)¬TIU÷(.*?)¬TM÷(.*?)¬TW÷(.*?)¬TWR÷(.*?)¬TWO÷(.*?)¬TWP÷(.*?)¬TWA÷(.*?)¬TDR÷(.*?)¬TL÷(.*?)¬TLR÷(.*?)¬TLO÷(.*?)¬TLP÷(.*?)¬TLA÷(.*?)¬TAP÷(.*?)¬NRM÷(.*?)¬TPK÷(.*?)¬TPF÷(.*?)¬TG÷(.*?)¬PC÷(.*?)¬~LMS÷(.*?)¬LMU÷(.*?)¬LME÷(.*?)¬LMH÷(.*?)¬LMA÷(.*?)¬LMT÷(.*?)')

    match_info_pattern = re.compile(r'(\d+)¬~LMS÷(.*?)¬LMU÷(.*?)¬LME÷(.*?)¬LMH÷(.*?)¬LMA÷(.*?)¬LMT÷(.*?)')

    # Extract team information
    team_info_match = team_info_pattern.search(data)
    team_info = {
        "team_name": team_info_match.group(1),
        "team_image_url": team_info_match.group(2),
        "team_logo_url": team_info_match.group(3),
        "team_id": team_info_match.group(4),
        "player1_id": team_info_match.group(5),
        "player1_name": team_info_match.group(6),
        "player2_id": team_info_match.group(7),
        "player2_name": team_info_match.group(8),
        "player3_id": team_info_match.group(9),
        "player3_name": team_info_match.group(10),
        "player4_id": team_info_match.group(11),
        "player4_name": team_info_match.group(12),
        "player5_id": team_info_match.group(13),
        "player5_name": team_info_match.group(14),
        "team_country": team_info_match.group(15),
        "team_code": team_info_match.group(16),
        "team_abbr": team_info_match.group(17),
        # Add more team information fields as needed
    }

    # Extract standings information
    standings_info = {
        "standings_type": team_info_match.group(3),
        "standings_subtype": team_info_match.group(4),
    }

    # Extract upcoming matches
    upcoming_match_info = match_info_pattern.search(data)
    upcoming_matches = [
        {
            "timestamp": int(upcoming_match_info.group(1)),
            "status": upcoming_match_info.group(2),
            "result": upcoming_match_info.group(3),
            "event_id": upcoming_match_info.group(4),
            "home_team_id": upcoming_match_info.group(5),
            "away_team_id": upcoming_match_info.group(6),
            "result_details": upcoming_match_info.group(7),
        }
    ]

    # Add more logic to extract other match information
    # Extract more match information
    while match_info_pattern.search(data, upcoming_match_info.end()):
        upcoming_match_info = match_info_pattern.search(data, upcoming_match_info.end())
        upcoming_matches.append({
            "timestamp": int(upcoming_match_info.group(1)),
            "status": upcoming_match_info.group(2),
            "result": upcoming_match_info.group(3),
            "event_id": upcoming_match_info.group(4),
            "home_team_id": upcoming_match_info.group(5),
            "away_team_id": upcoming_match_info.group(6),
            "result_details": upcoming_match_info.group(7),
        })

    # Combine all information into a JSON structure
    result_json = {
        "team_info": team_info,
        "standings_info": standings_info,
        "upcoming_matches": upcoming_matches,
    }

    return json.dumps(result_json, indent=2)