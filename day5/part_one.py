def get_data(file:str = 'data.txt'):
    try:
        with open(file, 'r') as f:
            data = f.readlines()
            return data
    except Exception as e:
        print(e)
    else:
        return None

def finder(seed, data):
    # check if seed is between any of the provided ranges
    is_between = False
    value = None
    for d in data:
        if d[1] <= seed <= d[1]+d[2]:
            is_between = True
            value = d[0] + (seed - d[1])
            continue
    
    if not is_between:
        value = seed
    
    print(value)
    return value

if __name__ == "__main__":
    data = get_data()
 
    seeds = []
    mapping = {}

    current_title = None

    for d in data:
        d = d.strip()
        if ":" in d:
            current_title = d.split(":")[0]
            if current_title == "seeds":
                seeds = [int(x) for x in d.split(":")[1].split(" ")[1:-1]]
        elif d != "":
            if current_title not in mapping.keys():
                mapping[current_title] = []
            mapping[current_title].append(tuple([int(x) for x in d.split(" ")]))

    final = None

    for seed in seeds:
        soil = finder(seed, mapping["seed-to-soil map"])
        fert = finder(soil, mapping["soil-to-fertilizer map"])
        water = finder(fert, mapping["fertilizer-to-water map"])
        light = finder(water, mapping["water-to-light map"])
        temp = finder(light, mapping["light-to-temperature map"])
        humi = finder(temp, mapping["temperature-to-humidity map"])
        loca = finder(humi, mapping["humidity-to-location map"])

        if final == None:
            final = loca
        elif loca < final:
            final = loca
        print(f"seed:{seed}, soil:{soil}, fert:{fert}, water:{water}, light:{light}, temp:{temp}, humi:{humi}, loca:{loca}")
    
    print(f"Answer for Part 1: {final}")
    