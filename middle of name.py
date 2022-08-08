def get_middle(s):
    str_len = len(s)
    if str_len % 2 > 0:
        return(s[str_len / 2])
    if str_len % 2 == 0:
        return(s[(str_len / 2 - 1): (str_len / 2 + 1)])
    else:
        return s


print (get_middle("of"))

