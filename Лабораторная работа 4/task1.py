import json
import os

filename = 'output.json'
indent = 1  # TODO Подставьте любое целое число
ensure_ascii = True  # TODO Замените на значение True

data = [
    {'score': 0.5, 'weight': 1},
    {'score': 0.098, 'weight': 2},
    {'score': 0.8, 'weight': 2},
]

# Запись данных в файл в формате JSON
with open(filename, 'w') as file:
    json.dump(data, file, indent=indent, ensure_ascii=ensure_ascii)

def task() -> float:
    with open(filename, 'r') as file:
        data = json.load(file)
    list_values =[item['score'] * item['weight'] for item in data]
    return round(sum(list_values), 3)

print(task())

