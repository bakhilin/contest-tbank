def f(k:int, arr:list) -> None:
    p = []
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            p.append([arr[i], arr[j]])
    
    sum_el = 0
    for value in p:
        sum_el += sum(value) ** k
    
    print(sum_el % 998244353)


def main() -> None:
    _, k = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(1,k+1):
        arr.sort()
        f(i, arr)


if __name__ == '__main__':
    main()