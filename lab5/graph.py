import heapq
import sys
from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def read_board(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            board = [line.strip() for line in f if line.strip()]
            board = [row.replace(' ', '') for row in board] 
            
            if not board:
                return []
            
            return board
        
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{filename}'.")
        sys.exit(1)

# According to the content, the correctness of the input file can be assumed,
# therefore it was assumed that the boards were prepared in accordance with the guidelines.

def search_x_in_board(board):
    x = []
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'X':
                x.append((r, c))
    
    if len(x) < 2:
        sys.exit(1)
        
    return x[0], x[1]

def transition_cost(board, from_position, to_position):
    from_row, from_col = from_position
    to_row, to_col = to_position

    target_char = board[to_row][to_col]
    source_char = board[from_row][from_col]

    if source_char == 'J':
        return 0
    if target_char == 'J' or target_char == 'X': 
        return 0
    
    if target_char.isdigit():
        cost = int(target_char)
        return cost
    
    return 0
    
get_cost = transition_cost
    
def shortest_path_dijkstra(board, start_pos, end_pos):
    rows = len(board)
    cols = len(board[0])

    dist = {}
    prev_on_path = {}

    pq = [(0, start_pos)]
    dist[start_pos] = 0

    while pq:
        current_cost, current_pos = heapq.heappop(pq)
        r, c = current_pos

        if current_cost > dist.get(current_pos, float('inf')):
            continue

        if current_pos == end_pos:
            break

        for dr, dc in DIRECTIONS:
            next_pos = (r + dr, c + dc)
            next_r, next_c = next_pos

            if 0 <= next_r < rows and 0 <= next_c < cols:
                move_cost = get_cost(board, current_pos, next_pos) 
                new_cost = current_cost + move_cost

                if new_cost < dist.get(next_pos, float('inf')):
                    dist[next_pos] = new_cost
                    prev_on_path[next_pos] = current_pos
                    heapq.heappush(pq, (new_cost, next_pos))

    path = []
    current = end_pos
    total_cost = dist.get(end_pos, float('inf'))
    
    if total_cost == float('inf'):
        return float('inf'), []

    while current is not None:
        path.append(current)
        if current == start_pos:
            break
        current = prev_on_path.get(current)
    
    path.reverse()
    return total_cost, path

def display_result(board, path, total_cost):
    rows = len(board)
    cols = len(board[0])

    path_set = set(path)
    print("\n--- Wynik ---")

    for r in range(rows):
        row_str = ""
        for c in range(cols):
            if (r, c) in path_set:
                row_str += board[r][c]
            else:
                row_str += ' '
        print("    ", row_str) 

    
    print(f"\nKoszt: {total_cost}")
    print("-------------")

def main():
    if len(sys.argv) != 2:
        print("Użycie: python wyniki.py board_7x6.txt")
        sys.exit(1)
    
    filename = sys.argv[1]

    board = read_board(filename)
    if not board:
        sys.exit(1)
        
    start_pos, end_pos = search_x_in_board(board)
    total_cost, path = shortest_path_dijkstra(board, start_pos, end_pos)

    if total_cost != float('inf'):
        display_result(board, path, total_cost)
    else:
        print("\nNie znaleziono ścieżki między dwoma 'X'.")
        
if __name__ == "__main__":
    main()