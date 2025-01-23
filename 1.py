def main(s:str):
    if s[0] == 'R':
        print('Yes')
    elif s[1] == 'R' and s[0] == 'S':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    s = input()
    main(s)