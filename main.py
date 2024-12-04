# #zadanie1
# def calculate_V(length, width, height):
#     return length * width * height
#
#
# def main():
#     total_V = 0
#
#     for i in range(1, 4):
#         print(f"Ввелите размеры {i} параллепида:")
#         length = float(input("Ввелите длину:: "))
#         width = float(input("Ввелите ширину:: "))
#         height = float(input("Ввелите высоту:: "))
#
#         V = calculate_V(length, width, height)
#         total_V += V
#         print(f"Объем {i}-го параллеп: {V:.2f}")
#
#     print(f"Общий объем трех параллепипеда: {total_V:.2f}")
# if __name__ == "__main__":
#     main()
# #zadanie2
# num = int(input("Скинь число от 1 до 10: "))
# if 1 <= num <= 10:
#     for i in range(1, 11):
#         result = num * i
#         print(f"{num} x {i} = {result}")
# else:
#     print("Сходи в больницу, если не видишь что написано от 1 до 10!")
# zadanie3
# import math
#
# def calculate_combinations(n, k):
#     if n < k:
#         return
#     return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
# n = int(input("Введите n: "))
# k = int(input("Введите k: "))
# if n < k:
#     print(f"{n} меньше {k}!")
# else:
#     result = calculate_combinations(n, k)
#     print(f"C({n}, {k}) = {result}")