def recite(start_verse, end_verse):
    condition = start_verse==end_verse
    result=[]
    animals = ['fly.', 'spider.', 'bird.', 'cat.', 'dog.', 'goat.', 'cow.', 'horse.']
    base = ["I know an old lady who swallowed a fly.", "I don't know why she swallowed the fly. Perhaps she'll die."]
    continuation = [["It wriggled and jiggled and tickled inside her.", "She swallowed the spider to catch the fly."],
                    ["How absurd to swallow a bird!", "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her."],
                    ["Imagine that, to swallow a cat!", "She swallowed the cat to catch the bird."],
                    ["What a hog, to swallow a dog!", "She swallowed the dog to catch the cat."],
                    ["Just opened her throat and swallowed a goat!","She swallowed the goat to catch the dog."],
                    ["I don't know how she swallowed a cow!","She swallowed the cow to catch the goat."]]
    repetitions = end_verse+1-start_verse
    temp_base=base
    first_assigned=False
    for i in range(repetitions):
        if start_verse==1:
            None
        elif start_verse==8:
            result.append("I know an old lady who swallowed a horse.")
            result.append("She's dead, of course!")
            return result

        else:
            temp_base[0] = temp_base[0][0:-len(temp_base[0].split()[-1])] + animals[start_verse-1]
            if first_assigned:
                temp_base[1]=continuation[start_verse-2][0]
                temp_base.insert(2, continuation[start_verse-2][1])
                
            else:
                temp_base.insert(1, continuation[start_verse-2][0])
                temp_base.insert(2, continuation[start_verse-2][1])
                first_assigned=True
        if condition:
                    count=start_verse-3
                    while count>=0:
                        temp_base.insert(-1, continuation[count][1])
                        count-=1
        for x in temp_base:
            result.append(x)
            
        if i != repetitions-1:
            result.append("")
        start_verse+=1
    return result