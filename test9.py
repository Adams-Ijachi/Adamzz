
alphabets = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m",
             14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y",
             26: "z"}
punct = {1: "!", 2: "?", 3: ",", 4: ".", 5: " ", 6: ";", 7: "'", 8: "\'"}
user  = [18, 12312, 171,763, 98423, 1208, 216,11,500,18,241,0,32,20620,27,10]
mode = "up"
remainder = 0
for numbers in user:
    if mode != "pun":
        remainder = numbers % 27

        if mode == "up":
            if remainder == 0:
                mode = "low"
                continue
            print(alphabets[remainder].upper(),end="")
    if mode == "low":

        if remainder == 0 :
                mode = "pun"
                continue
        print(alphabets[remainder],end="")
    if mode == "pun":
        remainder = numbers % 9
        if remainder == 0:
            mode = "up"
            continue
        print(punct[remainder],end="")






