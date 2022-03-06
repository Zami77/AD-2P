import sys
import os
from typing import List
from AD2PNode import AD2PNode, AD2PNodeLocation
from Vulnerabilities2038 import vulnerabilities_2038_map as vuln2038_map
from AD2PHelper import is_valid_file, valid_files
from AD2PScanOutput import AD2PScanOutput
from clang.cindex import Index, Cursor

scanned_files: List[str] = []
potential_vulns: List[AD2PNode] = []

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

def AD2P_scan_file(filename: str):
    cur_file_nodes = parse_nodes_from_file(filename)
    for node in cur_file_nodes:
        potential_vulns.append(node)
    scanned_files.append(filename)

def handle_file_or_dir(input_file_or_dir: str):
    if os.path.isdir(input_file_or_dir):
        for root, _dirs, files in os.walk(input_file_or_dir):
            for file in files:
                handle_file_or_dir(root + '/' + file)

    elif is_valid_file(input_file_or_dir):
        AD2P_scan_file(input_file_or_dir)

def end_scan_printout():
    for vuln in potential_vulns:
        print(vuln)
        
    if not scanned_files:
        print("No files were scanned...")
        print("Please ensure you submitted a valid file type.")
        print(f"Valid File Types:{valid_files}")
    else:
        print(scanned_files)

def clean_up():
    scanned_files.clear()
    potential_vulns.clear()

def main(input_file_or_dir):
    clean_up()
    handle_file_or_dir(input_file_or_dir)
    end_scan_printout()
    return AD2PScanOutput(scanned_files, potential_vulns)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('invalid number of arguments.\nUsage:\tpython ', os.path.basename(__file__), ' filename.extension')
        exit()

    main(sys.argv[1])