import sys


def filter_lines(lines, i, acc):
    if i >= len(lines):
        return acc
    if lines[i].strip() == '':
        return filter_lines(lines, i + 1, acc)
    return filter_lines(lines, i + 1, acc + [lines[i]])


def sum_power4(nums, i):
    if i >= len(nums):
        return 0
    val = nums[i]
    contribution = 0 if val > 0 else val ** 4
    return contribution + sum_power4(nums, i + 1)


def parse_cases(lines, index, n, results):
    if n == 0:
        return results
    x = int(lines[index])
    nums_raw = lines[index + 1].split()
    if len(nums_raw) != x:
        return parse_cases(lines, index + 2, n - 1, results + [-1])
    nums = list(map(int, nums_raw))
    total = sum_power4(nums, 0)
    return parse_cases(lines, index + 2, n - 1, results + [total])


def print_results(results, i):
    if i >= len(results):
        return
    print(results[i])
    print_results(results, i + 1)


def main():
    data = sys.stdin.read().split('\n')
    lines = filter_lines(data, 0, [])
    n = int(lines[0])
    results = parse_cases(lines, 1, n, [])
    print_results(results, 0)


if __name__ == "__main__":
    main()