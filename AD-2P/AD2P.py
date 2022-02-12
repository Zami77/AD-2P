import sys
import os
from Vulnerabilities2038 import vulnerabilities_2038_map as vuln_map
from datetime import datetime
from clang.cindex import Index, Cursor

def get_all_nodes(node: Cursor, nodesList = []):
    [get_all_nodes(c, nodesList)
        for c in node.get_children()]
    
    # TODO: Check against JSON list of potential vulnerabilities
    if node.spelling in vuln_map:
        nodesList.append({ 
            'kind' : node.kind,
            'spelling' : node.spelling,
            'displayname' : node.displayname,
            'type' : node.type,
            'line' : node.location
        })

def parse_nodes_from_file(filename: str):
    index = Index.create()
    translation_unit = index.parse(filename)
    print('Translation Unit', translation_unit.spelling)
    allNodes = []
    get_all_nodes(translation_unit.cursor, allNodes)
    return allNodes

def main():
    if len(sys.argv) < 2:
        print('invalid number of arguments.\nUsage:\tpython ', os.path.basename(__file__), ' filename')
        return -1

    # TODO: Check if directory, then recursively search
    print(vuln_map.keys())
    filename = sys.argv[1]
    allNodes = parse_nodes_from_file(filename)
    # print(allNodes)

if __name__ == '__main__':
    main()