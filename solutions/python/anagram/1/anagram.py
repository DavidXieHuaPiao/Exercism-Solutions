def find_anagrams(word, candidates):
    anagrams=[]
    for cand in candidates:
        if sorted(word.lower()) == sorted(cand.lower()) and word.lower()!= cand.lower():
            anagrams.append(cand)
    return anagrams