alias colbp='colcon build --symlink-install --packages-select'
alias colbup='colcon build --symlink-install --packages-up-to'
alias colb='colcon build --symlink-install'
alias ducks='du -ah . | sort -n -r | head -n 20'
alias dka='docker kill $(docker ps -q)'

fortune | cowsay | lolcat # :)

function findd() { 
    if [ "$#" == 1 ]; then
        find / -type d -name "$1" 2> /dev/null;
    elif [ "$#" == 2 ]; then
        find "$1" -type d -name "$2" 2> /dev/null;
    fi
}

function findf() { 
    if [ "$#" == 1 ]; then
        find / -type f -name "$1" 2> /dev/null;
    elif [ "$#" == 2 ]; then
        find "$1" -type f -name "$2" 2> /dev/null;
    fi
}
