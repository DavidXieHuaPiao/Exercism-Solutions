def translate(text):
    splitted_text = text.split()
    vowels="aeiou"
    phrase=""
    for x in splitted_text:
        if x[0] in vowels or x.startswith(("xr", "yt")):
            phrase = phrase+x+"ay"+" "
        else:
            new=x
            counter=0
            for i in x:
                if x[counter:counter+2] == "qu":
                    new+="qu"
                    counter+=2
                    break
                if i not in vowels and (i!= "y" or x[0]=="y"):
                    new+=i
                    counter+=1
                else:
                    break
            phrase = phrase + new[counter:]+"ay"+" "
    return phrase.strip()
                
            