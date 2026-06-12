from datetime import datetime
import os
import requests


def generate_log(data):
    """
    Generate a log file with the provided data.
    
    Args:
        data: A list of log entries to write to the file
        
    Returns:
        str: The filename of the created log file
        
    Raises:
        ValueError: If data is not a list
    """
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")
    
    return filename


def fetch_api_data():
    """
    Fetch data from JSONPlaceholder API.
    
    Returns:
        dict: The JSON response from the API, or empty dict on failure
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    # Create sample log data
    log_data = ["User logged in", "User updated profile", "Report exported"]
    
    # Generate the log file
    generate_log(log_data)
    
    # Fetch and display API data
    post = fetch_api_data()
    if post:
        print("Fetched Post Title:", post.get("title", "No title found"))
    else:
        print("Failed to fetch data from API")
