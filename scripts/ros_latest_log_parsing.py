import sys

# cat `ls -tr ~/.ros/log/planner_server_* | tail -n 1` | grep "Map update" | python avg.py

i = 1
s = 0.0
for line in sys.stdin:
    elements = line.split(' ')
    update_delta = float(elements[-1])
    s += update_delta
    i += 1
print(f"avg: {s/i} from {i} samples")