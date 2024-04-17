import os
import re
import sys

# Заданная маска
#mask_regex = re.compile(r'^pow\d{1,12}$')

# Путь к папке
folder_path = sys.argv[1]

# Проверка и удаление файлов
for filename in os.listdir(folder_path):
    if not re.match(r'^pow(?:[1-9]\d{3,11})',filename):
        os.remove(os.path.join(folder_path, filename))
        print(f"Файл {filename} удален")

