# Encoded events
EVENTS = {
    0: "Admit",
    1: "Activate",
    2: "Execute",
    3: "Suspend",
    4: "I/O Request",
    5: "I/O Completed",
    6: "Quantum ended",
    7: "Exit"
}

# Encoded states
STATES = {
    0: "New",
    1: "Ready",
    2: "Ready & Suspended",
    3: "Executing",
    4: "Blocked",
    5: "Blocked & Suspended",
    6: "Completed"
}

# δ: Map (current_state, event) --> next_state
TRANSITIONS = {
    (0, 0): 1,  # New --Admit--> Ready

    (1, 2): 3,  # Ready --Execute--> Executing
    (1, 3): 2,  # Ready --Suspend--> Ready & Suspended

    (2, 1): 1,  # Ready & Suspended --Activate--> Ready

    (3, 4): 4,  # Executing --I/O Request--> Blocked
    (3, 6): 1,  # Executing --Quantum ended--> Ready
    (3, 7): 6,  # Executing --Exit--> Completed

    (4, 3): 5,  # Blocked --Suspend--> Blocked & Suspended
    (4, 5): 1,  # Blocked --I/O Completed--> Ready

    (5, 1): 4,  # Blocked & Suspended --Activate--> Blocked
    (5, 5): 2   # Blocked & Suspended --I/O Completed--> Ready & Suspended
}

# g: MAP (current_state, event) --> output text
OUTPUTS = {
    (0, 0): "Process admitted",

    (1, 2): "Executing process",
    (1, 3): "Process suspended",

    (2, 1): "Reactivating process",

    (3, 4): "I/O Request",
    (3, 6): "Quantum completed",
    (3, 7): "Process completed",

    (4, 3): "Process suspended",
    (4, 5): "I/O Completed",

    (5, 1): "Reactivating process",
    (5, 5): "I/O Completed"
}


class FSMProcess:
    def __init__(self):
        self.state = 0

    def on_event(self, ev: int):
        """Processes an event ev (code 0–7)."""
        if ev not in EVENTS:
            raise ValueError(f"Unknown event: {ev}")

        key = (self.state, ev)
        if key not in TRANSITIONS:
            print(f"Invalid transition: {STATES[self.state]} + {EVENTS[ev]}")
            return

        # output message
        msg = OUTPUTS.get(key)
        # next state
        next_state = TRANSITIONS[key]

        # print log
        print(f"Event   : {ev} – {EVENTS[ev]}")
        if msg:
            print(f"Action  : {msg}")
        print(f"{STATES[self.state]} → {STATES[next_state]}\n")

        # update state
        self.state = next_state

    def current_state(self):
        return self.state, STATES[self.state]


if __name__ == "__main__":
    fsm = FSMProcess()

    # Testing sequence, can be changed for any desired input
    string = [0, 2, 6, 2, 4, 5, 2, 7]
    
    for ev in string:
        fsm.on_event(ev)