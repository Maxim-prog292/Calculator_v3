import math

#пользователь вводит запрос
oper = input("Какую опервцию вы хотите выполнить: ")

#списки возможных запросов
#сумма
sum = ["+", "сумма", "сложение", "Сумма", "Сложение", "Sum", "sum", "сложить", "Сложить"]
#вычитание
sub = ["-", "вычитание", "Вычитание", "вычесть", "Вычесть", "найти разницу", "Найти разницу", "subtraction", "Subtraction"]
#умножение
mult = ["*", "•", "×", "умножить", "Умножить", "Умножить числа", "умножить числа", "умножение", "Умножение", "Multiplication", "multiplication"]
#деление
div = ["/", "÷", "деление", "Деление", "разделить", "Разделить", "division", "Division", "разделить числа", "Разделить числа"]
#возведение в степень
deg = ["**", "^", "возвести в степень", "Возвести в степень", "Степень", "степень", "возвести", "Возвести", "возведение в степень", "Возведение в степень"]
#извдечение корня
root = ["√", "извлечь корень", "Извлечь корень", "корень извлечь", "Корень извлечь", "корень", "Корень", "извлечение корня", "Извлечение корня", "Извлечение квадратного корня", "извлечение квадратного корня"]

#операция сложения
if oper in sum:
	firstNum = int(input("Введите первое число: "))
	secNum = int(input("Введите второе число: "))
	numSum = firstNum + secNum
	print(f"Ответ: {numSum}")

#операция вычитания
if oper in sub:
	firstNum = int(input())
	secNum = int(input())
	if firstNum < secNum:
		subNum = secNum - firstNum
		print(f"Ответ: {subNum}")
	else:
		subNum = firstNum - secNum
		print(f"Ответ: {subNum}")
		
#операция умножения
if oper in mult:
	firstNum = int(input("Введите первое число: "))
	secNum = int(input("Введите второе число: "))
	multNum = firstNum * secNum
	print(f"Ответ: {multNum}")

#операция деления
if oper in div:
	firstNum = int(input("Введите первое число: "))
	secNum = int(input("Введите второе число: "))
	if secNum == 0:
		print("На ноль делить нельзя!")
	else:
		divNum = firstNum / secNum
		print(f"Ответ: {divNum}")
		
#возведение в степень
if oper in deg:
	firstNum = int(input("Введите число: "))
	secNum = int(input("Введите степень: "))
	degNum = firstNum ** secNum
	print(f"Ответ: {degNum}")
	
#извлечение корня
if oper in root:
	root = int(input("Введите число под корнем: "))
	print(f"Ответ: {math.sqrt(root)}")
