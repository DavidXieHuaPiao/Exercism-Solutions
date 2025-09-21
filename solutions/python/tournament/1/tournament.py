def tally(rows):
    table = [
    "Team                           | MP |  W |  D |  L |  P"]
    teams = {
        "Allegoric Alaskans": [0,0,0,0,0],
        "Devastating Donkeys": [0,0,0,0,0],
        "Blithering Badgers": [0,0,0,0,0],
        "Courageous Californians": [0,0,0,0,0]
    }
    for play in rows:
        info = play.split(";")
        for i in info[:-1]:
            teams[i][0]+=1
        if info[-1]=="draw":
            for i in info[:-1]:
                teams[i][2]+=1
        else:
            if info[-1]=="loss":
                info[0], info[1] = info[1], info[0]
            teams[info[0]][1]+=1
            teams[info[1]][3]+=1
        for key in teams:
            teams[key][-1]= teams[key][1]*3+teams[key][2]
    teams_sorted= sorted(teams.items(), key=lambda item: (-item[1][-1], item[0]))
    for i in teams_sorted[::-1]:
        if i[1][0]==0:
            teams_sorted.remove(i)
    for i in teams_sorted:
        text = f"{i[0]}" + " "*(31-len(i[0])) + "|"
        count=0
        for x in i[1]:
            count+=1
            text+= " "*(3-len(str(x))) + str(x)
            if count!=5:
                text+=" |"
        table.append(text)
    return table