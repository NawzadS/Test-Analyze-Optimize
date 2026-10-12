
# Problem 1: Find Most Frequent Element
def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    most_common = numbers[0]

    for number in numbers:
        if number not in counts:
            counts[number] = 0

        counts[number] += 1

        if counts[number] > counts[most_common]:
            most_common = number

    return most_common


"""
Time and Space Analysis for Problem 1:

Best-case: O(n), because I still have to check every number.
Worst-case: O(n) normally, since dictionary operations are usually O(1).
Average-case: O(n), because I only go through the list once.

Space complexity: O(n), because the dictionary might need to store
every number if they are all different.

Why this approach?
I used a dictionary to count how many times each number appears.
This is easier and faster than going through the list multiple times.

Could it be optimized?
I could use Python's Counter, but the time complexity would still
be O(n). I could also sort the list, but that would usually take
O(n log n) time. The dictionary uses extra memory, but it saves time.
"""


# Problem 2: Remove Duplicates While Preserving Order
def remove_duplicates(nums):
    seen = set()
    result = []

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


"""
Time and Space Analysis for Problem 2:

Best-case: O(n), because I still check every number.
Worst-case: O(n) normally, since checking a set is usually O(1).
Average-case: O(n), because I only go through the list once.

Space complexity: O(n), because I use a set and a new list.

Why this approach?
I used a set to remember which numbers I already saw. The result
list keeps the numbers in the same order they originally appeared.

Could it be optimized?
I could remove the set and just check the result list, but that
could make the time complexity O(n^2). Using a set takes extra
memory, but makes checking for duplicates faster.
"""


# Problem 3: Return All Pairs That Sum to Target
def find_pairs(nums, target):
    seen = set()
    pairs = []

    for number in nums:
        needed = target - number

        if needed in seen:
            pairs.append((needed, number))

        seen.add(number)

    return pairs


"""
Time and Space Analysis for Problem 3:

Best-case: O(n), because I check every number.
Worst-case: O(n) normally, because set lookups are usually O(1).
Average-case: O(n), because I only need one loop.

Space complexity: O(n), because I use a set and a list for pairs.

Why this approach?
I used a set to keep track of numbers I already checked.
For each number, I subtract it from the target to see what
other number I need to make the pair.

Could it be optimized?
I could use two loops to compare every pair, which would use
less extra memory, but it would take O(n^2) time. I chose the
set because it is faster for larger lists.
"""


# Problem 4: Simulate List Resizing
def add_n_items(n):
    capacity = 2
    size = 0
    items = [None] * capacity

    for number in range(n):
        if size == capacity:
            new_capacity = capacity * 2

            print("Resizing from", capacity, "to", new_capacity)

            new_items = [None] * new_capacity

            for i in range(size):
                new_items[i] = items[i]

            items = new_items
            capacity = new_capacity

        items[size] = number
        size += 1

    return items[:size]


"""
Time and Space Analysis for Problem 4:

Best-case: O(1) for one append when there is enough space.
Worst-case: O(n) for one append when resizing copies n items.
Average-case: O(1) amortized per append.
Adding n items overall takes O(n) time.

When do resizes happen?
Resizing happens when the list reaches its capacity. It starts
at 2, then doubles to 4, 8, 16, and so on.

Space complexity: O(n), because the list grows as more items
are added. During resizing, both lists temporarily exist.

Why this approach?
I doubled the capacity so the list does not need to resize
every time an item is added.

Could it be optimized?
I could start with a larger capacity to reduce resizing, but
that would waste memory if I do not add many items.

Why does doubling help?
Even though resizing takes longer when it happens, most
appends do not need resizing. This makes the average cost
per append O(1) over many operations.
"""


# Problem 5: Compute Running Totals

# Original version before optimization
def running_total_original(nums):
    result = []

    for i in range(len(nums)):
        total = 0

        for j in range(i + 1):
            total += nums[j]

        result.append(total)

    return result


# Optimized version
def running_total(nums):
    result = []
    total = 0

    # I optimized this by keeping the previous total instead
    # of starting over and adding the same numbers again.
    for number in nums:
        total += number
        result.append(total)

    return result


"""
Time and Space Analysis for Problem 5:

Best-case: O(n), because I still go through every number.
Worst-case: O(n), because I only use one loop.
Average-case: O(n), because every number is visited once.

Space complexity: O(n), because I create a new list.

Why this approach?
I used a running total so I can keep adding the next number
without having to calculate the entire sum again.

Could it be optimized?
If I were allowed to change the original list, I could update
the totals directly in it and use O(1) extra space. However,
the assignment asks me to return a new list.

Optimization comparison:

Original version:
Time complexity: O(n^2)
Space complexity: O(n)

Optimized version:
Time complexity: O(n)
Space complexity: O(n)

The original version used nested loops and kept adding the
same numbers multiple times.

The optimized version only uses one loop and remembers the
total from the previous step.

Both versions use the same amount of extra space, but the
optimized version is faster because it avoids repeated work.

The trade-off is that it still needs a new list to store the
results, but this is required by the problem.
"""


# Test cases for all five problems
if __name__ == "__main__":

    # Problem 1 tests
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
    assert most_frequent([5, 5, 2]) == 5
    assert most_frequent([]) is None

    # Problem 2 tests
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([]) == []
    assert remove_duplicates([2, 2, 2]) == [2]

    # Problem 3 tests
    assert set(find_pairs([1, 2, 3, 4], 5)) == {(1, 4), (2, 3)}
    assert find_pairs([1, 2, 3], 20) == []
    assert set(find_pairs([-2, 0, 2, 4], 2)) == {(-2, 4), (0, 2)}

    # Problem 4 tests
    assert add_n_items(0) == []
    assert add_n_items(1) == [0]
    assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

    # Problem 5 tests
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([]) == []
    assert running_total([-1, 2, -3]) == [-1, 1, -2]

    assert running_total_original([1, 2, 3, 4]) == running_total([1, 2, 3, 4])

    print("All tests passed!")
