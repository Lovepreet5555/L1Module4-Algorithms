from collections import deque
initial_state = (3, 3, 1) 
goal_state = (0, 0, 0)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def is_valid(state):
    m_left, c_left, _ = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if (m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0):
        return False
    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False 
    return True

def bfs():
    queue = deque([(initial_state, [])]) 
    visited = set()

    while queue:
        (m_left, c_left, boat), path = queue.popleft()

        if (m_left, c_left, boat) == goal_state:
            path.append((m_left, c_left, boat))
            print("Solution Reached:")
            for step in path:
                print(step)
            print(f" Total steps needed to reach the final state:,{len(path)-1}")
            return

        if (m_left, c_left, boat) in visited:
            continue
        visited.add((m_left, c_left, boat))

        for m_move, c_move in moves:
            if boat == 1:  # Boat on the left =p
                new_state = (m_left - m_move, c_left - c_move, 0)
            else:  # Boat on the right
                new_state = (m_left + m_move, c_left + c_move, 1)

            if is_valid(new_state):
                queue.append((new_state, path + [(m_left, c_left, boat)]))
    print("No solution found")

bfs()

