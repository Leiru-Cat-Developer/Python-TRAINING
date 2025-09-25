# Do BFS search
def bfs(adj):
    v = len(adj)
    s = 2
    result = []

    print(f"\nAJD LEN: {v} \nS value: {s} \nResult array: {result}\n")

    from collections import deque
    dq = deque()
    visited = [False] * v

    print(f"Deque init: {dq} \nVisited array: {visited}\n")

    visited[s] = True
    dq.append(s)

    print(f"Visited array with S: {visited} \nDeque first append: {dq}\n\n")

    while dq:
        current = dq.popleft()
        result.append(current)

        print(f"Current: {current} | Result until here: {result}")

        for x in adj[current]:
            print(f"\n\nDuring the {x} iteration, ADJ[current]: {adj[current]}")
            if not visited[x]:
                print(f"Visited before: {visited[x]}")
                visited[x] = True
                print(f"Visited after: {visited[x]}")
                print(f"Dp before: {dq}")
                dq.append(x)
                print(f"Dp after: {dq}")
        print("\n")
    print(f"\nEND VALUES \n\nAJD LEN: {v} \nS value: {s} \nResult array: {result}\n")
    return result

adj = [
    [1,2],
    [0,2,3],
    [0,1,4],
    [1,4],
    [2,3]
]

print(f"FINAL RESULT: {bfs(adj)}\n")