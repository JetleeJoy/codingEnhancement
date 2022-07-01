# find how many times the string 'hsl' can be made out from a given random input string

query = ['h','s','l']
string = list(input("Enter the string_ "))
flag = 0
for i in string:
    if i == query[0]:
        for j in string[string.index(i)::]:
            if j == query[1]:
                for k in string[string.index(j)::]:
                    if k == query[2]:
                        flag +=1
print("In the input string, the word hsl can be found ",flag," times !")
