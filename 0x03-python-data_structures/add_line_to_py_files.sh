#!/bin/bash

# Specify the text to add to each .py file
line_to_add="    pass"

# Iterate through all .py files in the current directory
for file in *.py; do
    # Check if the file exists and is a regular file
    if [ -f "$file" ]; then
        # Add the line to the file
        echo "$line_to_add" >> "$file"
        echo "Added line to $file"
    fi
done
