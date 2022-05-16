from datetime import datetime as dt
from collections import defaultdict
from collections import Counter

example = "[1518-04-12 00:00] Guard #71 begins shift\n[1518-04-12 00:36] falls asleep\n [1518-02-22 00:58] wakes up\n"

def parse_dt_str(s):
    return s[s.index('[')+1:s.index(']')]

class LogEntry:
    def __init__(self, s):
        self.s = s
        self.entry_time = dt.fromisoformat(parse_dt_str(s))
        self.start = False
        self.guard_id = 0
        if 'begins' in s:
            self.start = True
            self.awake = True
            self.asleep = False
            self.guard_id = int(s[s.index('#')+1:s.index('b')-1])
        elif 'asleep' in s:
            self.asleep = True
            self.awake = False
        else:
            self.awake = True
            self.asleep = False
    def __str__(self):
        return self.s

def assign_id(log_list):
    current_id = 0
    for log in log_list:
        if log.start and log.guard_id:
            current_id = log.guard_id
        else:
            log.guard_id = current_id

def guard_dict(log_list):
    time_dict = defaultdict(list)
    for index, log in enumerate(log_list):
        if log.awake and log.asleep:
            raise ValueError('INVALID LOG BOTH ASLEEP AND AWAKE')
        if not log.awake and not log.asleep:
            raise ValueError('INVALID LOG NOT ASLEEP OR AWAKE')
        s_rep = log.__str__()
        if log.guard_id == 3299:
            if log.asleep:
                start_min = log.entry_time.minute
                end_min = log_list[index+1].entry_time.minute
                if start_min<end_min:
                    time_dict[str(log.guard_id)].extend([m for m in range(start_min,end_min)])
                else:
                    time_dict[str(log.guard_id)].extend(m for m in range(start_min,60))
                    time_dict[str(log.guard_id)].extend(m for m in range(0,end_min))
            else:
                continue
    return time_dict


def find_sleepiest(input_dict):
    most_minutes_slept = 0
    sleepiest_guard = None
    for id, times in input_dict.items():
        if len(times)> most_minutes_slept:
            sleepiest_guard = id
            most_minutes_slept = len(times)
        else:
            continue
    return sleepiest_guard

def test_sleepiest(input_dict):
    list_lens = []
    for id, times in input_dict.items():
        list_lens.append((id,len(times)))
    return list_lens


def find_minute(input_dict):
    sleepiest_id = find_sleepiest(input_dict)
    minute = Counter(input_dict[sleepiest_id]).most_common(1)[0][0]
    return minute


log_list1 = []
with open('2018/d4-input.txt','r') as fin:
    while line :=fin.readline():
        new_entry = LogEntry(line)
        log_list1.append(new_entry)

log_list1.sort(key = lambda x: x.entry_time)
assign_id(log_list1)

the_dict=guard_dict(log_list1)

print(find_sleepiest(the_dict))
print(find_minute(the_dict))

print(f"The Solution is: {int(find_sleepiest(the_dict))*find_minute(the_dict)}")




        
        






    
   








