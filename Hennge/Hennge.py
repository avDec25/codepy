import sys
from typing import List, Iterator


def compute_sum_of_powered_non_positives(numbers: List[int]) -> int:
    """
    Computes the sum of non-positive numbers raised to the 4th power.

    Process: filter(x <= 0) -> map(x^4) -> sum

    Args:
        numbers: List of integers to process

    Returns:
        Sum of (x^4) for all x where x <= 0
    """
    # Pure functional: filter -> map -> sum
    return sum(map(lambda x: x ** 4, filter(lambda x: x <= 0, numbers)))


def process_test_case(input_iterator: Iterator[str]) -> int:
    """
    Processes a single test case.

    Reads two lines:
    1. X (expected count)
    2. Space-separated integers

    Returns -1 if:
    - X is negative
    - Actual count of integers != X
    - Input is malformed

    Args:
        input_iterator: Iterator over input lines

    Returns:
        Computed sum or -1 for invalid input
    """
    try:
        expected_count = int(next(input_iterator))

        # Negative count is invalid
        if expected_count < 0:
            return -1

        number_line = next(input_iterator)
        numbers = list(map(int, number_line.split()))

        # Check if actual count matches X
        if len(numbers) != expected_count:
            return -1

        return compute_sum_of_powered_non_positives(numbers)

    except (StopIteration, ValueError):
        # Malformed input or premature end
        return -1


def safe_process_case(args) -> int:
    """
    Safely processes a test case, catching all exceptions.

    Args:
        args: Tuple of (case_number, input_iterator)

    Returns:
        Result of processing or -1 on error
    """
    try:
        _, input_iterator = args
        return process_test_case(input_iterator)
    except Exception:
        return -1


def process_all_test_cases(num_cases: int, input_iterator: Iterator[str]) -> List[int]:
    """
    Processes N test cases functionally without loops/recursion/comprehensions.

    Uses map() with shared iterator to process cases sequentially.

    Args:
        num_cases: Number of test cases (N)
        input_iterator: Iterator over remaining input lines

    Returns:
        List of N results (one per test case)
    """
    if num_cases <= 0:
        return []

    # Create N references to the same iterator
    # Each map() call advances the shared iterator
    case_numbers = range(num_cases)
    results = map(safe_process_case, zip(case_numbers, [input_iterator] * num_cases))

    return list(results)


def strip_line(line: str) -> str:
    """Helper to strip whitespace from a line."""
    return line.strip()


def is_non_empty(line: str) -> bool:
    """Helper to check if line is non-empty."""
    return bool(line)


def main():
    """
    Main entry point.

    REQUIREMENTS SATISFIED:
    1. No output until all input received - reads all stdin first
    2. No blank lines between outputs - uses '\n'.join()
    3. Takes input from stdin, outputs to stdout
    4. No EOF handling needed - reads complete stdin
    5. Output within int32 range - Python ints handle this naturally
    6. Prints -1 when count mismatch
    7. NO for loops, while loops, or comprehensions used anywhere

    Input format:
        Line 1: N (number of test cases)
        For each test case:
            Line 1: X (expected count)
            Line 2: X space-separated integers

    Output format:
        N lines, one result per test case (no blank lines between)
    """
    stripped_lines = map(strip_line, sys.stdin)
    non_empty_lines = filter(is_non_empty, stripped_lines)
    all_lines = list(non_empty_lines)

    if not all_lines:
        return

    try:
        num_cases = int(all_lines[0])

        if num_cases <= 0:
            return

        # Create iterator for remaining lines (slice, not comprehension)
        remaining_lines = all_lines[1:]
        input_iterator = iter(remaining_lines)

        results = process_all_test_cases(num_cases, input_iterator)

        # Output to stdout with NO blank lines between results
        if results:
            result_strings = map(str, results)
            output = '\n'.join(result_strings)
            print(output)

    except (ValueError, IndexError):
        # Malformed input
        pass


if __name__ == "__main__":
    main()