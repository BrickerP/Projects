import csv
import os

# Get the current working directory
current_directory = os.getcwd()
# Step 1: Define the function to parse flow logs and map them to tags
def parse_flow_logs(flow_log_file, lookup_table_file):
    # Read the lookup table into a dictionary
    lookup_table = {}
    with open(lookup_table_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Combine dstport and protocol as the key for lookup
            key = (row['dstport'].strip(), row['protocol'].strip().lower())
            lookup_table[key] = row['tag'].strip()

    # Initialize counts
    tag_counts = {}
    port_protocol_counts = {}

    # Process the flow logs
    with open(flow_log_file, 'r') as log_file:
        for line in log_file:
            # Split the log line into components
            components = line.strip().split()
            dstport = components[6]
            protocol = 'tcp' if components[7] == '6' else 'udp'  # Assuming 6=tcp, 17=udp for simplicity

            # Map to tag
            key = (dstport, protocol)
            tag = lookup_table.get(key, 'Untagged')

            # Update tag counts
            if tag in tag_counts:
                tag_counts[tag] += 1
            else:
                tag_counts[tag] = 1

            # Update port/protocol combination counts
            if key in port_protocol_counts:
                port_protocol_counts[key] += 1
            else:
                port_protocol_counts[key] = 1

    return tag_counts, port_protocol_counts

# Step 2: Define function to write results to a file
def write_results_to_file(tag_counts, port_protocol_counts, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write tag counts
        writer.writerow(["Tag", "Count"])
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])
        
        writer.writerow([])  # Blank line

        # Write port/protocol combination counts
        writer.writerow(["Port", "Protocol", "Count"])
        for (port, protocol), count in port_protocol_counts.items():
            writer.writerow([port, protocol, count])

# Step 3: Define a function to run the program
def run_program(flow_log_file, lookup_table_file, output_file):
    tag_counts, port_protocol_counts = parse_flow_logs(flow_log_file, lookup_table_file)
    write_results_to_file(tag_counts, port_protocol_counts, output_file)

# Step 4: Example file paths (these would be replaced with actual file paths)
flow_log_file = os.path.join(current_directory, 'flow_logs.txt')
lookup_table_file = os.path.join(current_directory, 'lookup_table.csv')
output_file = os.path.join(current_directory, 'output_results.csv')

# Run the program
run_program(flow_log_file, lookup_table_file, output_file)