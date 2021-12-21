if __name__ == '__main__':
    list1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name, score])
    second_highest = sorted(set([score for name, score in list1]))[1]
print('\n'.join(sorted([name for name, score in list1 if score == second_highest])))