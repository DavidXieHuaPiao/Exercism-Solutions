def convert(input_grid):
        result=""
        if len(input_grid)%4!=0:
                raise ValueError("Number of input lines is not a multiple of four")
        for row in input_grid:
                if len(row)%3!=0:
                        raise ValueError("Number of input columns is not a multiple of three")
        result=""
        c=[("   "), (" _ "), ("  |"), ("|_|"), (" _|"), ("|_ "), ("| |")]
        count=0
        for i in range(len(input_grid)//4):
                for i_col_index in range(len(input_grid[0])//3):
                        r1=input_grid[0+count][i_col_index*3:i_col_index*3+3]
                        r2=input_grid[1+count][i_col_index*3:i_col_index*3+3]
                        r3=input_grid[2+count][i_col_index*3:i_col_index*3+3]
                        if r1==c[1]:
                                if r3==c[4]:
                                        if r2 ==  c[4]:
                                                result+='3'
                                                continue
                                        if r2 == c[5]:
                                                result+='5'
                                                continue
                                        if r2 == c[3]:
                                                result+='9'
                                                continue
                                if r3==c[3]:
                                        if r2==c[5]:
                                                result+='6'
                                                continue
                                        if r2==c[3]:
                                                result+='8'
                                                continue
                                        if r2==c[6]:
                                                result+='0'
                                                continue
                                if r2==c[4] and r3==c[5]:
                                        result+='2'
                                        continue
                                if r2==c[2] and r3==c[2]:
                                        result+='7'
                                        continue
                        if r1==c[0] and r3==c[2]:
                                if r2 == c[2]:
                                        result+='1'
                                        continue
                                if r2 == c[3]:
                                        result+='4'
                                        continue
                        result+='?'
                result+=','
                count+=4

                                        
        return result.strip(',')
