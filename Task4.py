# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# Примеры:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10


# Решение 1:

"""
Для решения этой задачи можно воспользоваться следующими логическими рассуждениями:

1. Пусть Петя сделал X журавликов.
2. Серёжа сделал столько же журавликов - тоже X.
3. Катя сделала в два раза больше журавликов, чем Петя и Серёжа вместе, то есть 2 * (X + X) = 4X журавликов.

Общее количество журавликов, сделанных Петей, Серёжей и Катей, равно X + 4X + X = 6X.

Зная общее количество журавликов n, можем найти X:
x = n / 6

Теперь, зная x, можно определить количество журавликов, сделанных каждым ребёнком.
"""

# def crane_count(n):
#     # Найти количество журавликов, сделанных Петей и Серёжей
#     x = n // 6
#     # Количество журавликов, сделанных Катей
#     katya = 4 * x
#     # Петя и Серёжа сделали одинаковой количество журавликов
#     petya = x
#     serezha = x
#     return petya, katya, serezha

# n = 6
# petya, katya, serezha = crane_count(n)
# print(petya, katya, serezha)

"""
Этот код сначала вычисляет количество журавликов, сделанных каждым ребёнком, а затем
выводит результат.
"""

# Решение 2:

"""
Для решения задачи нужно определить количество журавликов, сделанных каждым из детей, 
зная, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза 
больше журавликов, чем Петя и Сережа вместе.

Давайте обозначим количество журавликов, сделанных Петей и Сережей, как xx. Тогда Катя 
сделала 2(x + x) = 4x2(x+x)=4x журавликов, так как она сделала в два раза больше журавликов, 
чем Петя и Сережа вместе.

Суммарное количество журавликов, которое сделали все трое, равно nn. Мы можем записать это так:
x + x + 4x = nx+x+4x=n

Упрощаем уравнение:
6x = n6x=n

Таким образом, чтобы найти xx, нужно разделить nn на 6. После этого можно найти количество 
журавликов, сделанных каждым ребенком:

Петя и Сережа сделали по xx журавликов.
Катя сделала 4x4x журавликов.

Теперь на основе этого формулируем код:
"""

# def count_cranes(n):
#     if n % 6 != 0:
#         return "Ответ не существует для данного n"
    
#     x = n // 6
#     pete = x
#     katya = 4 * x
#     serezha = x
    
#     return pete, katya, serezha

# n = int(input("Введите общее количество журавликов n: "))
# pete, katya, serezha = count_cranes(n)
# print(pete, katya, serezha)

"""
Этот код сначала проверяет, делится ли nn на 6, чтобы убедиться, что количество журавликов 
можно корректно распределить между детьми. Затем он вычисляет количество журавликов, 
сделанных каждым из детей, и выводит их.
"""

# Решение 3 (без использования фунций):

# Ввод общего количества журавликов
n = int(input("Введите общее количество журавликов n: "))

# Проверка, делится ли n на 6
if n % 6 == 0:
    x = n // 6  # Количество журавликов, сделанных Петей и Сережей (каждый сделал по x)
    katya = 4 * x  # Количество журавликов, сделанных Катей
    # Вывод количества журавликов, сделанных Петей, Катей и Сережей
    print(x, katya, x)
else:
    print("Ответ не существует для данного n")