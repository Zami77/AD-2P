from typing import List
from AD2PNode import AD2PNode

class AD2PScanOutput:
    def __init__(self, scanned_files: List[str] = [], potential_vulns: List[AD2PNode] = []) -> None:
        self.scanned_files = scanned_files
        self.potential_vulns = potential_vulns