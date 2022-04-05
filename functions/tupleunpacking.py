stkprice=[('appl',100),('msft',200)]
for ticker,price in stkprice:
    print(price+(.1*price))

wrk_hours=[('abby',100),('billy',400),('cassie', 800)]
def empcheck(wrk_hours):
    current_max=0
    emp_of_month=''

    for employee,hours in wrk_hours:
        if hours>current_max:
            current_max=hours
            emp_of_month=employee
        else:
            pass
    return (emp_of_month,current_max)    
print(empcheck(wrk_hours))           
name,hours=empcheck(wrk_hours)
print(name)
print(hours)