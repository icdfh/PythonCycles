# asdkqweasdqwlkel;asd\
# q;wleka;sldkq;lwejk;lasd
# qwlekas;ldjq;lwej
# \qwejasdk

# i = 1
# while i <= 5:
#     print(i)
#     i -= 1

# correct = "1234"
# pwd = input("Введите пароль: ")
# while pwd != correct:
#     print("Неверно,Попробуй еще!")
#     pwd = input("Введите пароль: ")
# print("Доступ разрещен")


# total = 0 
# while True:
#     x = int(input("Введите число (0 - стоп)"))
#     if x == 0:
#         break
#     total += x
# print("Сумма: ", total)

# total = 0
# while True:
#     x = int(input("Введите число (0 - стоп): "))
#     if x == 0:
#         break
#     if x < 0:
#         continue
#     total += x
# print("Сумма", total)

# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# for i in range(10,0,-1):
#     print("Число:",i)

# for i in range(1,101):
#     if i % 7 == 0:
#         print("Первое кратное 7: ",i)
#         continue

# for i in range(1,101,2):
#     print(i)

# word = "Python"
# for i in word:
#     if "o" in word:
#         print("Если нашел скажи")
#         break
# print("Ничего не дам")

# word = "Python"
# print(len(word))
# for i in range(len(word)):
#     print(i, word[i])

# sum
# avg = sum / len


text = input("Введите какое то слово на англ: ")
spaces = 0
e_count = 0
for i in text:
    if i == " ":
        spaces += 1
    if i == "e" or i == "E":
        e_count += 1
print("Пробелов:", spaces)
print("Букв Е:", e_count)

