def swap_case(s):
    temp=[]
    l=list(s)
    for i in s:
        x=""
        if i.isupper():
            x+=chr(ord(i)+32) 
        elif i.islower():
            x+=chr(ord(i)-32)
        else:
            temp.append(i)
        temp.append(x)
    x="".join(temp)
    return x 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)