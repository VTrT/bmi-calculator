"""
There's just one problem: by holding the two lists up side by side (your puzzle input),
it quickly becomes clear that the lists aren't very similar.
Maybe you can help The Historians reconcile their lists?

For example:

3   4
4   3
2   5
1   3
3   9
3   3
Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are.
Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest
 left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
 For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4;
  if you pair up a 9 with a 3, the distance apart is 6.
"""

left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]


def list_diff(first_list, second_list):
    i = 0
    differences_list = []
    for item in first_list:
        differences_list.append(
            abs(item - second_list[i])
        )
        i = i + 1
    return differences_list


left_list.sort()
right_list.sort()

print(left_list)
print(right_list)

distances = list_diff(left_list, right_list)
print(distances)
print(f"\nTotal distance: {sum(distances)}")

left_list = []
with open("left_list.txt") as f:
    for line in f.readlines():
        left_list.append(int(line))

right_list = []
with open("right_list.txt") as f:
    for line in f.readlines():
        right_list.append(int(line))

left_list.sort()
right_list.sort()

print(left_list)
print(right_list)

distances = list_diff(left_list, right_list)
print(distances)
print(f"Total distance: {sum(distances)}")


# Here are the same example lists again:
#
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# For these example lists, here is the process of finding the similarity score:
#
# The first number in the left list is 3. It appears in the right list three times,
# so the similarity score increases by 3 * 3 = 9.
# The second number in the left list is 4. It appears in the right list once,
# so the similarity score increases by 4 * 1 = 4.
# The third number in the left list is 2. It does not appear in the right list,
# so the similarity score does not increase (2 * 0 = 0).
# The fourth number, 1, also does not appear in the right list.
# The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
# The last number, 3, appears in the right list three times; the similarity score again increases by 9.
# So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

def list_similarities(first_list, second_list):
    similarities_list = []
    for item in first_list:
        i = 0
        for second_item in second_list:
            if item == second_item:
                i = i + 1
        similarities_list.append(item * i)
    return similarities_list


left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 8, 3]
similarities = list_similarities(left_list, right_list)
print(similarities)
print(f"Total similarities: {sum(similarities)}\n")

left_list = []
with open("left_list.txt") as f:
    for line in f.readlines():
        left_list.append(int(line))

right_list = []
with open("right_list.txt") as f:
    for line in f.readlines():
        right_list.append(int(line))

left_list.sort()
right_list.sort()

similarities = list_similarities(left_list, right_list)
print(similarities)
print(f"Total similarities: {sum(similarities)}\n")

