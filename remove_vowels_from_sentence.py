def disemvowel(string):
    o = list(string)
    t = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in range(len(o)):
        for i in o:
            for ii in t:
                if i in ii:
                    o.remove(i)
                    g = "".join(o)
    return g
print(disemvowel("A common way to deal with this situation is \n to remove all of the vowels from the \n trolls' comments, neutralizing the threat. "))








