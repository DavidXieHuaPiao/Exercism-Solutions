def encode(numbers):
        binaries=[]
        for i in numbers:
                binaries.append(bin(int(str(i)))[2:])
                
        everyone = []
        
        for binary in binaries:
                groups = []
                count=0
                while count<len(binary):
                        new_add= (binary[::-1][count:count+7])
                        new_add+='0'*(7-len(new_add))
                        if count != 0:
                                new_add+='1'
                        else:
                                new_add+='0'
                        groups.append(new_add[::-1])
                        count+=7
                groups.reverse()
                everyone+=groups
        
        encoded = []
        
        for i in everyone:
                encoded.append(int(i, 2))
                
        return encoded

def decode(bytes_):
        binaries = []
        sub_bin=[]
        result = []
        for index, hex in enumerate(bytes_):
                new_bin = bin(int(str(hex))).lstrip('0b')
                if len(new_bin) == 8:
                        if index == len(bytes_)-1:
                                raise ValueError("incomplete sequence")
                        new_bin=new_bin[1:]
                        sub_bin.append(new_bin)
                elif len(new_bin) < 8:
                        new_bin = '0'*(7-len(new_bin)) + new_bin
                        sub_bin.append(new_bin)
                        binaries.append(sub_bin)
                        sub_bin=[]
                        
        for binary in binaries:
                result.append(int("".join((binary)), 2))

        return result