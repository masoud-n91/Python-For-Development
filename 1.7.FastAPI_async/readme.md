# OverView

This project consists of several Python scripts that demonstrate various concepts in asynchronous programming.

## 0. Classroom Activity
The 0.ClassroomActivity folder contains two Python scripts that showcase asynchronous programming concepts.

### computer.py:

This script defines three asynchronous functions (download, ai, and printer) that simulate tasks that take random amounts of time to complete. The main function runs these tasks concurrently using asyncio.gather.

### marriage.py:

This script simulates a marriage ceremony where four children get married after random amounts of time. The main function runs the marriage ceremony for each child concurrently using asyncio.create_task.

## 1. asyncAPI

The 1.asyncAPI folder contains a Python script that demonstrates asynchronous API calls using the aiohttp library.

### main.py:

This script defines several asynchronous functions that interact with APIs to retrieve data. The main function runs these functions concurrently using asyncio.gather. The script also uses the requests library to make API calls.

# Running the Scripts

To run the scripts, navigate to the respective folders and execute the Python files using Python 3.x.

## 0.ClassroomActivity: 

Run python computer.py and python marriage.py to execute the scripts.
## 1.asyncAPI: 

Run python main.py to execute the script.

## Note: 
Make sure you have Python 3.x installed and the required libraries installed (e.g., aiohttp, requests) to run the scripts.


