#!/usr/bin/env bash                                                                # Specify the interpreter as Bash

version="0.0.1"                                                                    # Set the version number of the script

declare -A alias_to_interpreter=(                                                  # Declare an associative array for
    ["bash"]="bash"                                                                # mapping aliases to interpreters
    ["sh"]="sh"
    ["python"]="python"
)


function find_md_files() {                                                         # Define function to find Markdown files
    local dir="$PWD"                                                               # Start from the current directory
    while [ "$dir" != "/" ]; do                                                    # Loop until reaching the root directory
        find "$dir" -maxdepth 1 -name "*.md"                                       # Find .md files in current dir
        [ "$NO_WALK" = "true" ] && break                                           # Stop if NO_WALK is set to true
        dir=$(dirname "$dir")                                                      # Move up one directory level
    done
}

function parse_md_file() {                                                         # Define function to parse Markdown file
    local file="$1"                                                                # Get the file path as an argument
    local in_code_block=false                                                      # Flag to track if inside a code block
    while IFS= read -r line; do                                                    # Read the file line by line
        if [[ "$line" =~ ^## ]]; then                                              # Check if line starts with ##
            command=$(echo "$line" | sed -n 's/## \[\(.*\)\].*/\1/p')              # Extract command name
            echo "Command found: $command"                                         # Print the found command
        elif [[ "$line" =~ ^\`\`\` ]]; then                                        # Check for code block delimiter
            in_code_block=$(! $in_code_block)                                      # Toggle code block flag
        elif $in_code_block; then                                                  # If inside a code block
            echo "Script line: $line"                                              # Print the script line
        fi
    done < "$file"                                                                 # Read from the specified file
}

find_md_files                                                                      # Call the function to find Markdown files
