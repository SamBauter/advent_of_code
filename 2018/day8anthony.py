#Code inspired by anthonywritescodes solution
from ast import Call
from typing import Any
from typing import Callable
from typing import List
from typing import NamedTuple
from typing import Optional

class Node(NamedTuple):
    children: List[Any]
    metadata: List[int]

def make_node(values: List[int], cb: Callable[[int],None]) -> Node:
    node = Node([],[])
    child_count = values.pop()
    meta_count = values.pop()

    make_node()