def parse_int(string):
    a = 0
    number = 0
    dizionario = {
        "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, 
        "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, 
        "nineteen":19, "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90, 
        "hundred":100, "thousand":1000, "million":1000000 
    }

    parole = string.replace("-", " ")
    parole = parole.split()


    for i in parole:
        
        if i in dizionario:
            if i == "hundred":
                a *= 100
            elif i in ["thousand", "million"]:
                number += a * dizionario[i]
                a = 0
            else:
                a += dizionario[i]
        
    number += a
    return number

#print(parse_int("two hundred thousand three hundred forty-six")) - insert this string in your file
