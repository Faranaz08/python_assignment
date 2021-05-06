a=int(input("test1="))
b=int(input("test2="))
c=int(input("test3="))
avg=(a+b+c)/2
print("the avg of tests is="+str(avg))
#to take avg of best 2 out of 3


big1 =a if a>b else b
print(str(big1))
big2= b if a>c else c
print(str(big2))

AVG=(big1+big2)/2
print("Average of best of 2 out of 3 is :"+str(AVG))






