import re
import datetime

s = "\
    [1518-04-12 00:36] falls asleep\n \
    [1518-02-22 00:58] wakes up\n \
    [1518-10-17 00:01] wakes up\n \
    [1518-07-19 00:03] falls asleep\n \
    [1518-09-19 00:27] falls asleep\n \
    [1518-10-24 00:52] falls asleep\n \
    [1518-05-26 23:59] Guard #71 begins shift\n"

for line in s.splitlines():
    matching_str = re.search("\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}",line).group()
    print(datetime.datetime.fromisoformat(matching_str))

s2 = "801-392-6249"
print(re.search("\d\d\d-\d\d\d-\d\d\d\d",s2).group())

