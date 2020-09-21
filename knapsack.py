
# Make an inventory of things to go into knapsack
inventory = {}
inventory['iPod'] = {'weight': 1, 'price': 150}
inventory['Laptop'] = {'weight': 4, 'price': 300}
inventory['Blu-ray player'] = {'weight': 3, 'price': 200}

# Set knapsack capacity
capacity = 4

def DP(inventory, capacity):

    # Initialize weights and values with placeholder 0's, so
    # that the algorithm can work on the first row and column.
    weights = [0]
    prices = [0]

    # Add weights and prices to lists
    for item in inventory.keys():
        weights.append(inventory[item]['weight'])
        prices.append(inventory[item]['price'])

    # Make the grid
    n = len(weights)
    grid = [[0 for w in range(capacity + 1)] for i in range(n)]

    # Grid algorithm
    for row in range(1, n):

        for col in range(1, capacity + 1):
            weight = weights[row]
            price = prices[row]

            if weight <= col:
                previous_max = grid[row - 1][col]
                possible_max = price + grid[row - 1][col - weight]

                grid[row][col] = max(previous_max, possible_max)

            else:
                grid[row][col] = grid[row - 1][col]


    for row in grid:
        print(row)


DP(inventory, capacity)



                

        


        


        





