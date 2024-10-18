#!/usr/bin/env bash

VERSION="0.0.9"

function print_makedown_help {
  echo "TODO"
  echo "TODO"
  echo "TODO"
  echo "TODO"
  echo "TODO"
  echo "TODO"
}

function print_version {
  echo $VERSION
}

function find_md_files {
  local current_dir=$(pwd)
  while true; do
    find "$current_dir" -maxdepth 1 -type f | \
      sed -n '/\.[mM][dD]$/p' | \
      sort | \
      while read -r file; do
        echo "$file"
    done
    parent_dir=$(dirname "$current_dir")
    [ "$parent_dir" = "$current_dir" ] && break
    current_dir=$parent_dir
  done
}

COMMAND_REGEX="[a-zA-Z0-9_:-]+"

function find_commands {
  find_md_files | while read -r file; do
    local line_number=0
    cat "$file" | while IFS= read -r line; do
      ((line_number++))
      if [[ $line =~ ^(#+)[[:space:]]+(${COMMAND_REGEX})[[:space:]]*#(.*)$ ]]; then
        local level=${BASH_REMATCH[1]}
        local name="${BASH_REMATCH[2]}"
        local description=$(echo "${BASH_REMATCH[3]}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
        echo "$file|$line_number|$level|$name|$description"
      fi
    done
  done
}

function print_commands_help {
  echo "Usage:"
  echo
  echo "    $ $(blue "makedown") <command> foo bar # execute the command"
  echo "    $ $(blue "m") <command> --help         # short version, print help"

  longest=0
  while IFS='|' read -r file line_number level name description; do
    if [ "$description" = "hide" ]; then
      continue
    fi
    local prefix="$level $name"
    if ((${#prefix} > longest)); then
      longest=${#prefix}
    fi
  done < <(find_commands)

  local prevFile=""
  while IFS='|' read -r file line_number level name description; do
    if [ "$description" = "hide" ]; then
      continue
    fi
    if [ "$file" != "$prevFile" ]; then
      printf "\n%s\n" "$(green "$(bold "$file")")"
      prevFile="$file"
    fi
    local level_spaces=$(printf "%*s" $((longest - ${#name} - ${#level} - 1 )) "")
    printf "%s %s %s   # %s\n" $(yellow "$level") "$(blue "$name")"  "$level_spaces" "$description"
  done < <(find_commands)
}

function print_command_help {
  printf "command help: %1\n"
}

function execute_command {
  while IFS='|' read -r file line_number level name description; do
    local prefix="$level $name"
    if ((${#prefix} > longest)); then
      longest=${#prefix}
    fi
  done < <(find_commands)
}

function check_duplicates {
  echo "TODO: check_duplicates"
}

function check {
  check_duplicates
}

function red {
  printf "\033[31m%s\033[0m" "$1"
}

function blue {
  printf "\033[34m%s\033[0m" "$1"
}

function green {
  printf "\033[32m%s\033[0m" "$1"
}

function yellow {
  printf "\033[33m%s\033[0m" "$1"
}

function magenta {
  printf "\033[35m%s\033[0m" "$1"
}

function cyan {
  printf "\033[36m%s\033[0m" "$1"
}

function bold {
  printf "\033[1m%s\033[0m"  "$1"
}

function underline {
  printf "\033[4m%s\033[0m"  "$1"
}

function main {
    if [ $# -eq 0 ] || [ "$1" = "-c" ] || [ "$1" = "--commands" ]; then
        check
        print_commands_help
    elif [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
        print_makedown_help
    elif [ "$1" = "--version" ] || [ "$1" = "-v" ]; then
        print_version
    elif [ $# -eq 2 ] && [ "$2" = "--help" ]; then
        check
        print_command_help "$1"
    else
        check
        execute_command "$*"
    fi
}

main "$@"
