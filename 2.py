def main(money_per_day:list) -> None:
    for i in range(len(money_per_day)):
        count = 0
        money_one_day = money_per_day[i]
        if 2**0 + 2**1 + 2**2 > money_one_day:
            print(-1)
        else:
            for j1 in range(100):
                for j2 in range(j1+1, 100):
                    for j3 in range(j2+1, 100):
                        count = 2**j1 + 2**j2 + 2**j3
                        if count == money_one_day or count == money_one_day - 1:
                            break
                    if count == money_one_day or count == money_one_day - 1:
                        break
                if count == money_one_day or count == money_one_day - 1:
                    print(count)
            

if __name__ == '__main__':
    n = int(input())
    money_per_day = [int(input()) for i in range(n)]
    main(money_per_day)