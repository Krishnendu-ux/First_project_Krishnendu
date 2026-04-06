def ledger_operations(a, b):
    total = a + b
    difference = a - b
    print(f"Total Combined Value: {total}")
    print(f"Difference: {difference}")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
ledger_operations(a, b)
