n = 7
W = 15
p = [0, 4, 5, 10, 7, 6, 8, 9]
w = [0, 1, 2, 3, 6, 2, 4, 5]

# Create a table to store the maximum values
table = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

# Fill in the table using dynamic programming
for i in range(1, n + 1):
    for w_cap in range(W + 1):
        if w[i] <= w_cap:
            table[i][w_cap] = max(table[i-1][w_cap], p[i] + table[i-1][w_cap - w[i]])
        else:
            table[i][w_cap] = table[i-1][w_cap]

# Find the maximum value
max_value = table[n][W]

# Backtrack to find the selected items
selected_items = []
i, w_cap = n, W
while i > 0 and w_cap > 0:
    if table[i][w_cap] != table[i-1][w_cap]:
        selected_items.append(i)
        w_cap -= w[i]
    i -= 1

print("Maximum value:", max_value)
print("Selected items:", selected_items)
