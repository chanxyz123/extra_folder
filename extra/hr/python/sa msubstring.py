n = raw_input()
total = 0
for x in range(0,len(n)):
    for y in range(0,len(n)-x):
        total+=int(n[y:y+x+1])
print total%(1000000000+7)