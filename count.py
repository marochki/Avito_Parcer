from collections import Counter

# Чтение строк из файла
with open('output.txt', 'r') as file:
    lines = file.readlines()

# Подсчет уникальных строк и их повторений
line_count = Counter(lines)

# Вывод результата
print("Количество уникальных строк в файле:", len(line_count))
print("Повторения каждой из строк:")
for line, count in line_count.items():
    print(f"{line.strip()}: {count}")

