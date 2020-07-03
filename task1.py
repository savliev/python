# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета
# для конкретных значений необходимо запускать скрипт с параметрами.
def salary_calc(worktime, rate, bonus):
     """Функция расчета зп. Входные параметры: выработка в часах, ставка в час, премия"""
     try:
          return worktime * rate + bonus
     except TypeError:
          return

# использование функции с указанием параматров в конфигураторе (задано 160-500-35000)
import sys
try:
     file, worktime, rate, bonus = sys.argv
except ValueError:
     print("Invalid args")
     exit()

print(salary_calc(int(worktime), int(rate), int(bonus)))
