def get_data(file:str = 'data.txt'):
    try:
        with open(file, 'r') as f:
            data = f.readlines()
            return data
    except Exception as e:
        print(e)
    else:
        return None

# Check if any number neighbouring the current cursor (which has symbol)
def checkMid(index: int, line: list):
    part_numbers = []
    c = line[index]
    left = checkLeft(index, line)
    right = checkRight(index, line)
    mid = None
    if c == "." or not c.isnumeric():
        if left:
            part_numbers.extend([int(left)])
        if right:
            part_numbers.extend([int(right)])
    elif c.isnumeric():
        mid = int(f"{left if left != None else ''}{c}{right if right != None else ''}")
        part_numbers.extend([mid])
        line[index] = "."
    return part_numbers

# Find numbers on left of current cursor
def checkLeft(index: int, line: list):
    # Check if there is anything on the left
    if index > 0:
        numbers = []
        for x in range(index-1, -1, -1):
            c = line[x]
            if c == "." or not c.isnumeric():
                break
            elif c.isnumeric():
                numbers.append(c)
                line[x] = "."
        if len(numbers) > 0:
            return "".join(numbers[::-1])
        else:
            return None
    else:
        return None

# Find numbers on right of current cursor
def checkRight(index: int, line: list):
    # Check if there is anything on the right
    if index < (len(line) - 1):
        numbers = []
        for x in range(index+1, len(line), 1):
            c = line[x]
            if c == "." or not c.isnumeric():
                break
            elif c.isnumeric():
                numbers.append(c)
                line[x] = "."
        if len(numbers) > 0:
            return "".join(numbers)
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    data = get_data()

    # Initialize
    part_numbers = []
    total = 0
    buf0 = None
    buf1 = None
    buf2 = None
 
    for d in data:
        # Can imagine the code scanning 3 lines at a time on provided data
        buf2 = buf1             # for line 3 (third line)
        buf1 = buf0             # for line 2 (second line)
        buf0 = list(d.strip())  # for line 1 (first line in data.txt)

        # Wait until all buffers are filled
        if buf0 == None or buf1 == None or buf2 == None:
            continue

        # Go through from left to right, across all 3 lines
        for i in range(len(buf0)):
            c1 = buf1[i]    # data of second line
            if c1 == "*":   # if its "*"/gear
                part_numbers = []
                part_numbers.extend(checkMid(i, buf0))
                part_numbers.extend(checkMid(i, buf1))
                part_numbers.extend(checkMid(i, buf2))
                if len(part_numbers) == 2:  # only if exactly 2 gears
                    total += (part_numbers[0]*part_numbers[1])

    print(f"Answer for Part 2: {total}")
