def main(numbers:list, n, x, y, z):
    dividers = {x:1000,y:1000,z:1000}
    count = 0
    for i in x,y,z:
        for j in range(len(numbers)):
            for k in range(1,100):
                if (numbers[j]+k) % i == 0:
                    if k == 1:
                        dividers[i] = k
                    else: 
                        if dividers[i] > k:
                            dividers[i] = k

    times = dict()

    for key, value in dividers.items():
        for n in numbers:
            if (n + value) % key == 0:
                times[n] = value
    

    print(sum(times.values()))

if __name__ == '__main__':
    n, x, y, z = map(int, input().split())
    numbers = list(map(int, input().split()))
    main(numbers, n,x,y,z)
    
        