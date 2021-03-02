from json import loads, load, JSONDecodeError


def jsonfileToDic(jsonfile):
    """
    Load a json formatted string or file

    :param jsonfile: Json string or path to a json file
    :return: dic
    """
    try:
        return loads(jsonfile)
    except JSONDecodeError:
        try:
            with open(jsonfile) as jsonfile:
                return load(jsonfile)
        except JSONDecodeError:
            raise Exception("Not a json file")


def removePointInJsonKeys(contents: bytes):
    """
    This function permit to replace all '.' by a ',' in all key of a json file.

    :param contents: json read file
    :return: string
    """
    contents = contents.decode('utf-8')
    mod = ""
    for line in iter(contents.splitlines()):
        new_line = ""
        flag = 0
        for char in line:
            if char == '"':
                flag = flag + 1
            if char == '.' and flag == 1:
                char = ','
            new_line = new_line + char
        mod = mod + "\n" + new_line
    return mod
