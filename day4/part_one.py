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
 
    # Pre-calculate the points, to not waste computational power
    match_points = {
        0: 0,
        1: 1,
        2: 2,
        3: 4,
        4: 8,
        5: 16,
        6: 32,
        7: 64,
        8: 128,
        9: 256,
        10: 512
    }

    total = 0

    for d in data:
        split_data = d.split(":")
        card_num = int(split_data[0].replace("Card ",""))

        split_numbers = split_data[1].split("|")
        winning_set = set(split_numbers[0].split())
        have_set = set(split_numbers[1].split())

        matches = len(winning_set) - len(winning_set - have_set)
        total += match_points[matches]
        
    print(f"Answer for Part 1: {total}")
