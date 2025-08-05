def counter(x, y, garden_par):
        count=0
        
        for ny, nrow in enumerate(garden_par):
                for nx, nelem in enumerate(nrow):
                        if (((ny==y+1 or ny==y-1) and (nx==x-1 or nx==x or nx==x+1)) or (ny==y and (nx==x-1 or nx==x+1))) and nelem=="*":
                                count+=1
                
        
        return count

def annotate(garden):
        for y_pos, row in enumerate(garden):
                if len(row)!=len(garden[y_pos-1]):
                        raise ValueError("The board is invalid with current input.")
                for x_pos, element in enumerate(row):
                        if element == "*":
                                continue
                        if element == " ":
                                count = counter(x_pos, y_pos, garden)
                                if count != 0:
                                        garden[y_pos] = garden[y_pos][:x_pos] + str(count) + garden[y_pos][x_pos+1:]
                                continue
                        raise ValueError("The board is invalid with current input.")
        
        return garden