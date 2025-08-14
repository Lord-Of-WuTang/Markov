import random
import matplotlib.pyplot as plt

# Parameters
arrival_rate = 0.5  # average arrivals per time unit
service_rate = 0.6  # average services per time unit
simulation_time = 100

# Simulation variables
arrival_times = []
service_start_times = []
departure_times = []
queue = []

current_time = 0
next_arrival = random.expovariate(arrival_rate)
next_departure = float('inf')

while current_time < simulation_time:
    if next_arrival <= next_departure:
        current_time = next_arrival
        arrival_times.append(current_time)
        queue.append(current_time)
        next_arrival = current_time + random.expovariate(arrival_rate)
        if len(queue) == 1:
            next_departure = current_time + random.expovariate(service_rate)
    else:
        current_time = next_departure
        service_start_times.append(queue[0])
        departure_times.append(current_time)
        queue.pop(0)
        if queue:
            next_departure = current_time + random.expovariate(service_rate)
        else:
            next_departure = float('inf')

# Metrics
wait_times = [d - a for a, d in zip(arrival_times, departure_times)]
average_wait = sum(wait_times) / len(wait_times)

# Visualization
plt.plot(arrival_times, label='Arrival Times')
plt.plot(departure_times, label='Departure Times')
plt.xlabel('Customer Index')
plt.ylabel('Time')
plt.title(f'Single-Server Queue Simulation\nAverage Wait Time: {average_wait:.2f}')
plt.legend()
plt.grid(True)
plt.show()
# Save the results to a file
with open('queue_simulation_results.txt', 'w') as f:
    f.write(f'Average Wait Time: {average_wait:.2f}\n')
    f.write('Arrival Times:\n')
    for time in arrival_times:
        f.write(f'{time:.2f}\n')
    f.write('Departure Times:\n')
    for time in departure_times:
        f.write(f'{time:.2f}\n')