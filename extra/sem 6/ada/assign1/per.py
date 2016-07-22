def permute1(start, rest):
    res = []
    if len(rest) <= 1:
        res += [start + rest, rest + start]
        print res
    else:
        for i, c in enumerate(rest):
            s = rest[:i] + rest[i+1:]
            for perm in permute1(c, s):
                res += [start + perm]
                print res
    return list(set(res))
n =  int(raw_input())
a=''
for x in xrange(1,n+1):
	a+=str(x)
print permute1('',a)