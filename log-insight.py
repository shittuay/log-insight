import argparse
from collections import Counter
import re  # Import the regular expression module

def read_log_file(file_path):
    """
    This function opens a log file and reads all the lines in it.

    Args:
        file_path: The location of the log file on the computer.

    Returns:
        A list where each item is a line from the log file. Returns an empty list on error.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Oops! The file at '{file_path}' doesn't exist. Double-check the name!")
        return []

def count_keywords(lines, keyword):
    """
    This function counts the number of times a specific keyword appears in a list of lines.

    Args:
        lines: A list of strings, where each string is a line from the log file.
        keyword: The keyword to search for.

    Returns:
        The number of times the keyword appears in the lines.
    """
    count = 0
    for line in lines:
        if keyword in line:
            count += 1
    return count

def get_top_entries(lines, num_top=5):
    """
    This function finds the most frequent log entries.

    Args:
        lines: A list of strings, where each string is a line from the log file.
        num_top: The number of top entries to return (default: 5).

    Returns:
        A list of tuples, where each tuple contains (line, count), sorted in descending order of count.
        Returns an empty list if input lines is empty.
    """
    if not lines:
        return []
    line_counts = Counter(lines)  # Count occurrences of each line
    top_entries = line_counts.most_common(num_top)  # Get the top N entries
    return top_entries

def extract_error_timestamps(lines, error_keyword="ERROR"):
    """
    This function extracts timestamps from log entries that contain a specific error keyword.

    Args:
        lines: A list of strings, where each string is a line from the log file.
        error_keyword: The keyword to identify error entries (default: "ERROR").

    Returns:
        A list of (timestamp, line) tuples, where timestamp is extracted from the line.
        Returns an empty list if no errors are found or timestamp format is invalid.
    """
    error_timestamps = []
    timestamp_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"  # Regex for timestamp
    for line in lines:
        if error_keyword in line:
            match = re.search(timestamp_pattern, line)
            if match:
                timestamp = match.group(1)  # Extract the timestamp string
                error_timestamps.append((timestamp, line))
    return error_timestamps

def main():
    """
    This is the main function that parses command-line arguments, reads the log file,
    counts keywords, finds top entries, extracts error timestamps, and prints the results.
    """
    parser = argparse.ArgumentParser(description="Analyze log files for keyword counts, top entries, and error timestamps.")
    parser.add_argument("file_path", help="The path to the log file.")
    parser.add_argument("keyword", help="The keyword to search for.")
    parser.add_argument("-t", "--top", type=int, default=5,
                        help="The number of top log entries to display (default: 5).")
    parser.add_argument("-e", "--error_keyword", default="ERROR",
                        help="The keyword to identify error log entries (default: 'ERROR').")

    args = parser.parse_args()

    log_file_path = args.file_path
    keyword = args.keyword
    num_top = args.top
    error_keyword = args.error_keyword

    log_lines = read_log_file(log_file_path)
    if not log_lines:
        return

    keyword_count = count_keywords(log_lines, keyword)
    print(f"The keyword '{keyword}' appears {keyword_count} times in the log file.")

    top_entries = get_top_entries(log_lines, num_top)
    print(f"\nTop {num_top} most frequent log entries:")
    if top_entries:
        for line, count in top_entries:
            print(f"  {count}: {line.strip()}")
    else:
        print("  No log entries to display.")

    error_timestamps = extract_error_timestamps(log_lines, error_keyword)
    print(f"\nError timestamps (entries containing '{error_keyword}'):")
    if error_timestamps:
        for timestamp, line in error_timestamps:
            print(f"  {timestamp}: {line.strip()}")
    else:
        print(f"  No entries containing '{error_keyword}' found.")

if __name__ == "__main__":
    main()
