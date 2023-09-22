# 52-WAP to display the following pattern.
#       *
#     * * *
#   * * * * *
# * * * * * * *

for i in range(0,5):
    for j in range(0,4-i):
        print(' ',end=' ')
    for k in range(0,2*i+1):
        print("*",end=' ')
    print()