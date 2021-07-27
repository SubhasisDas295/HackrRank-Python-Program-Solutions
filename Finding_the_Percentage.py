if __name__ == '__main__':
    n = int(input())
    marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        scores=sum(scores)/3
        marks[name] = scores
    a=input()

    print('%.2f'% marks[a])