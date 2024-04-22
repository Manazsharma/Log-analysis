import time
import logging
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def monitor_log_file(file_path):
    try:
        with open(file_path, 'r') as log_file:
            # Move to the end of the file
            log_file.seek(0, 2)
            
            while True:
                line = log_file.readline()
                if not line:
                    time.sleep(1)  # Wait for a short interval before checking for new lines
                else:
                    process_log_entry(line)
    
    except KeyboardInterrupt:
        logging.info("Log monitoring interrupted. Exiting.")
    except FileNotFoundError:
        logging.error(f"Log file '{file_path}' not found.")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

def process_log_entry(log_entry):
    
    logging.info(f"New log entry: {log_entry.strip()}")
    
    # Perform analysis on the log entry
    # Count occurrences of specific keywords or patterns
    keywords = ['error', 'warning', 'critical']
    keyword_counts = Counter(keyword for keyword in keywords if keyword in log_entry.lower())
    
    # summary report
    if keyword_counts:
        logging.info("Keyword counts:")
        for keyword, count in keyword_counts.items():
            logging.info(f"{keyword}: {count}")

if __name__ == '__main__':
    log_file_path = 'app.log'  # Replace with the path to your log file
    monitor_log_file(log_file_path)
