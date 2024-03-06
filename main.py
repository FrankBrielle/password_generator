import secrets as sec
import string as st
#Используем secrets, а не random (для криптографически сложных паролей)

letters = st.ascii_letters
digits = st.digits
special = st.punctuation

alphabet = letters + digits + special

pass_leng = int(input("Введите длину пароля: "))

while True:
    passw = ''
    for i in range(pass_leng):
        passw += ''.join(sec.choice(alphabet))
#Проверка на содержание специальных символов и цифр в пароле
    if (any(char in special for char in passw) and sum(char in digits for char in passw)>=2):
        break


print(f"Ваш пароль: {passw}")