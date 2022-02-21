import sys
import os
from typing import List
from AD2PNode import AD2PNode, AD2PNodeLocation
from Vulnerabilities2038 import vulnerabilities_2038_map as vuln2038_map
from clang.cindex import Index, Cursor

def get_all_nodes(node: Cursor, nodesList = []):
    [get_all_nodes(c, nodesList)
        for c in node.get_children()]
    
    if node.spelling in vuln2038_map:
        nodesList.append(AD2PNode(name=node.spelling, location=AD2PNodeLocation(node.location), description=vuln2038_map[node.spelling].Description))

def parse_nodes_from_file(filename: str):
    index = Index.create()
    translation_unit = index.parse(filename)
    print('Translation Unit', translation_unit.spelling)
    allNodes: List[AD2PNode] = []
    get_all_nodes(translation_unit.cursor, allNodes)
    return allNodes

def main():
    if len(sys.argv) < 2:
        print('invalid number of arguments.\nUsage:\tpython ', os.path.basename(__file__), ' filename')
        return -1

    # TODO: Check if directory, then recursively search
    filename = sys.argv[1]
    allNodes = parse_nodes_from_file(filename)
    for node in allNodes:
        print(node)

if __name__ == '__main__':
    main()