from itertools import chain

with open('2018/d6-input.txt', 'r')as f:
    s= f.read()

#print(s)

def get_coord_list(s: str) -> list:
    lines = s.splitlines()
    coords = []
    for line in lines:
        x_str,y_str = line.split(',')
        coord = (int(x_str),int(y_str))
        coords.append(coord)
    return coords

def make_coord_dict(s:str) -> dict:
    coord_list = get_coord_list(s)
    c_names =[str(i) for i in range(len(coord_list))]
    return dict(zip(c_names,coord_list))

def manhattan_dist(coord1,coord2):
    return abs(coord2[0]-coord1[0]) + abs(coord2[1]-coord1[1])

def find_maxes_mins(coords):
    max_x = max((coord[0] for coord in coords))
    max_y = max((coord[1] for coord in coords))
    min_x = min((coord[0] for coord in coords))
    min_y = min((coord[1] for coord in coords))
    return (min_x,max_x), (min_y,max_y)

def get_key(test_val,my_dict):
    for key,value in my_dict.items():
        if test_val == value:
            return key

    
def mark_coords(s):
    coords = get_coord_list(s)
    coords_dict = make_coord_dict(s)
    x_bounds, y_bounds = find_maxes_mins(coords)
    arr_2d = []
    #invert array for better visualization
    for y in reversed(range(y_bounds[0],y_bounds[1]+1)):
        x_arr = []
        for x in range(x_bounds[0],x_bounds[1]+1):
            name_distances = { name: manhattan_dist((x,y),coord) for name, coord in coords_dict.items()}
            min_distance = min(name_distances.values())
            dist_values = list(name_distances.values())
            if dist_values.count(min_distance) > 1:
                x_arr.append('.')
            else:
                x_arr.append(get_key(min_distance,name_distances))
        arr_2d.append(x_arr)            
    return arr_2d

def get_infinites(s):
    arr_2d = mark_coords(s)
    infinites = set()
    for x in arr_2d[0]+arr_2d[-1]:
        infinites.add(x)
    y_min_boundary = [y[0] for y in arr_2d]
    y_max_boundary = [y[-1] for y in arr_2d]
    for y in y_min_boundary+y_max_boundary:
        infinites.add(y)
    return infinites

def find_max_area(s):
    coords_dict = make_coord_dict(s)
    arr_2d = mark_coords(s)
    infinites = get_infinites(s)
    max_area = 0
    for name in coords_dict:
        if name not in infinites:
            flat = list(chain.from_iterable(arr_2d))
            name_count = flat.count(name)
            if name_count>max_area:
                max_area=name_count
    return max_area

#print(find_max_area(s))

"""PART 2"""
def safe_zone_eff(s,tolerance):
    coords = get_coord_list(s)
    mins = []
    maxes = []
    for coord in coords:
        x,y = coord
        mins.append((x-tolerance,y-tolerance))
        maxes.append((x+tolerance,y+tolerance))
    biggest_x_min = max(min[0] for min in mins)
    biggest_y_min = max(min[1] for min in mins)
    smallest_x_max = min(max[0] for max in maxes)
    smallest_y_max = min(max[1] for max in maxes)
    area = 0
    for x_val in range(biggest_x_min,smallest_x_max+1):
        for y_val in range(biggest_y_min,smallest_y_max+1):
            all_passed = True
            for coord in coords:
                if manhattan_dist((x_val,y_val),coord)<tolerance:
                    continue
                else:
                    all_passed = False
                    break
            if all_passed == True:
                area+=1
    return area


    

def safe_zone(s):
    coords = get_coord_list(s)
    x_bounds, y_bounds = find_maxes_mins(coords)
    largest_x_range = range(x_bounds[0]-10000,x_bounds[1]+10000+1)
    largest_y_range = range(y_bounds[0]-10000,y_bounds[1]+10000+1)
    area = 0
    for y in largest_y_range:
        for x in largest_x_range:
            all_passed = True
            for coord in coords:
                if manhattan_dist((x,y),coord)<10000:
                    continue
                else:
                    all_passed = False
                    break
            if all_passed == True:
                area+=1
    return area
            
print(safe_zone_eff(s,1000))


    
    

    

    


#test_input = "0, 0\n 2, 2\n 4, 4\n"
#print(mark_coords(test_input))







