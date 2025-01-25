

def count_letters(s: str) -> str:
    if len(s) == 0:
        return '0' 
    elif len(s) == 1:
        return s[0] + str(1)
    else:
        final_str = ''
        count = 1
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                count += 1
            else:
                final_str += s[i] + str(count)
                if i == len(s) - 2: 
                    final_str += s[i+1] + str(1)
                count = 1

        return final_str

def test():
    s1 = 'AAABBC'
    s2 = 'ABC'
    s3 = 'A'
    s4 = 'CCCCBFFFA'
    s5 = ''
    
    assert count_letters(s1) == 'A3B2C1'
    assert count_letters(s2) == 'A1B1C1'
    assert count_letters(s3) == 'A1'
    assert count_letters(s4) == 'C4B1F3A1'
    assert count_letters(s5) == '0'


if __name__ == '__main__':
    
    test()