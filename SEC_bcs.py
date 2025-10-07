"""
Using PyCharm or another IDE of your choosing, implement a Python program that includes:

At least one of the five data types discussed in zyBook sections
3.1 through 3.5: strings, lists, tuples, sets, and dictionaries.
Whichever type(s) you choose to work with,
you must demonstrate code that manipulates data at the element level;
in the case of strings, this means working with the characters that comprise the string.
In other words, you should not work only with the list, set, string, tuple, or dictionary as a whole;
you should demonstrate at least one instance of working with an element within the container.
Conditional / branching logic as discussed in Chapter 4 of the zyBook.
Details beyond this are up to you. While not required, it is perfectly acceptable for this project
to expand upon the program that you developed for Project 1!

"""

sec_teams = {
    "Florida": {"wins": 2, "losses": 3, "sos": 1, "FPI": 26, "AVGWP": 67},
    "Alabama": {"wins": 4, "losses": 1, "sos": 3, "FPI": 3, "AVGWP": 39},
    "Kentucky": {"wins": 2, "losses": 3, "sos": 4, "FPI": 50, "AVGWP": 86},
    "Arkansas": {"wins": 2, "losses": 3, "sos": 5, "FPI": 41, "AVGWP": 69},
    "Auburn": {"wins": 3, "losses": 2, "sos": 7, "FPI": 23, "AVGWP": 61},
    "Georgia": {"wins": 4, "losses": 1, "sos": 11, "FPI": 6, "AVGWP": 30},
    "Texas": {"wins": 3, "losses": 2, "sos": 16, "FPI": 8, "AVGWP": 55},
    "Lsu": {"wins": 4, "losses": 1, "sos": 17, "FPI": 17, "AVGWP": 43},
    "Texas A&M": {"wins": 5, "losses": 0, "sos": 18, "FPI": 13, "AVGWP": 19},
    "South Carolina": {"wins": 3, "losses": 2, "sos": 25, "FPI": 29, "AVGWP": 59},
    "Vanderbilt": {"wins": 5, "losses": 1, "sos": 28, "FPI": 16, "AVGWP": 28},
    "Mississippi State": {"wins": 4, "losses": 2, "sos": 30, "FPI": 45, "AVGWP": 35},
    "Ole Miss": {"wins": 5, "losses": 0, "sos": 44, "FPI": 7, "AVGWP": 12},
    "Tennessee": {"wins": 4, "losses": 1, "sos": 45, "FPI": 11, "AVGWP": 11},
    "Oklahoma": {"wins": 5, "losses": 0, "sos": 64, "FPI": 15, "AVGWP": 4},
    "Missouri": {"wins": 5, "losses": 0, "sos": 109, "FPI": 18, "AVGWP": 8},
}
"""
SOS:Rank among all FBS teams of games already played schedule strength,
            from perspective of an average Top 25 team.

AVGWP:Team's average in-game win probability rank adjusted for chance that an average FBS team would
            control games from start to end the way this team did, given the schedule.

FPI:Football Power Index Rank vs all FBS teams.
"""


def evalute_teams(wins, losses, sos, fpi, avgwp):
    """Calculates team score based on weighted metrics."""
    win_pct = wins / (wins + losses)
    sos_score = (130 - sos) / 130
    fpi_score = (130 - fpi) / 130
    avgwp_score = (100 - avgwp) / 100
    score = (
        (win_pct * 0.25)
        + (sos_score * 0.30)
        + (fpi_score * 0.25)
        + (avgwp_score * 0.20)
    )
    return score


def get_team_details(team_name):
    """Displays detailed statistics for a specific team."""
    # Element-level string manipulation: capitalize each word
    team_name_formatted = team_name.title()

    # Conditional logic: check if team exists
    if team_name_formatted in sec_teams:
        stats = sec_teams[team_name_formatted]
        print(f"\n--- {team_name_formatted} Detailed Stats ---")
        print(f"Record: {stats['wins']}-{stats['losses']}")
        print(
            f"Win Percentage: {stats['wins'] / (stats['wins'] + stats['losses']) * 100:.1f}%"
        )
        print(f"Strength of Schedule Rank: {stats['sos']}")
        print(f"FPI Rank: {stats['FPI']}")
        print(f"Average Win Probability: {stats['AVGWP']}")

        # Conditional logic: performance evaluation
        win_pct = stats["wins"] / (stats["wins"] + stats["losses"])
        if win_pct >= 0.75:
            print("Status: Elite Performance")
        elif win_pct >= 0.60:
            print("Status: Strong Performance")
        elif win_pct >= 0.50:
            print("Status: Average Performance")
        else:
            print("Status: Struggling")

        # Conditional logic: strength of schedule assessment
        if stats["sos"] <= 10:
            print("Schedule Difficulty: BRUTAL")
        elif stats["sos"] <= 30:
            print("Schedule Difficulty: Tough")
        elif stats["sos"] <= 60:
            print("Schedule Difficulty: Moderate")
        else:
            print("Schedule Difficulty: Easy")
    else:
        print(f"\nTeam '{team_name_formatted}' not found in SEC rankings.")


team_rankings = {}

for team, stats in sec_teams.items():
    team_rankings[team] = evalute_teams(
        stats["wins"], stats["losses"], stats["sos"], stats["FPI"], stats["AVGWP"]
    )

sorted_teams = sorted(team_rankings.items(), key=lambda x: x[1], reverse=True)

print("Sec BCS Rankings")

for rank, (team, score) in enumerate(sorted_teams, start=1):
    print(f"{rank}.{team:18}| BCS Score: {score:.3f}")


user_input = input("\nWould you like to view detailed stats for a team? (yes/no): ")

if user_input.lower() == "yes" or user_input.lower() == "y":
    team_name = input("Enter team name: ")
    get_team_details(team_name)
else:
    print("Thank You, We Hope You Enjoy Your Day!")
