from collections import deque

def waterJugSolverBFS(jug1, jug2, aim):
    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    parents = {}

    while queue:
        current_state = queue.popleft()
        amt1, amt2 = current_state

        if amt1 == aim or amt2 == aim:
            steps = []
            while current_state != (0, 0):
                steps.append(current_state)
                current_state = parents[current_state]
            steps.append((0, 0))
            steps.reverse()
            return steps

        next_states = [
            (jug1, amt2),  
            (amt1, jug2),  
            (0, amt2),     
            (amt1, 0),     
            (min(jug1, amt1 + amt2), max(0, amt1 + amt2 - jug1)),  
            (max(0, amt1 + amt2 - jug2), min(jug2, amt1 + amt2))   
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                parents[state] = current_state
    return None

jug1 = int(input("Enter the size for the first jug : "))
jug2 = int(input("Enter the size for the second jug : "))
finalQuantity = int(input("Enter the water to collect : "))

solution = waterJugSolverBFS(jug1, jug2, finalQuantity)
numberOfSteps=0
if solution:
    for step in solution:
        numberOfSteps=numberOfSteps+1
        print(step)
    print("Number of steps needed are: ",len(solution)-1)
else:
    print("No solution found.")
