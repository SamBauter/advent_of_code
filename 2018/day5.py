
import string


smaller_test = "dabAcCaCBAcCcaDA"
longer_test = "VRrQqmPoOpMdAaDMQqmDZwWzfFdJjGmMgtTyYMmV"
end_test = "bBbBbbBAab"

with open('2018/d5-input.txt','r') as f:
    s = f.read().strip()



#Just to get while loop started
def react(s):
    ccount = 1
    first_pass = ""
    while ccount > 0:
        collision = False
        ccount = 0
        for index, c in enumerate(s):
            if index == len(s)-1:
                if collision:
                    collision = False
                else:
                    first_pass+=c
                break
            if collision:
                collision = False
                continue
            else:
                next = s[index+1]
                if c.islower() and c.upper() == next:
                    collision = True
                    ccount+=1
                elif c.isupper() and c.lower() == next:
                    collision = True
                    ccount+=1
                    pass
                else:
                    first_pass+= c
        s = first_pass
        first_pass = ''
    return s

#print(len(react(s)))

"""Part 2"""
def remove_atom(lower_atom,polymer_str):
    ret = polymer_str.replace(lower_atom,"")
    return ret.replace(lower_atom.upper(),"")

#test = "AAbbaCcDEf"
#print(remove_atom("a",test))

def find_shortest_poly(polymer_str):
    shortest = len(polymer_str)
    for c in string.ascii_lowercase:
        test_str = remove_atom(c,polymer_str)
        r_length = len(react(test_str))
        if r_length<shortest:
            shortest = r_length
    return shortest

print(find_shortest_poly(s))








