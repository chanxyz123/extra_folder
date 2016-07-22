def palindrome(s):
    for x in range(0,(len(s)/2)+1):
        if s[x]!=s[len(s)-1-x]:
            return 0
    return 1
def index(s):
    if palindrome(s)==1:
        return -1
    else:
        for x in range(0,(len(s)/2)+1):
            if s[x]!=s[len(s)-1-x]:
                s1 = s
                s1 = list(s1)
                del s1[x]
                s1 = ''.join(s1)
                if palindrome(s1)==1:
                    return x
                else:
                    return len(s)-1-x
test_case = int(raw_input())
for x in range(0,test_case):
    s = raw_input()
    print index(s)
