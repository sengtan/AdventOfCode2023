def get_data(file:str = 'data.txt'):
    try:
        with open(file, 'r') as f:
            data = f.readlines()
            return data
    except Exception as e:
        print(e)
    else:
        return None

# Check if dictionary contains the key, initialize it as 0 if not, then add in value
def add_copies(copies: dict, key: int, val: int):
    if key not in copies.keys():
        copies[key] = 0
    copies[key] += val

if __name__ == "__main__":
    data = get_data()
 
    # Tracks number of copies of each card
    copies = {}
    total = 0

    for d in data:
        split_data = d.split(":")
        card_num = int(split_data[0].replace("Card ",""))

        split_numbers = split_data[1].split("|")
        winning_set = set(split_numbers[0].split())
        have_set = set(split_numbers[1].split())

        # Check how many number matches
        matches = len(winning_set) - len(winning_set - have_set)

        # Original instance
        add_copies(copies, card_num, 1)

        # Winning matches reward copies
        for i in range(card_num + 1, card_num + 1 + matches):
            add_copies(copies, i, copies[card_num])
        total += copies[card_num]
        
    print(f"Answer for Part 2: {total}")
