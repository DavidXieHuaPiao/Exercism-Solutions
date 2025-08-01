def label(colors):
        list_color = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]

        number= int(str(list_color.index(colors[0]))+str(list_color.index(colors[1])))
        power = list_color.index(colors[2])
        result = number*(10**power)
        prefix = [' ', '0 ', '00 ', ' kilo', '0 kilo', '00 kilo', 'mega']
        if result >= 10**9:
            return str(result//(10**9)) + ' gigaohms'
        if result >= 10**6:
            return str(result//(10**6)) + ' megaohms'
        if result >= 10**3:
            return str(result//(10**3)) + ' kiloohms'
        return str(result) + ' ohms'