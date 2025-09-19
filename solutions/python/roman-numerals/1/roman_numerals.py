def roman(number):
        str_number=str(number)
        order=len(str_number)
        romans_by_order = [('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M'), ('M')]
        text=""
        for i in str_number:
                n=int(i)
                current_unit=romans_by_order[order-1]
                if n==9:
                        text+=current_unit[0]+current_unit[2]
                elif n>=5 and n<=8:
                        text+=current_unit[1]+current_unit[0]*(n-5)
                elif n==4:
                        text+=current_unit[0]+current_unit[1]
                elif n<=3:
                        text+=current_unit[0]*n
                        
                order-=1
                        
        return text