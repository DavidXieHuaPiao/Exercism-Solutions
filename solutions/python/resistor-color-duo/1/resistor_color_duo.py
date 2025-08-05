def value(colors):
    list = [
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
    string=''
    for i in colors[:2]:
        string+=str(list.index(i))

    return int(string)
