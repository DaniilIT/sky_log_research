import re
from typing import Iterator, List, Any, Optional


def build_query(cmd: str, val: str, file_list: Iterator) -> List[Any]:
    result = []

    if cmd == 'filter':
        # result = [row for row in file_list if val in row]
        result = list(filter(lambda row: val in row, file_list))
    elif cmd == 'map':
        # result = [row.split()[int(val)] for row in file_list]
        result = list(map(lambda row: row.split()[int(val)], file_list))
    elif cmd == 'unique':
        result = list(set(file_list))
    elif cmd == 'sort':
        reverse = (val == 'desc')
        result = sorted(file_list, reverse=reverse)
    elif cmd == 'limit':
        result = list(file_list)[:int(val)]
    elif cmd == 'regex':
        pattern: re.Pattern = re.compile(val)
        result = list(filter(lambda row: pattern.search(row), file_list))
    return result
