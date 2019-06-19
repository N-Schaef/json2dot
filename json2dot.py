#!/usr/bin/python3

import json
import sys
from collections import OrderedDict


def jsonObject2Dot(js, curr, nodes, connections):
    assert isinstance(nodes,list)
    assert isinstance(connections,list)
    assert isinstance(curr,str)
    for  key, value in js.items():
        curr_key = curr + "_" + key
        nodes.append((key,curr_key))
        connections.append((curr,curr_key))
        json2Dot_(value, curr_key,nodes,connections)

def jsonArray2Dot(js, curr, nodes, connections):
    assert isinstance(nodes,list)
    assert isinstance(connections,list)
    assert isinstance(curr,str)
    for i in range(len(js)):
        key = str(i)
        curr_key = curr + "_" + key
        nodes.append((key, curr_key))
        connections.append((curr, curr_key))
        json2Dot_(js[i], curr_key, nodes, connections)

def json2Dot_(js, curr, nodes, connections):
    assert isinstance(nodes,list)
    assert isinstance(connections,list)
    assert isinstance(curr,str)

    if isinstance(js, list):
        jsonArray2Dot(js,curr,nodes,connections)
    else:
        if isinstance(js,dict):
            jsonObject2Dot(js,curr,nodes,connections)



def json2Dot(js):
    curr = ""
    nodes = []
    connections = []
    if isinstance(js,dict):
        nodes.append(("",""))
    json2Dot_(js,curr,nodes,connections)


    dot_str = "digraph graphname {\n"
    for name,path in nodes:
        if name == "" and path == "":
            path = "root"
        dot_str += path+" [label=\""+name+"\"];\n"
    dot_str += "\n"

    for parent,child in connections:
        if parent == "":
            parent = "root"
        dot_str += parent+" -> "+child+";\n"


    dot_str+="\n}"
    return dot_str


def main():

    json_string = ""
    for line in sys.stdin:
        json_string = json_string + line
    sys.stdout.write(json2Dot(json.loads(json_string,object_pairs_hook=OrderedDict)))
    return 0

if __name__ == '__main__':
    sys.exit(main())
