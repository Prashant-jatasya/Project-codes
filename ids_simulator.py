import re
import time

def read_traffic_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

def detect_intrusions(network_traffic, log_file):
    # Simplified suspicious pattern for detecting access to /admin
    suspicious_pattern = r".*\b(GET|POST)\s(/admin)\b.*"

    with open(log_file, 'a') as log:
        for entry in network_traffic:
            if re.match(suspicious_pattern, entry):
                log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Alert: Suspicious pattern detected - {entry}\n"
                log.write(log_entry)
                print(log_entry.strip())  # Print the log entry without trailing newline

def main():
    file_path = input("Enter the path of the file containing simulated traffic data (e.g., traffic_data.txt): ")
    network_traffic = read_traffic_data(file_path)

    if not network_traffic:
        print("Exiting. Unable to read simulated traffic data.")
        return

    log_file = "ids_log.txt"
    print(f"Simulating network traffic. Logging alerts to {log_file}...")

    detect_intrusions(network_traffic, log_file)

if __name__ == "__main__":
    main()
