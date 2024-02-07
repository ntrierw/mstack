import re

def run(html):
    # Define the custom string to add
    start = "<i>"
    end = "</i>"

    # Define the regex pattern to match
    pattern = r"(\w+\s\w+)\s\|\s(\d+/\d+/\d+)"

    # Use the re.sub function to replace the matched parts with the custom text
    result = re.sub(pattern, start + r"\1" + "|" + r"\2" + end, html)
    return result
