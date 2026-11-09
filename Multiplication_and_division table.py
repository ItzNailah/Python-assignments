#Display the program title
print("Multiplication and division table")
num = int(input("Please enter a number: "))
print("\nMultiplication table")
#Repeat the calculation from 1 to 10
for i in range(1,11):
    answer = num*i
#Display the multiplication result
    print(num,"X",i,"=",answer)
print("\nDivision table")
for i in range(1,11):
    answer = num*i
#same as the multiplication result but division
    print(answer, "/",num,"=",i)
