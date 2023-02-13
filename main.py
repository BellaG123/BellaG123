def convertToKilometers(miles):
   kilometers=miles*1.60934
   return kilometers
while True:
  try:
   miles=float(input("Enter miles:"))
   break 
  except ValueError:
   print("No valid input. Please try again.")

kilometers = convertToKilometers(miles)
print("%0.3f miles = %0.3f kilometers" %(miles,kilometers))
    


  