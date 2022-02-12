import json

y2038_json = 'y2038-C-time-references.json'
vulnerabilities_2038_map = {}

class Y2038DotComVulnerability:
    def __init__(self, 
            category: str = '', 
            name: str = '', 
            header: str = '', 
            isC11: bool = False, 
            isPosix: bool = False, 
            isLinux: bool = False, 
            isWindows: bool = False, 
            isMacOSX: bool = False, 
            isVxWorks: bool = False, 
            description: str = '') -> None:
        self.Category = category
        self.Name = name
        self.Header = header
        self.IsC11 = isC11
        self.IsPosix = isPosix
        self.IsLinux = isLinux
        self.IsWindows = isWindows
        self.IsMacOSX = isMacOSX
        self.IsVxWorks = isVxWorks
        self.Description = description

def fill_vulnearbility_map():
    json_file = open(y2038_json)

    json_dump = json.load(json_file)

    # Keys from y2038_json
    for node in json_dump:
        vulnerabilities_2038_map[node["Name"]] = Y2038DotComVulnerability(node["Category"], node["Name"], node["Header"], node["C11 (ISO)"], node["POSIX"], node["Linux"], node["Windows"], node["Mac OSX"], node["VxWorks"], node["Description"])

    json_file.close()

fill_vulnearbility_map()
