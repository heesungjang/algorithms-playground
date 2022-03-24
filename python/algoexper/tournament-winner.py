import collections
from typing import List

input1 = [["HTML", "C#"],
          ["C#", "Python"],
          ["Python", "HTML"]]

input2 = [0, 0, 1]


def tournament_winner(competitions: List[List[str]], results: List[int]) -> str:
    map = collections.defaultdict(list)

    for idx, match in enumerate(competitions):
        # away team won [home_team, away_team]
        if results[idx] == 0:
            map[match[1]].append(True)
        # home team won
        else:
            map[match[0]].append(True)
    return max(map, key=lambda x: len(map[x]))


print(tournament_winner(input1, input2))
