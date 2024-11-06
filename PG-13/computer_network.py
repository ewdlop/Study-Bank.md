import random

# Function to generate random bandwidth calculation question
def generate_bandwidth_question():
    data_size_mb = random.randint(1, 1000)  # Data size in MB
    transfer_time_sec = random.randint(1, 60)  # Transfer time in seconds
    # Calculate bandwidth (in Mbps)
    bandwidth = (data_size_mb * 8) / transfer_time_sec
    problem = (f"Suppose you need to transfer {data_size_mb} MB of data over a network, "
               f"and it takes {transfer_time_sec} seconds to complete the transfer. "
               "What is the required bandwidth in Mbps?")
    return problem, f"{bandwidth:.2f} Mbps"

# Function to generate random latency question
def generate_latency_question():
    distance_km = random.randint(10, 5000)  # Distance between two points in km
    speed_of_signal_km_per_sec = 200000  # Speed of signal in km/s (rough estimate for fiber optics)
    # Calculate latency (in ms)
    latency_ms = (distance_km / speed_of_signal_km_per_sec) * 1000
    problem = (f"Two points in a network are {distance_km} km apart, and the signal travels at {speed_of_signal_km_per_sec} km/s. "
               "What is the latency in milliseconds (ms)?")
    return problem, f"{latency_ms:.2f} ms"

# Function to generate random throughput question
def generate_throughput_question():
    bandwidth_mbps = random.randint(1, 1000)  # Bandwidth in Mbps
    utilization_percentage = random.randint(10, 100)  # Network utilization percentage
    # Calculate throughput (in Mbps)
    throughput = (bandwidth_mbps * utilization_percentage) / 100
    problem = (f"A network has a bandwidth of {bandwidth_mbps} Mbps and is operating at {utilization_percentage}% utilization. "
               "What is the throughput in Mbps?")
    return problem, f"{throughput:.2f} Mbps"

# Generate random problems with solutions
generated_bandwidth_question = generate_bandwidth_question()
generated_latency_question = generate_latency_question()
generated_throughput_question = generate_throughput_question()

generated_bandwidth_question, generated_latency_question, generated_throughput_question
