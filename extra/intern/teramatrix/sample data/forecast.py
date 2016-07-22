import csv
import statistics
import math

# from pip._vendor.distlib.compat import raw_input

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
with open("H 4.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        A.append(float(row['TESTING PARAMETERS']))
        B.append(float(row['POWER SUPPLY VOLTAGE']))
        C.append(float(row['CURRENT']))
        D.append(float(row['FREQUENCY']))
        E.append(float(row['NOISE LEVEL']))
        F.append(float(row['OPERATING VOLTAGE RANGE']))

# print (A)

A_avg = statistics.mean(A)
B_avg  = statistics.mean(B)
C_avg  = statistics.mean(C)
D_avg  = statistics.mean(D)
E_avg  = statistics.mean(E)
F_avg  = statistics.mean(F)

A_dev = statistics.stdev(A)
B_dev = statistics.stdev(B)
C_dev = statistics.stdev(C)
D_dev = statistics.stdev(D)
E_dev = statistics.stdev(E)
F_dev = statistics.stdev(F)

AA=[]
BB=[]
CC=[]
DD=[]
EE=[]
FF=[]
AB=[]
AC=[]
AD=[]
AE=[]
AF=[]

a_b = 0
a_a = 0
a_c = 0
a_d = 0
a_e = 0
a_f = 0
b_b=0
c_c=0
d_d=0
e_e=0
f_f=0

A.sort()
B.sort()
C.sort()
D.sort()
E.sort()
F.sort()
# print (len(A))
if len(A)%2==0:
    med_A = A[int(len(A)/2)]+A[int(len(A)/2)+1]
    med_B = B[int(len(A)/2)]+B[int(len(A)/2)+1]
    med_C = C[int(len(A)/2)]+C[int(len(A)/2)+1]
    med_D = D[int(len(A)/2)]+D[int(len(A)/2)+1]
    med_E = E[int(len(A)/2)]+E[int(len(A)/2)+1]
    med_F = F[int(len(A)/2)]+F[int(len(A)/2)+1]
else:
    y = int((len(A)+1)/2)
    med_A = A[y]
    med_B = B[y]
    med_C = C[y]
    med_D = D[y]
    med_E = E[y]
    med_F = F[y]

for x in range(0,len(A)):
    # AB.append(A[x]*B[x])
    # AC.append(A[x]*C[x])
    # AD.append(A[x]*D[x])
    # AE.append(A[x]*E[x])
    # AF.append(A[x]*F[x])
    # AA.append(A[x]*A[x])
    # BB.append(B[x]*B[x])
    # CC.append(C[x]*C[x])
    # DD.append(D[x]*D[x])
    # EE.append(E[x]*E[x])
    # FF.append(F[x]*F[x])
    a_b += ((A[x]-med_A)*(B[x]-med_B))
    a_c += ((A[x]-med_C)*(C[x]-med_C))
    a_d += ((A[x]-med_D)*(D[x]-med_D))
    a_e += ((A[x]-med_E)*(E[x]-med_E))
    a_f += ((A[x]-med_F)*(F[x]-med_F))
    a_a += ((A[x]-med_A)*(A[x]-med_A))
    b_b += (B[x]-med_B)*(B[x]-med_B)
    c_c += (C[x]-med_C)*(C[x]-med_C)
    d_d += (D[x]-med_D)*(D[x]-med_D)
    e_e += (E[x]-med_E)*(E[x]-med_E)
    f_f += (F[x]-med_F)*(F[x]-med_F)

# print(AB)

# r_ab = (statistics.mean(AB)-(statistics.mean(A)*statistics.mean(B))) / math.sqrt((statistics.mean(AA)-(A_avg*A_avg))-(statistics.mean(BB)-(B_avg*B_avg)))
# r_ac = (statistics.mean(AC)-(statistics.mean(A)*statistics.mean(C))) / math.sqrt((statistics.mean(AA)-(A_avg*A_avg))-(statistics.mean(CC)-(C_avg*C_avg)))
# r_ad = (statistics.mean(AD)-(statistics.mean(A)*statistics.mean(D))) / math.sqrt((statistics.mean(AA)-(A_avg*A_avg))-(statistics.mean(DD)-(D_avg*D_avg)))
# r_ae = (statistics.mean(AE)-(statistics.mean(A)*statistics.mean(E))) / math.sqrt((statistics.mean(AA)-(A_avg*A_avg))-(statistics.mean(EE)-(E_avg*E_avg)))
# r_af = (statistics.mean(AF)-(statistics.mean(A)*statistics.mean(F))) / math.sqrt((statistics.mean(AA)-(A_avg*A_avg))-(statistics.mean(BB)-(F_avg*F_avg)))

# print(r_ab)
# b_ab = (r_ab*B_dev)/A_dev
# b_ac = (r_ac*C_dev)/A_dev
# b_ad = (r_ad*D_dev)/A_dev
# b_ae = (r_ae*E_dev)/A_dev
# b_af = (r_af*F_dev)/A_dev
# print(B_dev)
# print(A_dev)


b_ab = (a_b/len(A)-1)/(A_dev*A_dev)
b_ac = (a_c/len(A)-1)/(A_dev*A_dev)
b_ad = (a_d/len(A)-1)/(A_dev*A_dev)
b_ae = (a_e/len(A)-1)/(A_dev*A_dev)
b_af = (a_f/len(A)-1)/(A_dev*A_dev)

b_ab1 = a_b/a_a
b_ac1= a_c/a_a
b_ad1 = a_d/a_a
b_ae1 = a_e/a_a
b_af1 = a_f/a_a


a_ab = B_avg - (b_ab * A_avg)
a_ac = C_avg - (b_ac * A_avg)
a_ad = D_avg - (b_ad * A_avg)
a_ae = E_avg - (b_ae * A_avg)
a_af = F_avg - (b_af * A_avg)

a_ab1 = B_avg - (b_ab1 * A_avg)
a_ac1 = C_avg - (b_ac1 * A_avg)
a_ad1 = D_avg - (b_ad1 * A_avg)
a_ae1 = E_avg - (b_ae1 * A_avg)
a_af1 = F_avg - (b_af1 * A_avg)

x = float(input("Enter value"))

# print(b_ab)
# print(a_ab)
y1 = abs((b_ab*x)+a_ab)
y2 = abs((b_ac*x)+a_ac)
y3 = abs((b_ad*x)+a_ad)
y4 = abs((b_ae*x)+a_ae)
y5 = abs((b_af*x)+a_af)

print (y1)
print (y2)
print (y3)
print (y4)
print (y5)