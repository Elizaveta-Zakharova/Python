numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_without_None = numbers[:4]+numbers[5:]
sum_numbers_without_None = sum(numbers_without_None)
average = sum_numbers_without_None/len(numbers)
change_numbers = numbers[:4] + [average] + numbers[5:]
print("Измененный список:", change_numbers)

# TODO заменить значение пропущенного элемента средним арифметическим


