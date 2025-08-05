def resistor_label(colors):
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
        tolerance = dict(
        grey=0.05,
        violet=0.1,
        blue=0.25,
        green=0.5,
        brown=1,
        red=2,
        gold=5,
        silver=10)

        if len(colors) == 1:
            result = 0
            return str(result) + ' ohms'
        elif len(colors) == 4:
            number= int(str(list_color.index(colors[0]))+str(list_color.index(colors[1])))
            power = list_color.index(colors[2])
            result = number*(10**power)
        elif len(colors) == 5:
            number= int(str(list_color.index(colors[0]))+str(list_color.index(colors[1]))+str(list_color.index(colors[2])))
            power = list_color.index(colors[3])
            result = number*(10**power)

    
        prefix = [' ', '0 ', '00 ', ' kilo', '0 kilo', '00 kilo', 'mega']
        if result >= 10**9:
            simplified=str(result/(10**9))
            simp_f=simplified
            if simplified.endswith('.0'):
                simp_f=simplified.rstrip('.0')
            return simp_f + ' gigaohms' + ' ±{}%'.format(tolerance[colors[-1]])
        if result >= 10**6:
            simplified=str(result/(10**6))
            simp_f=simplified
            if simplified.endswith('.0'):
                simp_f=simplified.rstrip('.0')
            return simp_f + ' megaohms' + ' ±{}%'.format(tolerance[colors[-1]])
        if result >= 10**3:
            simplified=str(result/(10**3))
            simp_f=simplified
            if simplified.endswith('.0'):
                simp_f=simplified.rstrip('.0')
            return simp_f + ' kiloohms' + ' ±{}%'.format(tolerance[colors[-1]])
        return str(result) + ' ohms'+ ' ±{}%'.format(tolerance[colors[-1]])