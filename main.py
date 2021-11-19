import json

our_first_map_file = open('maps.json', )

all_maps_data = json.load(our_first_map_file)

for k in range(1, 3):
    for x in range(0, 10):
        for y in range(0, 10):
            print(all_maps_data[str(k)][x][y] + " ", end='')
        print('\n')

    print('\n')

# print(map_data["1"][0][8])

our_first_map_file.close()
