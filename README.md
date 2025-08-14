# Basic Queue Simulation

A fundamental single-server queue simulation using event-driven modeling and exponential distributions.

## Overview

This is a lightweight, educational queue simulation that demonstrates core queueing theory principles through discrete event simulation. It models a simple M/M/1 queue (Markovian arrivals, Markovian service, 1 server) and provides basic performance metrics.

## How It Works

The simulation uses an event-driven approach where:
- **Customers arrive** according to a Poisson process (exponential inter-arrival times)
- **Service times** follow an exponential distribution
- **Queue discipline** is First-Come, First-Served (FCFS)
- **Single server** processes one customer at a time

## Key Features

- **Real-time Event Processing**: Uses discrete event simulation methodology
- **Statistical Modeling**: Exponential distributions for arrivals and service
- **Performance Metrics**: Calculates average wait times automatically
- **Visual Output**: Generates arrival vs departure time plots
- **Lightweight**: Minimal dependencies and fast execution

## Parameters

```python
arrival_rate = 0.5      # Average arrivals per time unit
service_rate = 0.6      # Average services per time unit  
simulation_time = 100   # Total simulation duration
```

### Queue Characteristics
- **Traffic Intensity (ρ)**: 0.5/0.6 = 0.83 (stable system, ρ < 1)
- **Expected Wait Time**: Approximately 4.17 time units (theoretical)
- **Server Utilization**: ~83%

## Requirements

```
matplotlib
```

## Installation

```bash
pip install matplotlib
```

## Usage

```bash
python queue_simulation.py
```

## Output

### Metrics Displayed
- **Average Wait Time**: Mean time customers spend waiting in queue
- **Visual Plot**: Timeline showing arrival and departure patterns

### Sample Output
```
Single-Server Queue Simulation
Average Wait Time: 4.23
```

The plot displays:
- **Blue line**: Customer arrival times
- **Orange line**: Customer departure times
- **Gap between lines**: Represents wait time for each customer

## Understanding the Results

### Performance Indicators
- **Small gaps**: Efficient service with minimal waiting
- **Growing gaps**: Queue building up, increasing wait times
- **Parallel lines**: Steady-state operation
- **Converging lines**: Queue clearing, reduced wait times

### Theoretical vs Simulation
For M/M/1 queue with λ=0.5, μ=0.6:
- **Theoretical average wait**: W = λ/(μ(μ-λ)) = 0.5/(0.6×0.1) = 8.33
- **Simulation results**: Should approximate this value with sufficient runtime

## Code Structure

### Core Components
1. **Event Scheduling**: Manages next arrival and departure events
2. **Queue Management**: Maintains FIFO customer queue
3. **Time Advancement**: Discrete event time progression
4. **Statistics Collection**: Tracks arrivals, departures, and wait times
5. **Visualization**: Matplotlib plotting of results

### Algorithm Flow
```
Initialize → Schedule First Arrival → Process Events Loop:
  ├── If Next Event is Arrival:
  │   ├── Add customer to queue
  │   ├── Schedule next arrival
  │   └── Start service if server idle
  └── If Next Event is Departure:
      ├── Remove customer from queue
      ├── Record departure time
      └── Start service for next customer
```

## Educational Value

This simulation demonstrates:
- **Discrete Event Simulation**: Event-driven modeling approach
- **Stochastic Processes**: Random arrival and service patterns
- **Queue Theory**: M/M/1 system behavior
- **Performance Analysis**: Wait time calculations
- **System Stability**: Impact of arrival vs service rates

## Limitations

- **Single Server Only**: No multi-server capability
- **Infinite Queue**: No capacity constraints
- **Basic Metrics**: Limited performance measures
- **No Customer Differentiation**: All customers treated identically
- **Fixed Parameters**: No dynamic rate changes

## Extensions

This basic simulation can be enhanced with:
- Multiple servers (M/M/c queues)
- Finite queue capacity (M/M/1/K systems)
- Different service disciplines (Priority, LIFO, etc.)
- Non-exponential distributions
- Customer classification and priority levels
- Real-time visualization and animation
- Advanced statistics (percentiles, confidence intervals)

## Theoretical Background

### M/M/1 Queue Formulas
- **Average customers in system**: L = ρ/(1-ρ)
- **Average customers in queue**: Lq = ρ²/(1-ρ)  
- **Average time in system**: W = 1/(μ-λ)
- **Average wait time**: Wq = ρ/(μ-λ)

Where ρ = λ/μ is the traffic intensity.

## Performance Notes

- **Fast Execution**: Suitable for educational demonstrations
- **Memory Efficient**: Minimal data storage requirements
- **Scalable**: Can handle longer simulation times
- **Deterministic Output**: Results vary due to randomness

---

*This simulation serves as an excellent introduction to queueing theory and discrete event simulation concepts.*