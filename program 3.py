from collections import deque

def water_jug():
    visited = set()
    queue = deque([(0, 0)])  # Initial state: both jugs empty

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print(x, y)

        # Goal condition: get 2L in either jug
        if x == 2 or y == 2:
            print("Goal Reached")
            return

        # Fill 4L jug
        queue.append((4, y))

        # Fill 3L jug
        queue.append((x, 3))

        # Empty 4L jug
        queue.append((0, y))

        # Empty 3L jug
        queue.append((x, 0))

        # Pour water from 4L jug to 3L jug
        pour = min(x, 3 - y)
        queue.append((x - pour, y + pour))

        # Pour water from 3L jug to 4L jug
        pour = min(y, 4 - x)
        queue.append((x + pour, y - pour))


water_jug()
