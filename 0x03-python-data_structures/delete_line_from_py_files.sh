#!/bin/bash

# Specify the line to delete from each .py file
line_to_delete="    pass"

# Iterate through all .py files in the current directory
for file in *.py; do
    # Check if the file exists and is a regular file
    if [ -f "$file" ]; then
        # Delete the line from the file
        sed -i "/$line_to_delete/d" "$file"
        echo "Deleted line from $file"
    fi
done
