import day6

test_input = "137, 140\n 318, 75\n 205, 290\n"
simple_test = "0, 0\n 2, 2\n 4, 4\n"

def test_get_coords_list():
    assert day6.get_coord_list(test_input) == [(137,140),(318,75),(205,290)]

def test_manhat():
    assert day6.manhattan_dist((0,0),(2,2)) == 4

def test_min_max():
    coord_list = day6.get_coord_list(test_input)
    assert day6.find_maxes_mins(coord_list) == ((137,318),(75,290))

def test_coords_dict():
    assert day6.make_coord_dict(test_input) == {'0':(137,140),'1':(318,75),'2':(205,290)}

def test_mark_coords():
    assert day6.mark_coords(simple_test) == [['.', '.', '.', '2', '2'], ['.', '1', '1', '.', '2'], ['.', '1', '1', '1', '.'], ['0', '.', '1', '1', '.'], ['0', '0', '.', '.', '.']]

def test_infinites():
    assert day6.get_infinites(simple_test) == set(['0','2','.'])

def test_find_max_area():
    assert day6.find_max_area(simple_test) == 7

def test_safe_zone_eff():
    assert day6.test