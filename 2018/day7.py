from cgitb import small
import re
import string
with open('2018/d7-input.txt', 'r') as f:
    s = f.read()

small_Ex = "Step C must be finished before step A can begin.\n\
Step C must be finished before step F can begin.\n\
Step A must be finished before step B can begin.\n\
Step A must be finished before step D can begin.\n\
Step B must be finished before step E can begin.\n\
Step D must be finished before step E can begin.\n\
Step F must be finished before step E can begin."



class InstructionNode:
    def __init__(self,node_name, initial_prereq=None):
        self.node_name = node_name
        self.prereqs = []
        if initial_prereq:
            self.prereqs.append(initial_prereq)
    
    def add_prereq(self, additional_prereq):
        self.prereqs.append(additional_prereq)
    
    def __repr__(self):
        return f"{self.node_name} Pre:{self.prereqs}\n"
    
        
def construct_nodes(s: str) -> list[InstructionNode]:
    lines = s.splitlines()
    instruction_nodes = []
    for line in lines:
        prereq = re.search("Step\s[A-Z]", line).group(0)[-1]
        node_name = re.search("step\s[A-Z]", line).group(0)[-1]
        if len(instruction_nodes) == 0:
            instruction_nodes.append(InstructionNode(node_name,prereq))
        else:
            already_existed = False
            for instr_node in instruction_nodes:
                if instr_node.node_name == node_name:
                    instr_node.add_prereq(prereq)
                    already_existed = True
            if not already_existed:
                instruction_nodes.append(InstructionNode(node_name,prereq))
    return instruction_nodes

def find_start_node(node_list):
    name_set = {x.node_name for x in node_list}
    prereq_set = {prereq for instr_node in node_list for prereq in instr_node.prereqs}
    starters = prereq_set-name_set
    #if len(starter) > 1:
        #raise ValueError("More than one starter Node")
    return starters

def find_path(node_list):
    path = ""
    starters = find_start_node(node_list)
    starter_list = list(starters)
    starter_list.sort()
    start = starter_list.pop(0)
    path+=start
    next_steps = []
    for starter in starter_list:
        new_node = InstructionNode(starter)
        node_list.append(new_node)
        next_steps.append(new_node)
    initial_length = len(node_list)+1
    current = InstructionNode(start,None)

    while len(path)<initial_length:
        for node in node_list:
            if node in next_steps:
                continue
            elif current.node_name in node.prereqs:
                next_steps.append(node)
            else:
                continue

        for potential in next_steps:
            if potential in node_list:
                node_list.remove(potential)

        next_steps.sort(key = lambda n: n.node_name)

        for index, next_candidate in enumerate(next_steps):
            unsatisfied_prereqs = set(next_candidate.prereqs) - set(path)
            if len(unsatisfied_prereqs) > 0:
                continue
            else:
                current = next_steps.pop(index)
                path+=current.node_name
                break
    return path
        
    
#small_nodes = construct_nodes(small_Ex)
#print(find_start_node(small_nodes))
#print(find_path(small_nodes))

#problem_nodes = construct_nodes(s)
#print(find_path(problem_nodes))

"""PART 2"""

def list_starter_nodes(node_list):
    node_name_list = list(find_start_node(node_list))
    return [InstructionNode(n_name) for n_name in node_name_list]

def construct_all_nodes(s):
    node_list = construct_nodes(s)
    node_list.extend(list_starter_nodes(node_list))
    return node_list

def calc_node_worktime(node,durations):
    return durations[node.node_name]+60


def node_complete(triple):
    if triple[2] == 0:
        return True
    elif triple[2] > 0:
        return False
    else:
        raise ValueError(f"{triple[2]} should never be negative")

def find_availables(complete_nodes,node_list):
    satisfied_prereqs = [node.node_name for node in complete_nodes]
    return [node for node in node_list if set(node.prereqs) - set(satisfied_prereqs) == set()]
    

def transfer_node(node_triple,completed_nodes,avail_workers):
    completed_nodes.append(node_triple[1])
    avail_workers.append(node_triple[0])

def assign_worker_to_node(available_workers,available_nodes,current_nodes,durations,node_list):
    available_nodes.sort(key=lambda n:n.node_name)
    while available_workers and available_nodes:
                take_node = available_nodes.pop(0)
                assigned_worker = available_workers.pop(0)
                node_list.remove(take_node)
                current_nodes.append([assigned_worker,take_node,calc_node_worktime(take_node,durations)])
    

def fast_forward(current_nodes):
    if current_nodes:
        return min(node[2] for node in current_nodes)
    else:
        return 0



def find_duration(s, workers = 5):
    durations = dict(zip(string.ascii_uppercase,(x+1 for x in range(len(string.ascii_uppercase)))))
    node_list = construct_all_nodes(s)
    complete_nodes = []
    available_nodes = find_availables(complete_nodes,node_list)
    total_time = 0
    total_len = len(node_list)
    current_nodes = []
    available_workers = [x for x in range(workers)]

    while len(complete_nodes) < total_len:
        elapsed = fast_forward(current_nodes)
        for node_triple in current_nodes:
            node_triple[2]-=elapsed
            if node_complete(node_triple):
                transfer_node(node_triple,complete_nodes,available_workers)
        current_nodes = [current_node for current_node in current_nodes if current_node[2]>0]
        available_nodes.extend(find_availables(complete_nodes,node_list))
        available_nodes = list(set(available_nodes))

        assign_worker_to_node(available_workers,available_nodes,current_nodes,durations,node_list)
        total_time+=elapsed
    return total_time

print(find_duration(s))
            

            
                    

            
        



        




    

















