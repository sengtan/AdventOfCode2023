def get_data(file:str = 'data.txt'):
    try:
        with open(file, 'r') as f:
            data = f.readlines()
            return data
    except Exception as e:
        print(e)
    else:
        return None

if __name__ == "__main__":
    data = get_data()

    limit = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    total = 0

    for d in data:
        possible = True
        split_data = d.split(":")
        game_data = split_data[0]
        round_data = split_data[1]

        # Remove the "Game " in "Game 1", to extract the game number
        game_num = int(game_data.replace("Game ", ""))

        # Go through each round in the game
        for round in round_data.split(";"):
            cubes = {
                "red": 0,
                "green": 0,
                "blue": 0
            }

            # Go through each set in the round
            for sets in round.split(","):
                num = int(sets.split()[0])
                color = sets.split()[1]

                # If any color exceeds the expected limit, its impossible
                if num > limit[color]:
                    possible = False

        if possible:
            total += game_num

    print(f"Answer for Part 1: {total}")