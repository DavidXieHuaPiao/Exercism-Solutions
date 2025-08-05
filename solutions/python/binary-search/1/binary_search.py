def find(search_list, value):
    try:
        return search_list.index(value)
    except:
        raise ValueError("value not in array")