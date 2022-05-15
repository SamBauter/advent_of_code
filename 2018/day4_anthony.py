import argparse
import collections
import random
import re
from typing import Counter
from typing import DefaultDict
from typing import List
from typing import NamedTuple
from typing import Tuple


EVENT = re.compile(r'^\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\]')
BEGIN_SHIFT = re.compile(rf'{EVENT.pattern} Guard #(\d+) begins shift$')


class Duration(NamedTuple):
    start: int
    end: int

    @property
    def time_asleep(self) -> int:
        return self.end - self.start


def total_asleep_time(kv: Tuple[int, List[Duration]]) -> int:
    return sum(event.time_asleep for event in kv[1])


def compute_orig(s: str) -> int:
    guard = start = -1
    by_guard: DefaultDict[int, List[Duration]] = collections.defaultdict(list)

    for line in sorted(s.splitlines()):
        begin_shift_match = BEGIN_SHIFT.match(line)
        event_match = EVENT.match(line)
        assert event_match, line
        if begin_shift_match:
            guard = int(begin_shift_match.group(2))
        elif start == -1:
            start = int(event_match.group(1))
        else:
            by_guard[guard].append(Duration(start, int(event_match.group(1))))
            start = -1

    sleepiest, durations = sorted(by_guard.items(), key=total_asleep_time)[-1]

    asleep_times: Counter[int] = collections.Counter()
    for duration in durations:
        asleep_times.update(range(duration.start, duration.end))

    (sleepiest_minute, _), = asleep_times.most_common(1)
    return sleepiest * sleepiest_minute


def compute(s: str) -> int:
    guard = start = -1
    guard_sleep_time: Counter[int] = collections.Counter()
    durations: DefaultDict[int, List[Duration]] = collections.defaultdict(list)

    for line in sorted(s.splitlines()):
        begin_shift_match = BEGIN_SHIFT.match(line)
        event_match = EVENT.match(line)
        assert event_match, line
        if begin_shift_match:
            guard = int(begin_shift_match.group(2))
        elif start == -1:
            start = int(event_match.group(1))
        else:
            duration = Duration(start, int(event_match.group(1)))
            guard_sleep_time[guard] += duration.time_asleep
            durations[guard].append(duration)
            start = -1

    (sleepiest, _), = guard_sleep_time.most_common(1)

    asleep_times: Counter[int] = collections.Counter()
    for duration in durations[sleepiest]:
        asleep_times.update(range(duration.start, duration.end))

    (sleepiest_minute, _), = asleep_times.most_common(1)
    return sleepiest * sleepiest_minute

with open('2018/d4-input.txt','r') as f:
    s = f.read()

print(compute(s))

def compute2(s: str) -> int:
    guard = start = -1
    asleep_times: Counter[Tuple[int, int]] = collections.Counter()

    for line in sorted(s.splitlines()):
        begin_shift_match = BEGIN_SHIFT.match(line)
        event_match = EVENT.match(line)
        assert event_match, line
        if begin_shift_match:
            guard = int(begin_shift_match.group(2))
        elif start == -1:
            start = int(event_match.group(1))
        else:
            for minute in range(start, int(event_match.group(1))):
                asleep_times[(guard, minute)] += 1
            start = -1

    ((sleepiest, sleepiest_minute), _), = asleep_times.most_common(1)
    return sleepiest * sleepiest_minute

print(compute2(s))