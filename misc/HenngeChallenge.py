def main():
    def sum_squares(numbers, length):
        if length == 0:
            return 0
        head, *tail = numbers
        return (head ** 2 if head >= 0 else 0) + sum_squares(tail, length - 1)

    def process_test_cases(n, results):
        if n == 0:
            return results

        # Read number of integers in the current test case
        X = int(input())

        # Read the integers as a list
        integers = list(map(int, input().split()))

        # Store the result
        results.append(sum_squares(integers, X))

        # Recursively process remaining test cases
        return process_test_cases(n - 1, results)

    # Read number of test cases
    N = int(input())

    # Start processing test cases with an empty result list
    results = process_test_cases(N, [])

    # Output all results at once
    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()
