from Podatak import Electricity

with open('StrujaFile.txt') as f:
    contents = f.readlines()
    count = len(contents)
    i = 0

    while 1 > 0:
        if i == count:
            break
        one = Electricity(personal_id=contents[i], monthly_value=contents[i + 1], month=contents[i + 2])
        print(one)
        i = i+3


