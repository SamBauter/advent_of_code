from itertools import chain
import sys

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
    min_x, min_y = (sys.maxsize,sys.maxsize)
    max_x, max_y = (0,0)

    for coord in coords:
        x,y = coord
        max_x, max_y = max(x,max_x) , max(y,max_y)
        min_x, min_y = min(x,min_x) , min(y,min_y)
    
    area = 0
    adj = tolerance // len(coords)
    
    for x_val in range(min_x-adj,max_x+adj):
        for y_val in range(min_y-adj,max_y+adj):
            total_distance = 0
            for coord in coords:
                total_distance +=manhattan_dist(coord,(x_val,y_val))
            if total_distance<tolerance:
                area+=1
    return area
     
 
            
print(safe_zone_eff(s,10000))


    
    

    

    


#test_input = "0, 0\n 2, 2\n 4, 4\n"
#print(mark_coords(test_input))







