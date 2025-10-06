import matplotlib.pyplot as plt

# Parameters
ssthresh = 64   # Slow start threshold (in MSS)
cwnd = 1        # Initial CWND (1 MSS)
time = 0        # Time in RTTs

# Data storage
time_list = [time]
cwnd_list = [cwnd]

# Simulate Slow Start
while cwnd < ssthresh:
    time += 1
    cwnd *= 2   # Exponential growth in slow start
    time_list.append(time)
    cwnd_list.append(cwnd)

# Plotting
plt.figure(figsize=(8,5))
plt.plot(time_list, cwnd_list, marker="o")
plt.title("TCP Slow Start Simulation")
plt.xlabel("Time (RTTs)")
plt.ylabel("Congestion Window (CWND in MSS)")
plt.grid(True)
plt.show()
