import random

def player(prev_play, opponent_history=[]):
    # Save opponent moves
    if prev_play != "":
        opponent_history.append(prev_play)

    # First few moves → random
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    # Store patterns
    if not hasattr(player, "patterns"):
        player.patterns = {}

    # Last 3 moves pattern
    pattern = "".join(opponent_history[-3:])

    if pattern in player.patterns:
        player.patterns[pattern] += 1
    else:
        player.patterns[pattern] = 1

    # Predict based on last 2 moves
    last_two = "".join(opponent_history[-2:])
    possible_patterns = []

    for key in player.patterns:
        if key.startswith(last_two):
            possible_patterns.append((key, player.patterns[key]))

    if possible_patterns:
        prediction = max(possible_patterns, key=lambda x: x[1])[0][-1]
    else:
        prediction = random.choice(["R", "P", "S"])

    # Counter move
    counter = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    return counter[prediction]