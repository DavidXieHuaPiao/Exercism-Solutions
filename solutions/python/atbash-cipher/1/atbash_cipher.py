abc= 'abcdefghijklmnopqrstuvwxyz'

def encode(plain_text):
        ciphered = []
        
        for i in plain_text.replace(' ', '').replace(',', '').replace('.', ''):
                if i.lower() in abc:
                        ciphered.append(abc[-(abc.index(i.lower())+1)])
                else:
                        ciphered.append(i)
        count = 0           
        for i in range (len(ciphered)//5):
                ciphered.insert(5*(count+1) + count, " ")
                count+=1
        return ("".join(ciphered)).strip()


def decode(ciphered_text):
        
        return encode(ciphered_text).replace(' ', '')