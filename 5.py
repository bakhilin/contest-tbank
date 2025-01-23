def main():
    n, s = map(int, input().split())
    l = list(map(int, input().split()))
    
    total_parts = 0
    
    for l in range(n):
        current_sum = 0
        for r in range(l, n):
            current_sum += l[r]  
            total_parts += current_sum // s
            
    print(total_parts)

if __name__ == '__main__':
    main()