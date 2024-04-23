def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, cat_name, cat_age = parts
                    cat_info = {
                        "id": cat_id,
                        "name": cat_name,
                        "age": int(cat_age)
                    }
                    cats_info.append(cat_info)
                else:
                    print(f"Помилка: Неправильний формат рядка '{line.strip()}'")
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка під час обробки файлу: {e}")

    return cats_info

cats = get_cats_info("cats.txt")
print(cats)
