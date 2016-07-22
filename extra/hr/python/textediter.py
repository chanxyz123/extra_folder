n  = int(raw_input())
string = ""
store = []
for x in range(0,n):
    # print string
    s = raw_input().split()
    if int(s[0])==1:
        string+= s[1]
        store.append([1,s[1]])
        s[1] = list(s[1])
    elif int(s[0])==2:
        re = string[-int(s[1]):]
        # print "re =" + re
        string = string[:-int(s[1])]
        store.append([2,re])
    elif int(s[0])==3:
        print string[int(s[1])-1]
    elif int(s[0])==4:
        # print string
        # print store,len(store)
        if store[len(store)-1][0]==1:
            # print "hello"
            string =  string[:-len(store[len(store)-1][1])]
            store.remove(store[len(store)-1])
        elif store[len(store)-1][0]==2:
            # print "hellllll"
            string+=store[len(store)-1][1]
            store.remove(store[len(store)-1])
        # print string,store