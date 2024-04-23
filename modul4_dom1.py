def total_salary(path):
    total_sum = 0
    count = 0
    
    try:
        with open(path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total_sum += salary
                        count += 1
                    except ValueError:
                        print(f"Увага!!!немає данних, ведіть данні по працівнику '{line.strip()}'.")
                        return None, None
    
        if count == 0:
            print("Не має інформації по зарплатні")
            return None, None
        else:
            average_salary = total_sum / count
            return total_sum, average_salary
    except FileNotFoundError:
        print(f"Увага!!! Файл '{path}' не знайдено.")
        return None, None

total_sum, average_salary = total_salary("salaries.txt")
if total_sum is not None and average_salary is not None:
    print("Загальна сума заробітної плати:", total_sum)
    print("Середня заробітна плата:", average_salary)
