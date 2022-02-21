from clang.cindex import File, SourceLocation

class AD2PNodeLocation:
    def __init__(self, sourceFile: SourceLocation = SourceLocation()):
        if sourceFile.file is None:
            self.SourceFile = 'Unknown'
        else:
            self.SourceFile = sourceFile.file.name
        self.Line = sourceFile.line
        self.Column = sourceFile.column

class AD2PNode:
    def __init__(self, name: str = '', location: AD2PNodeLocation = AD2PNodeLocation(), description: str = '') -> None:
        self.Name = name
        self.Location = location
        self.Description = description
    
    def __str__(self) -> str:
        return '|Violation Found| Name: %-25s line: %-10d column: %-10d Source: %-300s' % (self.Name, self.Location.Line, self.Location.Column, self.Location.SourceFile)
