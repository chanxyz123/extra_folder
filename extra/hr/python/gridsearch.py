def check(i,j,G,P):
	while i<len(P):
		if P[i] in G[j]:
			return check(i+1,j+1,G,P)
		else:
			return "NO"
	return "YES"

t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
    j=0
    store = []
    while j<len(G):
    	i=0   
        if P[0] in G[j]:
            if check(i+1,j+1,G,P)=="NO":
                j= j+1
                store.append("NO")
                continue
            else:
                # check(i+1,j+1,G,P)
                store.append("YES")
                break
        else:
            j = j+1
            continue
    if (store.pop())=="YES":
    	print "YES"
    else:
    	print "NO"