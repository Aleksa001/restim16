from Podatak import Electricity

with open('StrujaFile.txt') as f:
    contents = f.readlines()
    for j in contents:
        if (j % 3 ==0):
            one = Electricity(personal_id=contents[j-2], monthly_value=contents[j-1], month=contents[j])
            print(one)

