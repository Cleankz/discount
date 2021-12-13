def MaximumDiscount(N, price):
    if N == 3:
        min = price[0]
        for i in range(len(price)):
            if min >= price[i]:
                min = price[i]
        return min
    elif N > 3:
        xchange = True 
        while(xchange):
            xchange = False
            for i in range(len(price)-1):
                if price[i] < price[i+1]:
                    price[i], price[i+1] = price[i+1], price[i]
                    xchange = True
        free_item = N // 3
        min_sum = 0
        for i in range(free_item):
            min = price[0]
            for j in range(3):
                if len(price) == 3:
                    min =price[2]
                    break
                if j != 6 or j != 3 and min >= price[j]:
                    min = price[j]
            min_sum = min_sum + min
            del price[0:3]
            if len(price) < 2:
                break 
        return min_sum
    elif N < 3:
        min_sum = 0
        return min_sum
