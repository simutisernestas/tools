alias colbp='colcon build --symlink-install --packages-select'
alias colb='colcon build --symlink-install'
alias ducks='du -ah . | sort -n -r | head -n 20'
fortune | cowsay | lolcat # :)
function findd() { find / -type d -name "$1" 2> /dev/null; }
function findf() { find / -type f -name "$1" 2> /dev/null; }
