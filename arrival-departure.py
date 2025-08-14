import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better aesthetics
sns.set(style="whitegrid")

# Sample data
arrival_times = [0.5, 1.2, 2.8, 3.5, 4.1]
departure_times = [1.0, 2.0, 3.5, 4.0, 5.0]

# Calculate time spent in system
time_differences = [dep - arr for arr, dep in zip(arrival_times, departure_times)]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(time_differences) + 1), time_differences, marker='o', linestyle='-', color='teal')
plt.title('Time Spent in Queue per Customer', fontsize=14)
plt.xlabel('Customer Index', fontsize=12)
plt.ylabel('Time in System (Departure - Arrival)', fontsize=12)
plt.xticks(range(1, len(time_differences) + 1))
plt.tight_layout()
plt.show()

# Save the plot to a file
plt.savefig('time_spent_in_queue.png')