def sezar_crypt(step, realtext):
    Outtext = []
    crypttext = []
    uppercase = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for echleter in realtext:
        if echleter in uppercase:
            index=uppercase.index(echleter)
            crypting=(index+ step) % 26
            crypttext.append(crypting)
            newletter=uppercase[crypting]
            Outtext.append(newletter)
        elif echleter in lowercase:
            index=lowercase.index(echleter)
            crypting=(index+ step) % 26
            crypttext.append(crypting)
            newletter=uppercase[crypting]
            Outtext.append(newletter)
        return Outtext
code=sezar_crypt(int(input("enter key : ")) ,input("inter string : "))
code = ''.join(code)
print("Encryped text is ", code)
