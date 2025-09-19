def recite(start_verse, end_verse):
        ordinal_numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
        poem= " twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, a Partridge in a Pear Tree"        
        poem_organized = list(poem.split(","))
        poem_organized.reverse()
        full_text=[]
        for i in range(start_verse, end_verse+1):
                first_part = list("On the number day of Christmas my true love gave to me:".split())
                first_part[2] = ordinal_numbers[i-1]
                text1= " ".join(first_part)
                
                second_part = poem_organized[0:i]
                if i>1:
                        second_part[0]= " and" + second_part[0]
                second_part.reverse()   
                text2= ",".join(second_part) 
                full_text.append(text1+text2+".")       
        return full_text