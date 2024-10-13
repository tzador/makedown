# BEGIN XFile completions

function _x_completion {
  local -a options
  options=(${(f)"$(x __list_commands 2>/dev/null)"})
  _describe "choices" options
}

compdef _x_completion x

# END XFile completions
