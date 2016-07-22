def check(s):
    if len(s)%2!=0:
    	print len(s)
        return "NO"
    else:
	    for x in range(0,len(s)/2):
	    	if ord(s[x])==40:
	    		print "hello"
	    		if ord(s[x])!=ord(s[len(s)-1-x])-1:
	    			print "helo1"
	    			return "NO"
	    	else:
		        if ord(s[x])!=ord(s[len(s)-1-x])-2:
		            print "hellooo", ord(s[x]),ord(s[len(s)-1-x])
		            return "NO"
    return "YES"
test_case = int(raw_input())
for x in range(0,test_case):
    s = raw_input()
    s= list(s)
    print check(s)