#to calculate your current age.
born=int(input("enter your born year"))
current=int(input("enter your current year"))
age=current-born
print("my age is",age)




def findAge(current_date, current_month, current_year, 
			birth_date, birth_month, birth_year): 
	month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
	if (birth_date > current_date): 
		current_month = current_month - 1
		current_date = current_date + month[birth_month-1] 
		
		
	# if birth month exceeds current month, then 
	# donot count this year and add 12 to the 
	# month so that we can subtract and find out 
	# the difference 
	if (birth_month > current_month):		 
		current_year = current_year - 1; 
		current_month = current_month + 12; 
		
	# calculate date, month, year 
	calculated_date = current_date - birth_date; 
	calculated_month = current_month - birth_month; 
	calculated_year = current_year - birth_year; 
	
	# print present age 
	print"Present Age"
	print("Years:", calculated_year, "Months:", 
		calculated_month, "Days:", calculated_date) 
	
# driver code 
current_date = 7
current_month = 12
current_year = 2017
		
# birth dd//mm//yyyy 
birth_date = 16
birth_month = 12
birth_year = 2009

findAge(current_date, current_month, current_year, 
		birth_date, birth_month, birth_year) 
