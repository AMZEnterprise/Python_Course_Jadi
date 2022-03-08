team_and_results = []

iran_dict = {'team': 'Iran', 'wins': 0, 'draws': 0,
             'losses': 0, 'goals': 0, 'goals_against': 0, 'goals_difference': 0, 'points': 0}
spain_dict = {'team': 'Spain', 'wins': 0, 'draws': 0,
              'losses': 0, 'goals': 0, 'goals_against': 0, 'goals_difference': 0, 'points': 0}
portugal_dict = {'team': 'Portugal', 'wins': 0, 'draws': 0,
                 'losses': 0, 'goals': 0, 'goals_against': 0, 'goals_difference': 0, 'points': 0}
morocco_dict = {'team': 'Morocco', 'wins': 0, 'draws': 0,
                'losses': 0, 'goals': 0, 'goals_against': 0, 'goals_difference': 0, 'points': 0}

for i in range(0, 6):
    match_results = list(map(int, input().split("-")))

    if i == 0:
        iran_dict["goals"] += match_results[0]
        iran_dict["goals_against"] += match_results[1]

        spain_dict["goals"] += match_results[1]
        spain_dict["goals_against"] += match_results[0]

        if match_results[0] > match_results[1]:
            iran_dict["wins"] += 1
            spain_dict["losses"] += 1

        elif match_results[0] < match_results[1]:
            iran_dict["losses"] += 1
            spain_dict["wins"] += 1

        else:
            iran_dict["draws"] += 1
            spain_dict["draws"] += 1

    if i == 1:
        iran_dict["goals"] += match_results[0]
        iran_dict["goals_against"] += match_results[1]

        portugal_dict["goals"] += match_results[1]
        portugal_dict["goals_against"] += match_results[0]

        if match_results[0] > match_results[1]:
            iran_dict["wins"] += 1
            portugal_dict["losses"] += 1

        elif match_results[0] < match_results[1]:
            iran_dict["losses"] += 1
            portugal_dict["wins"] += 1

        else:
            iran_dict["draws"] += 1
            portugal_dict["draws"] += 1

    if i == 2:
        iran_dict["goals"] += match_results[0]
        iran_dict["goals_against"] += match_results[1]

        morocco_dict["goals"] += match_results[1]
        morocco_dict["goals_against"] += match_results[0]

        if match_results[0] > match_results[1]:
            iran_dict["wins"] += 1
            morocco_dict["losses"] += 1

        elif match_results[0] < match_results[1]:
            iran_dict["losses"] += 1
            morocco_dict["wins"] += 1

        else:
            iran_dict["draws"] += 1
            morocco_dict["draws"] += 1

    if i == 3:
        spain_dict["goals"] += match_results[0]
        spain_dict["goals_against"] += match_results[1]

        portugal_dict["goals"] += match_results[1]
        portugal_dict["goals_against"] += match_results[0]

        if match_results[0] > match_results[1]:
            spain_dict["wins"] += 1
            portugal_dict["losses"] += 1

        elif match_results[0] < match_results[1]:
            spain_dict["losses"] += 1
            portugal_dict["wins"] += 1

        else:
            spain_dict["draws"] += 1
            portugal_dict["draws"] += 1

    if i == 4:
        spain_dict["goals"] += match_results[0]
        spain_dict["goals_against"] += match_results[1]

        morocco_dict["goals"] += match_results[1]
        morocco_dict["goals_against"] += match_results[0]

        if match_results[0] > match_results[1]:
            spain_dict["wins"] += 1
            morocco_dict["losses"] += 1

        elif match_results[0] < match_results[1]:
            spain_dict["losses"] += 1
            morocco_dict["wins"] += 1

        else:
            spain_dict["draws"] += 1
            morocco_dict["draws"] += 1

    if i == 5:
        portugal_dict["goals"] += match_results[0]
        portugal_dict["goals_against"] += match_results[1]

        morocco_dict["goals"] += match_results[1]
        morocco_dict["goals_against"] += match_results[0]

        if match_results[0] > match_results[1]:
            portugal_dict["wins"] += 1
            morocco_dict["losses"] += 1

        elif match_results[0] < match_results[1]:
            portugal_dict["losses"] += 1
            morocco_dict["wins"] += 1

        else:
            portugal_dict["draws"] += 1
            morocco_dict["draws"] += 1


def get_complete_dict():
    result_dict = {}

    result_dict["Iran"] = iran_dict
    result_dict["Spain"] = spain_dict
    result_dict["Portugal"] = portugal_dict
    result_dict["Morocco"] = morocco_dict

    return result_dict


def calc_goal_difference(list_of_dicts):
    for key, value in list_of_dicts.items():
        value["goals_difference"] = value["goals"] - value["goals_against"]


def calc_points(list_of_dicts):
    for key, value in list_of_dicts.items():
        value["points"] = 3 * value["wins"] + value["draws"]


def sort_result_dict(result_dict):
    return sorted(result_dict.items(), key=lambda x: (-x[1]["points"], x[1]["wins"], x[1]["team"]))


def print_result_list(list):
    for i in list:
        print(f"{i[0]} wins:{i[1]['wins']} , loses:{i[1]['losses']} , draws:{i[1]['draws']} , goal difference:{i[1]['goals_difference']} , points:{i[1]['points']}")


complete_dict = get_complete_dict()
calc_goal_difference(complete_dict)
calc_points(complete_dict)
print_result_list(sort_result_dict(complete_dict))
