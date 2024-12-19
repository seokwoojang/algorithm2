def sol(N):
    answer = []

    def dfs(s, start, current_Sum):
        if current_Sum == 10:
            answer.append(s[:])
            return
        
        if current_Sum > 10:
            return
        
        for i in range(start, N + 1):
            if current_Sum + i <= 10:
                s.append(i)
                dfs(s, i + 1, current_Sum + i)
                s.remove(i)

    dfs([], 1, 0)

    return answer

print(sol(5))
print(sol(2))
print(sol(7))