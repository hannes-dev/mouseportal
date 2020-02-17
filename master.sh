while true; do
    echo `xdotool getmouselocation | sed -e "s/^x:\([0-9]\+\) y:\([0-9]\+\) .*$/\1:\2/"`
done | nc $1 42333
