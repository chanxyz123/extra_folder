limit = int(raw_input("enter limit"))
a = [True] * (limit+1)                          # Initialize the primality list
a[0] = a[1] = False
for (i, isprime) in enumerate(a):
    if isprime:
        # yield i
        for n in xrange(i*i, limit+1, i):     # Mark factors non-prime
            a[n] = False
count=0
for x in xrange(2,limit+1):
    if a[x]==True:
        count+=1
        print x
print count