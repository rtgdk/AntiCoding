def foo1(string):
    x=0
    w=[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
    print(string)
    substring_score=0
    for i in range(0,len(string)):
        substring_score=substring_score+(ord(string[x]))*w[x]
        x=x+1
    #foo2(substring_score)
    return substring_score

def foo2(program):
    s= len(program)
    print("len",s)
    k= s//13
    total_score = 0
    for i in range(0,k+1):
        print(i)
        total_score+=foo1(program[13*i:13*i+13])
    return total_score

def sumofP(program):
    s = len(program)
    return -3*122*s

def final(program):
    total_score=foo2(program)
    sumP = sumofP(program)
    fractional_score=total_score/sumP
    final_score= 100*fractional_score
    return final_score

a=final("{int i=5,b=++i\n,print(b)}")
print(a)
# print(k)
# while k != 0:
#     string=[]
#     c=0
#     i=c*10 +1
#     while i%10 != 0:
#       string.append(n[i-1])
#       i=i+1
#       if (i%10 !=0 and k!=0):
#           c+=1
#     foo1(string)
#
# final
# a=n[0:10]
#
# print(a)
