# log-insight

*This is a submission for the [Amazon Q Developer "Quack The Code" Challenge](https://dev.to/challenges/aws-amazon-q-v2025-04-30): Crushing the Command Line*

## What I Built

I built a command-line tool called `log-insight` to help developers and system administrators quickly analyze log files. Log files are like digital diaries that record what a computer system or application is doing, and they can become very large and difficult to navigate. `Log-insight` automates extracting key information from these files, making it easier to identify errors, understand system behavior, and troubleshoot problems.

Specifically, `log-insight` provides the following functionalities:

* **Keyword Counting:** Counts the number of times a specific keyword appears in the log file. This is useful for quickly assessing the frequency of particular events, such as errors, warnings, or successful operations. Users can specify the keyword they want to search for.
* **Top Entry Analysis:** Identifies and displays the most frequent log entries. This helps in understanding recurring patterns and identifying the most common activities or issues within the system. The number of top entries to display is configurable.
* **Error Timestamp Extraction:** Extracts and lists the timestamps of log entries that contain a specific error keyword (e.g., "error", but this can be customized). This allows users to quickly pinpoint when errors occurred, which is crucial for debugging and incident analysis.

`log-insight` aims to "crush the command line" by providing a simple, efficient, and scriptable way to gain valuable insights from log data, directly from the terminal. It eliminates the need for manual searching and complex text processing, saving time and improving productivity.

## Demo

[Demo Video Link]


## Code Repository

https://github.com/shittuay/log-insight.git


## How I Used Amazon Q Developer

I used Amazon Q Developer as an invaluable assistant throughout the development process of `log-insight`. It significantly accelerated my workflow in several ways:

* **Code Snippet Generation:** Amazon Q helped me quickly generate efficient code snippets for core functionality like file reading, text processing, and handling command-line arguments, saving me substantial development time.

* **Library Implementation:** When implementing the argparse library for command-line arguments and regex patterns for log parsing, Amazon Q provided clear examples and implementation guidance that streamlined the development process.

* **Debugging Support:** Whenever I encountered errors or unexpected behavior, Amazon Q helped identify root causes and suggested practical solutions, particularly for complex regex patterns and file handling edge cases.

* **Best Practices:** Amazon Q provided guidance on writing clean, Pythonic code, ensuring that `log-insight` remains maintainable and follows industry standards.

Specifically, Amazon Q was instrumental in:
- Developing efficient file reading mechanisms that could handle large log files
- Creating optimized keyword searching algorithms that maintain performance even with massive logs
- Structuring the command-line interface to be intuitive and following Unix philosophy
- Implementing proper error handling for various edge cases

Amazon Q Developer proved to be like having an expert pair programmer available 24/7, offering suggestions, improvements, and solutions throughout the entire development cycle.

