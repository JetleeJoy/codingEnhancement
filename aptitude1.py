# a string having two parts, a number at front, a valid or invalid word after the number, find out if the length of the second part is same as the 
# number on the first part, if yes , then print true and length of the second part, else print false and lenth of the seccond part
# ex : input :: 3cat, output :: true, 3 

b = input("Enter a string _ ")
cnt = 0
cnt2 = 0
for i in b:
    if i.isdigit():
        cnt +=1
    else:
        cnt2 +=1
        if(cnt2+cnt-1 == cnt):
            break
if cnt!=0:
    d = int(b[0:cnt])
    if(d == len(b[cnt::])):
        print("True ",len(b[cnt::]))
    else:
        print("False ",len(b[cnt::]))
else:
    print("Input case is false")