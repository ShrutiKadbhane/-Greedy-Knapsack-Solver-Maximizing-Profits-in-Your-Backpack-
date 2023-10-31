import time

# Define items with weight, profit, and volume
items = [
    {"weight": 2, "profit": 10, "volume": 5},
    {"weight": 3, "profit": 5, "volume": 2},
    {"weight": 5, "profit": 15, "volume": 10},
    {"weight": 7, "profit": 7, "volume": 7},
]

# Define the capacity of the knapsack
knapsack_capacity = 10

def greedy_by_weight(items, capacity):
    items.sort(key=lambda x: x["weight"])
    knapsack = []
    total_weight = 0
    total_profit = 0
    for item in items:
        if total_weight + item["weight"] <= capacity:
            knapsack.append(item)
            total_weight += item["weight"]
            total_profit += item["profit"]
    return knapsack, total_profit

def greedy_by_profit(items, capacity):
    items.sort(key=lambda x: x["profit"], reverse=True)
    knapsack = []
    total_weight = 0
    total_profit = 0
    for item in items:
        if total_weight + item["weight"] <= capacity:
            knapsack.append(item)
            total_weight += item["weight"]
            total_profit += item["profit"]
    return knapsack, total_profit

def greedy_by_density(items, capacity):
    items.sort(key=lambda x: x["profit"] / x["weight"], reverse=True)
    knapsack = []
    total_weight = 0
    total_profit = 0
    for item in items:
        if total_weight + item["weight"] <= capacity:
            knapsack.append(item)
            total_weight += item["weight"]
            total_profit += item["profit"]
    return knapsack, total_profit

def greedy_by_volume(items, capacity):
    items.sort(key=lambda x: x["volume"], reverse=True)
    knapsack = []
    total_weight = 0
    total_profit = 0
    for item in items:
        if total_weight + item["weight"] <= capacity:
            knapsack.append(item)
            total_weight += item["weight"]
            total_profit += item["profit"]
    return knapsack, total_profit

# Show a menu to the user
print("Welcome to the Knapsack Problem Solver!")
print("Please choose a Greedy Method:")
print("1. Greedy by Weight")
print("2. Greedy by Profit")
print("3. Greedy by Density")
print("4. Greedy by Volume")

choice = int(input("Enter your choice (1/2/3/4): "))

if choice not in [1, 2, 3, 4]:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
else:
    method_name = ""
    start_time = 0
    end_time = 0
    if choice == 1:
        method_name = "Greedy by Weight"
        start_time = time.time()
        result, total_profit = greedy_by_weight(items, knapsack_capacity)
        end_time = time.time()
    elif choice == 2:
        method_name = "Greedy by Profit"
        start_time = time.time()
        result, total_profit = greedy_by_profit(items, knapsack_capacity)
        end_time = time.time()
    elif choice == 3:
        method_name = "Greedy by Density"
        start_time = time.time()
        result, total_profit = greedy_by_density(items, knapsack_capacity)
        end_time = time.time()
    elif choice == 4:
        method_name = "Greedy by Volume"
        start_time = time.time()
        result, total_profit = greedy_by_volume(items, knapsack_capacity)
        end_time = time.time()

    # Display the results
    print("\n" + method_name + " Results:")
    print("Items in the knapsack:", result)
    print("Total Profit:", total_profit)
    print("Time Taken: {:.6f} seconds".format(end_time - start_time))
