class AD2PNodeLocation:
    def __init__(self, sourceFile = '', line: int = 0, column: int = 0) -> None:
        self.SourceFile = sourceFile
        self.Line = line
        self.Column = column

@staticmethod
def parse_location_from_node(node_location) -> AD2PNodeLocation:
    pass

class AD2PNode:
    def __init__(self, name = '', location: AD2PNodeLocation = AD2PNodeLocation(), description = '') -> None:
        self.Name = name
        self.Location = location
        self.Description = description
    
    def print_violation(self) -> str:
        return 'Violation Found:' + self.Name + ' at line ' + self.Location.Line + ', column ' + self.Location.Column + ' of ' + self.Location.SourceFile
