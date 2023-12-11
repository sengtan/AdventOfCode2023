import re

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

        # Find the first number digit from the string
        num1 = re.search(r'\d', d)

        # Reverse the string and find the first number digit
        num2 = re.search(r'\d', d[::-1])

        # Combine both numbers side by side, {num1}{num2}, then sum up with previous result
        total += int(f"{num1.group()}{num2.group()}")

    print(f"Answer for Part 1: {total}")