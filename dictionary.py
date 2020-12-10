#allow the user to input the date
date=raw_input("Please enter the date in the format of dd/mm/year: ")

#split the strings
date=date.split('/')

#day
day=date[:2]

#create a dictionary for the months
monthDict={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
#month
month=date[3:5]
if month in monthDict:
    for key,value in monthDict:
        month=value

#year
year=date[4:]

#print the result in the required format
print day, month, "," , year