def rows(letter):
        result=[]
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sep = ' '
        for i in (abc[:abc.index(letter)+1]+(abc[:abc.index(letter)])[::-1]):
                times=len(abc[:abc.index(letter)])-abc.index(i)
                mid_times = 1+2*(abc.index(i)-1)
                line = (sep*times+i)
                if i == 'A':
                        line+=sep*times
                else:
                        line+=sep*mid_times+i+sep*times
                result.append(line)
                
        return result