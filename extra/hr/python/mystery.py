def array():
	arr = []
	for x in xrange(97,123):
		arr.append([x,chr(x)])
	return arr
def function(S):
	count = 0
	j=0
	if (len(S)%2)==0:
		i=len(S)/2
		while True:
			if j<i:
				arr = array()
				if ord(S[i-j-1]) > ord(S[i+j]):
					k=0
					while True:
						if k<=ord(S[i-j-1])-97:
							if arr[ord(S[i-j-1])-97][1] == arr[ord(S[i+j])-97][1]:
								j=j+1
								break
							else:
								arr[ord(S[i-j-1])-97] = arr[ord(S[i-j-1])-1-97]
								k=k+1
								count  = count +1
				elif ord(S[i-j-1]) < ord(S[i+j]):
					k = 0
					while True:
						if k<=ord(S[i+j])-97:
							if arr[ord(S[i-j-1])-97][1] == arr[ord(S[i+j])-97][1]:
								j=j+1
								break
							else:
								arr[ord(S[i+j])-97] = arr[ord(S[i+j])-1-97-k]
								k =k+1
								count  = count +1
				else:
					j= j+1
					continue
			else:
				break
	else:
		i=((len(S)+1)/2)
		while True:
			if j<i-1:
				arr = array()
				if ord(S[i-j-2]) > ord(S[i+j]):
					k=0
					while True:
						if k<=ord(S[i-j-2])-97:
							if arr[ord(S[i-j-2])-97][1] == arr[ord(S[i+j])-97][1]:
								j=j+1
								break
							else:
								arr[ord(S[i-j-2])-97] = arr[ord(S[i-j-2])-1-97-k]
								k =k+1
								count  = count +1
				elif ord(S[i-j-2]) < ord(S[i+j]):
					k=0
					while True:
						if k<=ord(S[i+j])-97:
							if arr[ord(S[i-j-2])-97][1] == arr[ord(S[i+j])-97][1]:
								j=j+1
								break
							else:
								arr[ord(S[i+j])-97] = arr[ord(S[i+j])-1-97-k]
								k =k+1
								count  = count +1
				else:
					j=j+1
					continue
			else:
				break
	return count
test_case =  int(raw_input())
for x in xrange(0,test_case):
	S = raw_input()
	print function(S)