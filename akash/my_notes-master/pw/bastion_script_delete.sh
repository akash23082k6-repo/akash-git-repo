#!/bin/bash

# Function to recursively delete files larger than 10MB
delete_large_files() {
    local target="$1"
    # Loop through items in the target directory
    for item in "$target"/*; do
        if [ -d "$item" ]; then
            # If the item is a directory, recursively call delete_large_files function
            delete_large_files "$item"
        elif [ -f "$item" ] && [ "$(stat --printf='%s' "$item")" -gt 10485760 ]; then
            # If the item is a file and larger than 10MB, delete it
            rm "$item"
            echo "Deleted file: $item"
        fi
    done
}

# Loop through all user directories in /home except root
for user_dir in /home/*; do
    # Check if the current item is a directory and skip if it's not
    if [ -d "$user_dir" ]; then
        user=$(basename "$user_dir")
        if [ "$user" != "root" ]; then
            # Call delete_large_files function for the user's home directory
            delete_large_files "$user_dir"
        fi
    fi
done
