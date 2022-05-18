from cgitb import small
import re
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

problem_nodes = construct_nodes(s)
print(find_path(problem_nodes))







