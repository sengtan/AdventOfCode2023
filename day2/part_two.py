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

    total = 0

    for d in data:
        split_data = d.split(":")
        game_data = split_data[0]
        round_data = split_data[1]

        # Remove the "Game " in "Game 1", to extract the game number
        game_num = int(game_data.replace("Game ", ""))

        cubes = {
            "red": [],
            "green": [],
            "blue": []
        }

        # Go through each round in the game
        for round in round_data.split(";"):
            # Go through each set in the round
            for sets in round.split(","):
                num = int(sets.split()[0])
                color = sets.split()[1]

                cubes[color].append(num)
            
        # After going through all the set, find the minimum number of each color
        red = 0 if len(cubes["red"]) == 0 else max(cubes["red"])
        green = 0 if len(cubes["green"]) == 0 else max(cubes["green"])
        blue = 0 if len(cubes["blue"]) == 0 else max(cubes["blue"])

        # If all colors are 0, then skip
        if (red + green + blue) == 0:
            continue

        # Otherwise, ensure all colors at least 1 to multiply
        red = 1 if red == 0 else red
        green = 1 if green == 0 else green
        blue = 1 if blue == 0 else blue

        total += (red*green*blue)
        
    print(f"Answer for Part 2: {total}")