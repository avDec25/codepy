import random

def generate_test_file(filename="large_input.txt", num_cases=100000):
    with open(filename, "w") as f:
        f.write(f"{num_cases}\n")
        for _ in range(num_cases):
            count = random.randint(10, 50)
            nums = [random.randint(-100, 100) for _ in range(count)]
            f.write(f"{count}\n")
            f.write(" ".join(map(str, nums)) + "\n")

generate_test_file()
print("Large test file generated.")