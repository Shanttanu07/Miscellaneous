# # annual_salary = int(input("Type your annual salary"))
# # total_cost = int(input("cost of your dream home?"))
# # semi_annual_raise= float(input("your semi annual raise is?"))
# # time = int(input("After how many months you need to buy your dream home?"))

# annual_salary = int(100000)
# total_cost = int(1000000)
# semi_annual_raise= float(0.07)
# time = int(36)

# down_payment = float(total_cost/4)
# monthly_salary = float(annual_salary/12)
# high=1
# low=0
# fraction_saved = float((high+ low)/2)
# guesses=0
# savings=0 
# for i in range(time):
#     if i/6- int(i/6)==0:
#         monthly_salary += monthly_salary*semi_annual_raise 
#     savings += savings/300 + monthly_salary
# maximum_savings= savings
# if maximum_savings<= down_payment:
#     print("You are out of mind")
# else:
#     savings=0
#     while abs(down_payment-savings) >100:
#         savings=0
#         monthly_salary=float(annual_salary/12)
#         for i in range(1,time+1):
#             if i/6- int(i/6)==0:
#                 monthly_salary += monthly_salary*semi_annual_raise 
#             savings += savings/300 + monthly_salary*fraction_saved
#         if down_payment-savings>0:
#             low= fraction_saved
#             fraction_saved= float((high+low)/2)
#         else:
#             high= fraction_saved
#             fraction_saved= float((high+low)/2)
#         guesses+=1
#     print("You need to save approximately ",fraction_saved," fraction of your salary")
#     print(guesses)

a=int(input("value of a is"))
b=int(input("value of b is"))
def f(a,b):
    
    
f(a,b)
print(a)



