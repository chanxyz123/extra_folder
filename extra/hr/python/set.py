temp = int(raw_input())
temp1 = raw_input()
t = temp1.split(" ")
new1 = list(map(int,t)) 
temp2 = int(raw_input())
temp3 = raw_input()
t1 = temp3.split(" ")
new2 = list(map(int,t1))
print new1 +new2
total1 = (set(new1)).difference(set(new2))
total2 = (set(new2)).difference(set(new1))
total1 = list(total1)
total2 = list(total2)
print total1
print total2
total = total1+total2
print total
total.sort()
for i in range(0,len(total)):
    print total[i]  