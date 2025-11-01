#!/bin/bash

# Find the PID of launcher.py
PID=$(pgrep -f launcher.py)

if [ -z "$PID" ]; then
    echo "launcher.py is not running."
else
    echo "Killing launcher.py (PID $PID)..."
    kill $PID
    sleep 1
    # Check if it's really gone
    if ps -p $PID > /dev/null; then
        echo "Process did not exit, forcing kill..."
        kill -9 $PID
    else
        echo "launcher.py terminated successfully."
    fi
fi

