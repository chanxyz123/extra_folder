def anagram(s):
    l = len(s)
    if l%2!=0:
        return -1
    else:
        arr1 = []
        arr2 = []
        for x in range(0,26):
            arr1.append(0)
            arr2.append(0)
        i=0
        print s[:(l/2)]
        while i<l/2:
            arr1[ord(s[i])-97]+=1
            i+=1
        print arr1
        print s[(l/2):]
        j=l/2
        while j<l:
            arr2[ord(s[j])-97]+=1
            j+=1
        print arr2
        count = 0
        for x in range(0,26):
            if arr2[x]!=0:
                if (arr2[x]-arr1[x])>=0:
                    count+=arr2[x]-arr1[x]
        return count
test_case =  int(raw_input())
for x in range(0,test_case):
    s = raw_input()
    print anagram(s)