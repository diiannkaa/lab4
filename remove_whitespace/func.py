def remove_whitespace(string):
    while string[0] == ' ' or string[0] == '\t':
        string = string[1:]
    while string[-1] == ' ' or string[-1] == '\t':
        string = string[:-1]
    return string
