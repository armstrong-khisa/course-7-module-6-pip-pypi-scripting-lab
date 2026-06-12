"""
Root-level re-export of generate_log module for convenience.
The actual implementation is in lib/generate_log.py
"""

from lib.generate_log import generate_log, fetch_api_data

__all__ = ["generate_log", "fetch_api_data"]

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
