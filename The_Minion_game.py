def minion_game(string):
    # your code goes here
    k=0
    s1=0
    a="AEIOU"
    for i in range(len(string)):
        if string[i] in a:
            k+=len(string)-i
        else:
            s1+=len(string)-i
    if k>s1:
        print("Kevin",k)
    elif s1>k:
        print("Stuart",s1)
    else:
        print("Draw")
   
if __name__ == '__main__':
    s = input()
    minion_game(s)