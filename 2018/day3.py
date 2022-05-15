#%%
from itertools import chain
from turtle import width

small_example = "#1 @ 1,3: 4x4\n #2 @ 3,1: 4x4\n #3 @ 5,5: 2x2"

with open('2018/d3-input.txt', 'r') as f:
    cut_string= f.read()

def process_str(s):
    processed_list = []
    for line in s.splitlines():
        l = line.split()
        id_int=int(l[0][1:])
        left_top = l[2].split(',')
        left = int(left_top[0])
        top = int(left_top[1][:-1])
        width_s,height_s = l[3].split('x')
        width = int(width_s)
        height = int(height_s)
        processed_list.append((id_int,left,top,width,height))
    return processed_list

#print(process_str(small_example))


empty_grid1 = [[0 for x in range(0,1000)] for y in range(0,1000)]

def change_grid(s,empty_grid):
    processed_cuts = process_str(s)
    for cut in processed_cuts:
        left = cut[1]
        top = cut[2]
        width = cut[3]
        height = cut[4]
        for vertical_index in range(top,top+height):
            for horizontal_index in range(left,left+width):
                empty_grid[vertical_index][horizontal_index] +=1

def count_collisions(empty_grid):
    flat = list(chain.from_iterable(empty_grid))
    col_count= 0
    for val in flat:
        if val>1:
            col_count+=1
    return col_count

def search_for_1s(s,changed_grid):
    processed_cuts = process_str(s)
    for cut in processed_cuts:
        int_id = cut[0]
        left = cut[1]
        top = cut[2]
        width = cut[3]
        height = cut[4]
        coords = []
        for vertical_index in range(top,top+height):
            for horizontal_index in range(left,left+width):
                coords.append((vertical_index,horizontal_index))
        failed = False
        for y_coord,x_coord in coords:
            if changed_grid[y_coord][x_coord] == 1:
                continue
            else:
                failed = True
                break
        if not failed:
            return int_id
        

            
                




                    




#change_grid(small_example,empty_grid1)
#print(count_collisions(empty_grid1))

change_grid(cut_string,empty_grid1)
print(count_collisions(empty_grid1))
print(search_for_1s(cut_string,empty_grid1))



# %%
