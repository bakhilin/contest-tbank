def main(m:int, days:list):
    good_days = []
    for day in days[2:]:
        if day < days[0]:
            good_days.append(days[0] - day) 
        elif day > days[1]:
            good_days.append(day - days[1])
       
    good_days.sort()
    min_sum = 0
    for i in range(m):
        min_sum += good_days[i]
    
    print(min_sum)
    


if __name__ == '__main__':
    _, m = map(int, input().split())
    days = list(map(int, input().split()))
    main(m, days)