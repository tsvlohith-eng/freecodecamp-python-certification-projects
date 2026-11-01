def hanoi_solver(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []

    moves = [f"{source} {auxiliary} {target}"]

    def solve(num_disks, start, end, temp):
        if num_disks == 1:
            end.append(start.pop())
            moves.append(f"{source} {auxiliary} {target}")
            return

        solve(num_disks - 1, start, temp, end)

        end.append(start.pop())
        moves.append(f"{source} {auxiliary} {target}")

        solve(num_disks - 1, temp, end, start)

    solve(n, source, target, auxiliary)

    return "\n".join(moves)


