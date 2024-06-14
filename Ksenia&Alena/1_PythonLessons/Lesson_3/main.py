def arithmetic_operations(num, num1, num2, num3):
    num += num1
    num **= num2
    num /= num3
    num -= num1
    return num


number = int(input("Введите число: "))
print(f"Ваше число: {number}")

number = arithmetic_operations(num=number, num1=2, num2=3, num3=4)


print(number)
