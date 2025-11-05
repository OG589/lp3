class Item:
    def __init__(self, value, weight, index):
        self.value = value
        self.weight = weight
        self.index = index
        self.ratio = value / weight


def getMaxValue(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0
    total_weight_used = 0
    items_included = []
    remaining_capacity = capacity

    for item in items:
        if item.weight <= remaining_capacity:
            total_value += item.value
            total_weight_used += item.weight
            remaining_capacity -= item.weight
            items_included.append(
                f"Item {item.index}: Weight = {item.weight}, Value = {item.value}"
            )
        else:
            fraction = remaining_capacity / item.weight
            value_taken = item.value * fraction
            total_value += value_taken
            total_weight_used += remaining_capacity

            items_included.append(
                f"Item {item.index}: Weight = {remaining_capacity:.2f}, Value = {value_taken:.2f}"
            )
            break

    print(f"\nMaximum value that can be put in knapsack = {total_value:.2f}")
    print(f"Total weight used = {total_weight_used:.2f}")
    print("Items included:")

    for x in items_included:
        print(x)


# MAIN
n = int(input("Enter number of items: "))
items = []

for i in range(1, n + 1):
    w = int(input(f"Weight of item {i}: "))
    v = int(input(f"Value of item {i}: "))
    items.append(Item(v, w, i))

capacity = int(input("Enter capacity of Knapsack: "))
getMaxValue(items, capacity)
