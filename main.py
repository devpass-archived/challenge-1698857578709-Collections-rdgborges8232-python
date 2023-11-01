from collections import Counter

def count_duplicates(lst):
    counts = Counter(lst)
    duplicates = sum(count - 1 for count in counts.values())
    return duplicates

if __name__ == '__main__':
    numbers = [1, 3, 4, 2, 5, 3, 4, 1, 1]
    print(count_duplicates(numbers))  # Expected: 4
