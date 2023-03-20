user_eingabe = input("Bitte geben Sie ein, was wiederholt werden soll. ")
user_count = input("Bitte geben Sie ein, wie oft es wiederholt werden soll. ")

user_count1 = int(user_count)

for _ in range(user_count1):
    print(_ + 1, user_eingabe)