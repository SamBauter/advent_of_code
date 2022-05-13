import itertools

with open('2018/1-input.txt','r')as f0:
    global total_s 
    total_s= f0.read()

def find_total():
    with open('2018/1-input.txt','r')as f1:
        total = 0
        while line:=f1.readline():
                total += int(line)
    return total


def find_repeat():
    with open('2018/1-input.txt','r')as f2:
        total = 0
        seen = {total}
        while True:
            if line := f2.readline():
                total+=int(line)
                if total in seen:
                    return total
                else:
                    seen.add(total)
            else:
                f2.seek(0)

#Other Implementation from anthonywritescode
def compute(s: str) -> int:
    val = 0
    seen = {val}
    for line in itertools.cycle(s.splitlines()):
        val+= int(line)
        if val in seen:
            return val
        else:
            seen.add(val)

if __name__ == '__main__':
    print(find_total())
    print(find_repeat())
    print(compute(total_s))
