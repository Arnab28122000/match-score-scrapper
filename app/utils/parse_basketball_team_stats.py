import re

def parse_team_stats(data):
   # Extracting relevant information using regular expressions
    pattern = re.compile(r'SG÷(\w+(?: \w+)?).*?SH÷(\d+)¬SI÷(\d+).*?SH÷(\d+)¬SI÷(\d+)')
    matches = pattern.findall(data)
    stat_mapping = {
    "Field Goals": "FG",
    "Field Goals %": "Field Goal %",
    "2-Point Field G.": "2PT",
    "2-Point Field Goals %": "Two Point %",
    "3-Point Field G.": "3PT",
    "3-Point Field Goals %": "Three Point %",
    "Free Throws": "FT",
    "Free Throws %": "Free Throw %",
}

# Creating the JSON structure
    team_stats = []
    for match in matches:
        stat, away_attempted, away_made, home_attempted, home_made = match
        stat_key = stat_mapping.get(stat, stat)
        
        team_stat = {
            "stat": stat_key,
            "away_team": f"{away_made}-{away_attempted}",
            "home_team": f"{home_made}-{home_attempted}"
        }
        team_stats.append(team_stat)

    return {"team_stats": team_stats}