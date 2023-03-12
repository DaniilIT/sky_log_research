def build_query(cmd, val, file_list):
    result = None

    if cmd == 'filter':
        # result = [row for row in file_list if val in row]
        result = list(filter(lambda row: val in row, file_list))
    elif cmd == 'map':
        val = int(val)
        # result = [row.split()[val] for row in file_list]
        result = list(map(lambda row: row.split()[val], file_list))
    elif cmd == 'unique':
        result = list(set(file_list))
    elif cmd == 'sort':
        reverse = (val == 'desc')
        result = sorted(file_list, reverse=reverse)
    elif cmd == 'limit':
        val = int(val)
        result = file_list[:val]

    return result
