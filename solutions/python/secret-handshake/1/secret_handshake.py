def commands(binary_str):
    count = 0
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    do = []
    for i in binary_str[::-1]:
        if int(i) and count != 4:
            do.append(actions[count])
        elif int(i):
            do.reverse()
        count+=1
    return do