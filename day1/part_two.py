import re

numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
srebmun = {"eno":1, "owt":2, "eerht":3, "ruof":4, "evif":5, "xis":6, "neves":7, "thgie":8, "enin":9}

def test():
    test_data = {
        "two1nine": 29,
        "eightwothree": 83,
        "abcone2threexyz": 13,
        "xtwone3four": 24,
        "4nineeightseven2": 42,
        "zoneight234": 14,
        "7pqrstsixteen": 76
    }

    for d, r in test_data.items():

        # find numbers in word form and digit form
        numstr = "|".join(numbers)

        # Find all numbers from the string and return a list
        nums = re.findall(f"({numstr}|\d)", d)

        # Combine both numbers side by side, {num1}{num2}, then sum up with previous result
        result = int(f"{to_int(nums[0])}{to_int(nums[-1])}")

        if result == r:
            print("Pass")
        else:
            print(f"Fail, provided {d} expect {r} get {result}")

def get_data(file:str = 'data.txt'):
    try:
        with open(file, 'r') as f:
            data = f.readlines()
            return data
    except Exception as e:
        print(e)
    else:
        return None

def to_int(num):
    if num.isnumeric():
        return int(num)
    elif num in numbers.keys():
        return numbers[num]

if __name__ == "__main__":
    data = get_data()
    total = 0

    for d in data:

        # find numbers in word form and digit form
        numstr = "|".join(numbers)

        # Find all numbers from the string and return a list
        nums = re.findall(f"({numstr}|\d)", d)

        # find numbers in word form and digit form in reverse
        numstr = "|".join(srebmun)

        # Find all numbers from the reversed string and return a list
        smun = re.findall(f"({numstr}|\d)", d[::-1])

        # Combine both numbers side by side, {num1}{num2}, then sum up with previous result
        total += int(f"{to_int(nums[0])}{to_int(smun[0][::-1])}")

    print(f"Answer for Part 2: {total}")