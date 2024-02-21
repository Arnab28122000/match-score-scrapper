import re

def parse_box_score(data):
   # Extracting relevant information using regular expressions
    teams = {}
    current_team = None

    lines = data.split('~')

    for line in lines:
        line = line.strip()

        if line.startswith('PA÷'):
            current_team = line[3:]
            teams[current_team] = []
        elif line.startswith('PJ÷'):
            player_info = re.findall(r'(\w{2})÷([^¬]+)', line)
            player_dict = {key: value for key, value in player_info}
            teams[current_team].append(player_dict)

    return teams