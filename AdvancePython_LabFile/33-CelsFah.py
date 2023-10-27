#33-WAP that converts a list of temperatures in celsius into fahrenheit using map() function
cel=[23,11,15,0,37,12.3,-5]
def celsToFah(c):
    f=(c*(9/5))+32
    return f

fah=list(map(celsToFah,cel))
print(fah)