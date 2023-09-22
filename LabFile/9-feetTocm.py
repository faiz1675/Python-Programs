# 9-Python program to convert height (in feet and inches) to centimetres. (1 feet= 12 inches, 1 inch=2.54 cm)(cms=feet*12*2.54+inches*2.54)
ft=int(input("Enter the height in feet: "))
inc=int(input("Enter th height in inches: "))

inc=inc+ft*12
cm=inc*2.54

print("{} Feet and {} inches = {} cm".format(ft,inc,cm))