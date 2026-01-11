# Turing Machine Simulator

import sys



# reads the tape contents and the transition function

def readfile(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return lines


def load_transitions(filename):
    transitions = {}
    lines = readfile(filename)

    for line in lines:
        line = line.strip()       
        if not line:              
            continue

        parts = line.split()
        if len(parts) != 5:
            raise ValueError(f"Niepoprawna linia w pliku: {line}")

        state, symbol, new_symbol, direction, new_state = parts
        key = (state, symbol)

        action = {
            "new_symbol": new_symbol,
            "direction": direction,
            "new_state": new_state
        }

        if key not in transitions:
            transitions[key] = []

        transitions[key].append(action)

    return transitions




# displays the contents of the tape, the position of the head

def print_config(tape, head, state):
    print("".join(tape), state)
    print(" " * head + "^")



# finds and displays the sequence of changes in tape content, head position and status
def step(tape, head, state, transitions):
    results = []
    symbol = tape[head]

    key = (state, symbol)
    if key not in transitions:
        return results

    for action in transitions[key]:  # teraz action jest słownikiem
        new_tape = tape.copy()
        new_head = head

        new_tape[head] = action["new_symbol"]

        direction = action["direction"]
        if direction == 'R':
            new_head += 1
        elif direction == 'L':
            new_head -= 1
        # '*' → brak ruchu, new_head pozostaje

        if new_head < 0:
            new_tape.insert(0, '_')
            new_head = 0
        elif new_head >= len(new_tape):
            new_tape.append('_')

        results.append((new_tape, new_head, action["new_state"]))

    return results

def simulate(transitions, input_tape):
    start_tape = list(input_tape)
    start = (start_tape, 0, "init", [(start_tape, 0, "init")])

    stack = [start]

    while stack:
        tape, head, state, history = stack.pop()

        if state.startswith("halt"):
            return history

        for new_tape, new_head, new_state in step(tape, head, state, transitions):
            new_history = history + [(new_tape, new_head, new_state)]
            stack.append((new_tape, new_head, new_state, new_history))

    return None

def main():
    tape_input = sys.argv[1]
    filename = sys.argv[2]

    transitions = load_transitions(filename)
    history = simulate(transitions, tape_input)

    if history is None:
        print("Brak stanu halt")
        return

    for tape, head, state in history:
        print_config(tape, head, state)


if __name__ == "__main__":
    main()





        