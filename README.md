# Log Analysis and Monitoring Script

This script automates the analysis and monitoring of log files. It continuously monitors a specified log file for new entries and performs basic analysis on the log entries.

## Features

- Real-time monitoring of log files
- Keyword-based analysis of log entries
- Summary reports of keyword occurrences
- Graceful handling of interrupts and errors

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:
```
git clone https://github.com/Manazsharma/Log-analysis
```

2. Open a terminal and navigate to the directory containing the `log-monitor.py` file.
   
3. Run the script using the following command:
   ```
   python log-monitor.py
   ```
   
4. The script will start monitoring the specified log file and display new log entries in real-time.

5. Press `Ctrl+C` to stop the monitoring process.

## Customization

- Modify the `process_log_entry` function to implement additional analysis logic based on your specific requirements.
- Adjust the `keywords` list in the `process_log_entry` function to include relevant keywords or patterns for your log analysis.

## Error Handling

The script includes error handling for the following scenarios:
- Keyboard interrupts (e.g., pressing `Ctrl+C`) to stop the monitoring process
- File not found errors if the specified log file does not exist
- General exceptions to catch and log any unexpected errors

## Additional Features
- **Error Message Counting**: The script counts the occurrences of error messages in the log entries.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


