def gross_pay(h_pay, hours):
  if(hours > 40):
    gross_pay = (h_pay * 40) + 1.5 * h_pay * (hours - 40)
  else:
    gross_pay = h_pay * hours 
  return gross_pay  

h_pay = float(input("What is your hourly pay? "))
hours = int(input("How many hours have you worked? "))

gross_pay = float(gross_pay(h_pay, hours))

print("You've worked ", hours, "hours.")
print("Your hourly rate is: ${:.2f}" .format(h_pay))
print("Your gross pay is: ${:.2f}" .format(gross_pay))
