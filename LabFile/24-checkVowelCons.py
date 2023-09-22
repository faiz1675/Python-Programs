# 24-WAP to enter a character and then determine whether it is a vowel, consonants, or a digit.
ch=input('Enter any character: ')
if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
    if ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='i' or ch=='I' or ch=='O' or ch=='o' or ch=='U' or ch=='u':
        print('The given character is vowel.')
    else:
        print('The given character is consonant')
elif ch>='0' and ch<='9':
    print("The given character is a digit")
