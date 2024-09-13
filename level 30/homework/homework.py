# 8) შექმენით for loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
for i in range(1, 11):
    print(i)

# 9) შექმენით რიცხვების list'ი, შექმენით for loop'ი list'ის რიცხვების ჯამის გამოსათვლელად.
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)

# 10) შექმენით for loop'ი თითოეული სიმბოლოს დასაბეჭდად სტრინგში -> "Hello, World!".
string = "Hello, World!"
for char in string:
    print(char)

# 11) შექმენით while loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
i = 1
while i <= 10:
    print(i)
    i += 1

# 12) შექმენით while loop'ი რომელიც დათვლის რიცხვებს 1დან 100მდე თუმცა გამოტოვებს რიცხვებს 50დან 60მდე.
i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1

# 13) შექმენით while loop'ი, რომელიც დაიწყებს რიცხვების შეკრებას 1-დან, სანამ ჯამი არ გაუტოლდება 50-ს.
i = 1
total = 0
while total < 50:
    total += i
    i += 1
print(total)

# 14) შექმენით ფუნქცია რომელიც მომხმარებელს შემოატანინებს რიცხვს და დაპრინტავს ეს რიცხვი თუ იყოფა 3ზე ან 5ზე ან ორივეზე
def check_divisibility():
    number = int(input("Enter a number: "))
    if number % 3 == 0 or number % 5 == 0:
        print(number)

check_divisibility()

# 15) შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია,თქვენი მოვალეობააა გამოითვალოთ ამ სიის საშუალო არითმეტიკული.
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print(calculate_average([1, 3, 4, 5, 2]))