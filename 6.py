def main(homes:list):
    for i in range(len(homes)-1):
        for j in range(i+1, len(homes)):
            if homes[i] == homes[j]:
                homes.pop(j)

    print(len(homes) // 3)


if __name__ == '__main__':
    n = int(input())
    homes = [list(map(int,input().split())) for i in range(n)]
    main(homes)