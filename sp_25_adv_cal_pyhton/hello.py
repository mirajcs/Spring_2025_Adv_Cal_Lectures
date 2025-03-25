import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 4))

# Draw the full interval (0,1) as a dashed line at y=0 for reference
ax.hlines(0, 0, 1, colors='gray', linestyles='dashed', label='(0,1) full interval')
ax.text(0.5, -0.3, '(0,1)', fontsize=12, ha='center')

# Define a few values of n to illustrate the open cover intervals
n_values = [2, 3, 4, 5, 10]
colors = ['blue', 'green', 'red', 'orange', 'purple']

# Plot each interval (1/n,1) on a separate horizontal line
for i, n in enumerate(n_values):
    start = 1/n
    y = i + 1  # vertical position for this interval
    ax.hlines(y, start, 1, colors=colors[i], linewidth=5, label=f'$(1/{n},1)$')
    # Annotate the interval
    ax.text((start + 1)/2, y + 0.2, f'$(1/{n},1)$', fontsize=10, ha='center')

# Enhance the plot appearance
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.5, len(n_values) + 1)
ax.set_xlabel('x')
ax.set_ylabel('Interval index (for display)')
ax.set_title('Open Cover of (0,1) by Intervals $(1/n,1)$')
ax.legend(loc='upper left')

plt.show()