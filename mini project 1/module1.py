user=input("enter the name")
monthly_income=int(input("enter the income"))
food=int(input("enter the food expense"))
travel_expenses=int(input("enter the travel expenses"))
study_materials=int(input("enter the study materials expenses"))
internet=int(input("enter the internet expenses"))
other_expenses=int(input("enter the other expenses"))
total_expenses=food+travel_expenses+study_materials+internet+other_expenses
remaining_balance=monthly_income-total_expenses
saving_rate=(remaining_balance/monthly_income)*100
print(f"Student:{user} \nMonthly income:{monthly_income} \nFood:{food} \nTravel:{travel_expenses} \nStudy materials:{study_materials} \nmobile/internet:{internet} \nOther:{other_expenses} \nTotal expenses:{total_expenses} \nRemaining balance:{remaining_balance} \nSavings rate:{saving_rate}")