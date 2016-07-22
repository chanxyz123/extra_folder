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
with open("H 2.csv") as file:
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
    a_b += ((A[x]-A_avg)*(B[x]-B_avg))
    a_c += ((A[x]-A_avg)*(C[x]-C_avg))
    a_d += ((A[x]-A_avg)*(D[x]-D_avg))
    a_e += ((A[x]-A_avg)*(E[x]-E_avg))
    a_f += ((A[x]-A_avg)*(F[x]-F_avg))
    a_a += ((A[x]-A_avg)*(A[x]-A_avg))
    b_b += (B[x]-B_avg)*(B[x]-B_avg)
    c_c += (C[x]-C_avg)*(C[x]-C_avg)
    d_d += (D[x]-D_avg)*(D[x]-D_avg)
    e_e += (E[x]-E_avg)*(E[x]-E_avg)
    f_f += (F[x]-F_avg)*(F[x]-F_avg)

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


b_ab = a_b/a_a
b_ac = a_c/a_a
b_ad = a_d/a_a
b_ae = a_e/a_a
b_af = a_f/a_a

a_ab = B_avg - (b_ab * A_avg)
a_ac = C_avg - (b_ac * A_avg)
a_ad = D_avg - (b_ad * A_avg)
a_ae = E_avg - (b_ae * A_avg)
a_af = F_avg - (b_af * A_avg)

x = float(input("Enter value"))

# print(b_ab)
# print(a_ab)
y1 = abs((b_ab*x)+a_ab)
y2 = abs((b_ac*x)+a_ac)
y3 = abs((b_ad*x)+a_ad)
y4 = abs((b_ae*x)+a_ae)
y5 = abs((b_af*x)+a_af)

S_ab =math.sqrt(b_b-(b_ab*a_b))
S_ac =math.sqrt(c_c-(b_ac*a_c))
S_ad =math.sqrt(d_d-(b_ad*a_d))
S_ae =math.sqrt(e_e-(b_ae*a_e))
S_af =math.sqrt(f_f-(b_af*a_f))

S_ab = S_ab/math.sqrt(len(A)-2)
S_ac = S_ac/math.sqrt(len(A)-2)
S_ad = S_ad/math.sqrt(len(A)-2)
S_ae = S_ae/math.sqrt(len(A)-2)
S_af = S_af/math.sqrt(len(A)-2)


SE_bb = S_ab/a_a
SE_bc = S_ac/a_a
SE_bd = S_ad/a_a
SE_be = S_ae/a_a
SE_bf = S_af/a_a

SE_ab = S_ab*math.sqrt((1/len(A))+((A_avg*A_avg)/a_a))
SE_ac = S_ac*math.sqrt((1/len(A))+((A_avg*A_avg)/a_a))
SE_ad = S_ad*math.sqrt((1/len(A))+((A_avg*A_avg)/a_a))
SE_ae = S_ae*math.sqrt((1/len(A))+((A_avg*A_avg)/a_a))
SE_af = S_af*math.sqrt((1/len(A))+((A_avg*A_avg)/a_a))

# print (B_avg)

e_ab = SE_ab*abs(y1-B_avg)+SE_bb
e_ac = SE_ac*abs(y2-C_avg)+SE_bc
e_ad = SE_ad*abs(y3-D_avg)+SE_bd
e_ae = SE_ae*abs(y4-E_avg)+SE_be
e_af = SE_af*abs(y5-F_avg)+SE_bf

# print (y1+(e_ab))
# print (y1-(e_ab))
# print (y2+(e_ac))
# print (y2-(e_ac))
# print (y3+(e_ad))
# print (y3-(e_ad))
# print (y4+(e_ae))
# print (y4-(e_ae))
# print (y5+(e_af))
# print (y5-(e_af))
print (y1)
print (y2)
print (y3)
print (y4)
print (y5)