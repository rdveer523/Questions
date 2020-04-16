n1 = int(input("Total distance in LIGHT YEARs : "))

lss1 = 299792 #light speed in km/s
lsm1 = lss1 * 60 #seconds to one minute
lsh1 = lsm1 * 60 #minutes to one hour
lsd1 = lsh1 * 24 #per day
lsy1 = lsd1 * 365 #per year
lsly1 = lsd1 * 366 #per leap year

print("Ligh speed in KM/s : ",lss1,'\n',
      "Light speed in a MINUTE : ",lsm1,'\n',
      "Light speed in a HOUR : ",lsh1,'\n',
      "Light speed in a DAY : ",lsd1,'\n',
      "Light speed in a YEAR : ",lsy1,'\n',
      "Light speed in a LEAP YEAR : ",lsly1,'\n', 
      )

print("Light speed in {} years is : ".format(n1), n1*lsy1)
