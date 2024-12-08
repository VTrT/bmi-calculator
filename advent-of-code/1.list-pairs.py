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