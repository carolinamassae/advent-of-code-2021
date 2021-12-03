from itertools import islice, tee


def main():
    with open('Input/day1.txt') as f:
        lines = [int(l.strip('\n\r')) for l in f.readlines()]

    print(compare_number(lines))
    print(compare_block(lines))
    print(compare_block_pedro(lines, 3))


def compare_number(lines):
    count = 0
    for previous, current in zip(lines, lines[1:]):
        if previous < current:
            count += 1
    return count


def compare_block(lines):
    count = 0
    for n1, n2, n3, n4 in zip(lines, lines[1:], lines[2:], lines[3:]):
        if n1 + n2 + n3 < n2 + n3 + n4:
            count += 1
    return count


def sliding_window(iterable, size):
    iterables = tee(iter(iterable), size)
    window = zip(*(islice(t, n, None) for n, t in enumerate(iterables)))
    yield from window


def compare_block_pedro(lines, n):
    count = 0
    prev = None
    for block in sliding_window(lines, 3):
        if prev is not None and sum(prev) < sum(block):
            count += 1
        prev = block
    return count


if __name__ == "__main__":
    main()
