import sys
from multiprocessing import Pool, cpu_count
from typing import List, Tuple


def compute_sum_of_powered_non_positives(numbers: List[int], power_table: Tuple[int, ...]) -> int:
    # Filter non-positive values (<= 0)
    filtered = filter(lambda x: x <= 0, numbers)
    # Use the power table: for value x, lookup at index (x + 100) since table starts at -100
    powered = map(lambda x: power_table[x + 100], filtered)
    return sum(powered)


def process_single_test_case(case_data: Tuple[int, str, str, Tuple[int, ...]]) -> Tuple[int, int]:
    case_index, x_line, numbers_line, power_table = case_data
    try:
        expected_count = int(x_line)
        if expected_count < 0:
            return (case_index, -1)

        parts = numbers_line.split()
        if len(parts) != expected_count:
            return (case_index, -1)

        numbers = tuple(map(int, parts))
        result = compute_sum_of_powered_non_positives(numbers, power_table)
        return (case_index, result)

    except (ValueError, AttributeError, IndexError):
        return (case_index, -1)


def chunk_input_optimized(lines: List[str], num_cases: int, power_table: Tuple[int, ...]) -> List[
    Tuple[int, str, str, Tuple[int, ...]]]:
    # Separate even/odd lines (count on even, numbers on odd)
    even_lines = lines[0::2]
    odd_lines = lines[1::2]

    indices = range(num_cases)

    def get_lines(i: int) -> Tuple[int, str, str, Tuple[int, ...]]:
        x_line = even_lines[i] if i < len(even_lines) else ''
        num_line = odd_lines[i] if i < len(odd_lines) else ''
        return (i, x_line, num_line, power_table)

    return list(map(get_lines, indices))


def process_all_test_cases_parallel(num_cases: int, remaining_lines: List[str]) -> List[int]:
    if num_cases <= 0:
        return []

    # Pre-compute x^4 for x in [-100, 0]
    POWER_FOUR_TABLE = tuple(x ** 4 for x in range(-100, 1))

    test_case_data = chunk_input_optimized(remaining_lines, num_cases, POWER_FOUR_TABLE)

    num_workers = min(cpu_count(), num_cases)

    # Use sequential processing for small workloads
    if num_cases <= 4 or num_workers == 1:
        indexed_results = tuple(map(process_single_test_case, test_case_data))
    else:
        chunk_size = max(1, num_cases // (num_workers * 4))

        with Pool(processes=num_workers) as pool:
            indexed_results = tuple(pool.imap(
                process_single_test_case,
                test_case_data,
                chunksize=chunk_size
            ))

    # Reconstruct results in original order
    results = [0] * num_cases
    tuple(map(lambda x: results.__setitem__(x[0], x[1]), indexed_results))
    return results


def strip_line(line: str) -> str:
    return line


def is_non_empty(line: str) -> bool:
    return bool(line)


def main():
    # Read and filter input lines
    stripped_lines = map(strip_line, sys.stdin)
    non_empty_lines = filter(is_non_empty, stripped_lines)
    all_lines = list(non_empty_lines)

    if not all_lines:
        return

    try:
        num_cases = int(all_lines[0])

        if num_cases <= 0:
            return

        remaining_lines = all_lines[1:]
        results = process_all_test_cases_parallel(num_cases, remaining_lines)
        if results:
            result_strings = map(str, results)
            output = '\n'.join(result_strings)
            print(output)

    except (ValueError, IndexError):
        pass


if __name__ == "__main__":
    main()
