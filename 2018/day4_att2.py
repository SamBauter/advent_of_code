from datetime import datetime as dt
import re
from collections import defaultdict
from collections import Counter

class ShiftEntry:
    def __init__(self,line):
        self.line = line
        self.d_str = re.search("\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}",line).group()
        self.timestamp = dt.fromisoformat(self.d_str)
        self.guard_id = 0
        self.awake = True
        self.asleep = False
        if "asleep" in line:
            self.asleep = True
            self.awake = False
        elif "wakes up" in line:
            self.awake = True
            self.asleep = False
        else:
            self.guard_id = re.search("#\d+",line).group().replace("#","")
        
    def __repr__(self):
        return f"s: {self.line} time: {self.d_str} guard_id: {self.guard_id} asleep: {self.asleep} awake: {self.awake}"

        
def make_shift_list():
    shift_list = []
    with open('2018/d4-input.txt', 'r') as f:
        s = f.read()
    for line in s.splitlines():
        shift_list.append(ShiftEntry(line))
    return shift_list

def sort_shift_list(shift_list):
    shift_list.sort(key = lambda shift:shift.timestamp)

def assign_id_to_missing(shift_list):
    current_id = 0
    for shift in shift_list:
        if shift.guard_id:
            current_id = shift.guard_id
        elif not current_id:
            raise ValueError("Current ID should always be set in a sorted entry list")
        else:
            shift.guard_id = current_id

def calc_time(shift_list):
    guard_dict = defaultdict(list)
    minutes_slept = defaultdict(int)
    for index, shift in enumerate(shift_list):
        if shift.asleep:
            next = shift_list[index+1]
            start_min = shift.timestamp.minute
            stop_min = next.timestamp.minute
            if start_min < stop_min:
                guard_dict[shift.guard_id].extend([minute for minute in range(start_min,stop_min)])
                minutes_slept[shift.guard_id] += (stop_min-start_min)
            elif stop_min<start_min:
                guard_dict[shift.guard_id].extend([minute for minute in range(start_min,60)])
                guard_dict[shift.guard_id].extend([minute for minute in range(0,stop_min)])
                minutes_slept[shift.guard_id] += (60-start_min)
                minutes_slept[shift.guard_id] += stop_min
        else:
            continue
    return guard_dict, minutes_slept


            
     


shifts = make_shift_list()
sort_shift_list(shifts)
#print(len(shifts))
assign_id_to_missing(shifts)
#print(calc_time(shifts))
g_dict, m_slept = calc_time(shifts)



def get_sleepy_guard(min_dict): 
    minute_max = 0
    sleepy_guard = ''
    for name in m_slept:
        if m_slept[name] > minute_max:
            minute_max = m_slept[name]
            sleepy_guard = name
        else:
            continue
    return sleepy_guard

def get_sleepy_minute(g_dict,sleepy_guard):
    return Counter(g_dict[sleepy_guard]).most_common(1)[0][0]

sleepy_guard = get_sleepy_guard(m_slept)
sleepy_minute = get_sleepy_minute(g_dict, sleepy_guard)
#print(int(sleepy_guard)*sleepy_minute)

"""PART 2"""
def most_occurent_minute(g_dict):
    highest_min_occurences = 0
    minute_name = -1
    guard_name = ''
    for guard, min_list in g_dict.items():
        ccount = Counter(min_list)
        most_com = ccount.most_common(1)
        minute_value = most_com[0][0]
        number_of_times = most_com[0][1]
        if number_of_times > highest_min_occurences:
            minute_name = minute_value
            highest_min_occurences = number_of_times
            guard_name = guard
    return minute_name*int(guard_name)

print(most_occurent_minute(g_dict))





#print(shifts[:9])




    

"""for line in s.splitlines():
    d_str = re.search("\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}",line).group()
    timestamp = dt.fromisoformat(d_str)
    print(timestamp)
    if "asleep" in line:
        asleep = True
    elif "wakes up" in line:
        awake = True
    else:
        guard_id = re.search("#\d+",line).group().replace("#","")
        print(guard_id)"""




# %%
