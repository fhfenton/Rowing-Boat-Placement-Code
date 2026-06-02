# Rowing Boat Placement App
# This program recommends a rowing boat based on athlete stats.

def time_to_seconds(time_text):
    """Converts a 2K time like 7:15 into seconds."""
    minutes, seconds = time_text.split(":")
    return int(minutes) * 60 + int(seconds)


def calculate_rower_score(two_k_seconds, height, form, weight):
    """Calculates a total rower score using 2K, height, form, and weight."""
    score = 0

    # Selection based on 2K speed
    if two_k_seconds <= 390:
        score += 40
    elif two_k_seconds <= 420:
        score += 32
    elif two_k_seconds <= 450:
        score += 24
    else:
        score += 15

    # Selection based on height
    if height >= 74:
        score += 20
    elif height >= 70:
        score += 15
    else:
        score += 10

    # Form rating
    score += form * 3

    # Weight range
    if 140 <= weight <= 220:
        score += 10
    else:
        score += 5

    return score


def choose_boat(score):
    """Chooses the boat based on final score."""
    if score >= 90:
        return "Varsity 1 Boat"
    elif score >= 75:
        return "Varsity 2 Boat"
    elif score >= 60:
        return "JV Boat"
    else:
        return "Novice/Development Boat"


def get_rowers():
    """Gets multiple rowers from the user using a loop."""
    rowers = []

    number = int(input("How many rowers are you entering? "))

    for i in range(number):
        print("\nRower", i + 1)

        name = input("Name: ")
        two_k = input("2K time (example 7:15): ")
        height = int(input("Height in inches: "))
        form = int(input("Form rating 1-10: "))
        weight = int(input("Weight in pounds: "))

        seconds = time_to_seconds(two_k)
        score = calculate_rower_score(seconds, height, form, weight)
        boat = choose_boat(score)

        rowers.append([name, score, boat])

    return rowers


def display_results(rowers):
    """Displays final boat placements."""
    print("\n--- Boat Placement Results ---")

    for rower in rowers:
        print(rower[0], "- Score:", rower[1], "- Placement:", rower[2])


# Main program
rower_list = get_rowers()
display_results(rower_list)