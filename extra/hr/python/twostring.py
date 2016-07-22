def array():
    a = []
    for x in range(0,26):
        a.append(0)
    return a
def palindrome(s):
    for x in range(0,len(s)):
        if s[x]!=s[len(s)-1-x]:
            return 0
    return 1
def length(s1,s2):
    a1 = array()
    a2 = array()
    for x in range(0,len(s1)):
        a1[ord(s1[x])-97]+=1
    for x in range(0,len(s2)):
        a2[ord(s2[x])-97]+=1
    for x in range(0,26):
        if a1[x]%2!=0:
            s1 = s1.replace(chr(97+x),"")
        if a2[x]%2!=0:
            s2 = s2.replace(chr(97+x),"")
    return len(s1)+len(s2)
    
test_case =int(raw_input())
for x in range(0,test_case):
    s1= raw_input()
    s2= raw_input()
    print length(s1,s2)