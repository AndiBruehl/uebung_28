count = int(input("Wie viele Fibonacci-Zahlen sollen ausgegeben werden?: "))
fibonacci_a = 0
fibonacci_b = 1
for i in range(count):
    print(fibonacci_a)
    fibonacci_c = fibonacci_a + fibonacci_b
    fibonacci_a = fibonacci_b
    fibonacci_b = fibonacci_c

print("Das sind alle Fibonacci-Zahlen der gewählten Eingabe.")