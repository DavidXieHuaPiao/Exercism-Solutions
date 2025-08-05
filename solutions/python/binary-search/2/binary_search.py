def find(search_list, value):
        if value not in search_list:
                raise ValueError("value not in array")
        
        index=len(search_list)//2
        middle_value = search_list[index]
        if value > middle_value:
                return index + find(search_list[index:], value)
        if value < middle_value:
                return find(search_list[:index], value)
        return index