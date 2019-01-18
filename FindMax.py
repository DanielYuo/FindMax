def find_max(lis):
    ma = 0
    for i in lis:
        if ma == 0:
            ma = i
        elif i > ma:
            ma = i 
    return ma