def max_toys(prices, rupees):
    prices.sort()
    print len(prices)
    index= 0
    for x in range(0,len(prices)):
        if prices[x]>rupees:
            index = x
            break
    total = 0
    answer = 0
    print index
    print len(prices)
    for x in range(0,index):
        total+=prices[x]
        if total<=rupees:
            # print total
            answer+=1
            # print answer    
        else:
            break
    return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)
