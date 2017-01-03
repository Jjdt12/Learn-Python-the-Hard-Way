def LetterChanges(str):

    var = ""

    for i in str:
        if i == " ":
            var += i
        else:
            var += chr(ord(i)+1)


    var = list(var)
    for i in var:
        if i == "b":
            var[i] = var[i].upper()

    return var

print LetterChanges("testing aaaaaa test aaaa")
