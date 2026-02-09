def add(a, b):
    return a + b

print("This line always runs")

if __name__ == "__main__":
    print("This runs only when the file is executed directly")
    result = add(2, 3)
    print("Result:", result)

