# Определенные слова, с которых должны начинаться строки
keyword = "Сделка состоялась:"

# Открываем файл для чтения
with open("input.txt", "r") as file:
    lines = file.readlines()

# Открываем файл для записи
with open("output.txt", "w") as file:
    for line in lines:
            if line.strip().startswith(keyword):
                cleaned_line = line.replace(keyword, "").strip()
                file.write(cleaned_line + "\n")  
print("Файл успешно обработан. Строки")

