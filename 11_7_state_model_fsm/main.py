import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidget
from gui import Ui_MainWindow
from source import FSMProcess, OUTPUTS, STATES, EVENTS, TRANSITIONS

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # FSM
        self.fsm = FSMProcess()

        # Create QListWidget dynamically in the listView
        self.log_display = QListWidget()
        self.ui.listView.setViewport(self.log_display)

        # Button events
        self.ui.pushButton.setText("Enter Input")
        self.ui.pushButton.clicked.connect(self.enter_event)

        self.ui.pushButton_2.setText("Reset")
        self.ui.pushButton_2.clicked.connect(self.reset_fsm)

        self.update_visual_state()
        self.show_available_options()

    def enter_event(self):
        self.log_display.clear()
        input_text = self.ui.textEdit.toPlainText().strip()
        if not input_text.isdigit():
            QMessageBox.warning(self, "Invalid input", "Enter an integer from 0 to 7.")
            return

        event = int(input_text)
        current_state = self.fsm.estado

        if (current_state, event) not in TRANSITIONS:
            QMessageBox.warning(self, "Invalid transition",
                                f"The event '{EVENTS.get(event, '?')}' cannot be applied in the current state '{STATES[current_state]}'.")
            return

        next_state = TRANSITIONS[(current_state, event)]
        action = OUTPUTS.get((current_state, event), "")
        transition_text = f"{STATES[current_state]} -> {STATES[next_state]}"
        event_text = f"Event   : {event} - {EVENTS[event]}"
        action_text = f"Action  : {action}" if action else "Action  : (no action)"

        # Execute transition
        self.fsm.on_event(event)

        # Show details in log
        self.log_display.addItem(event_text)
        self.log_display.addItem(action_text)
        self.log_display.addItem(transition_text)
        self.log_display.addItem("-" * 40)

        # Update visualization
        self.update_visual_state()
        self.ui.textEdit.clear()

        # Show current state and available options
        self.show_available_options()

    def reset_fsm(self):
        self.fsm = FSMProcess()
        self.log_display.clear()
        self.update_visual_state()
        self.show_available_options()

    def update_visual_state(self):
        """Displays the current state in the interface labels."""
        state = self.fsm.estado

        # Clear all labels
        self.ui.label.setText("")
        self.ui.label_3.setText("")
        self.ui.label_5.setText("")
        self.ui.label_6.setText("")

        # Show current state with icons
        if state == 0:  # New
            self.ui.label_5.setText("New 🆕")
        elif state == 1:  # Ready
            self.ui.label_3.setText("Ready ✅")
        elif state == 2:  # Ready & Suspended
            self.ui.label.setText("Ready & Suspended ✅😴")
        elif state == 3:  # Executing
            self.ui.label_3.setText("Executing 🏃")
        elif state == 4:  # Blocked
            self.ui.label_3.setText("Blocked 🔒")
        elif state == 5:  # Blocked & Suspended
            self.ui.label.setText("Blocked & Suspended 🔒😴")
        elif state == 6:  # Completed
            self.ui.label_6.setText("Completed 💀")

    def show_available_options(self):
        """Displays in the log the possible transitions from the current state."""
        state = self.fsm.estado
        self.log_display.addItem(f"Current state: {STATES[state]}")
        possibles = [f"{k[1]}: {STATES[k[1]]}" for k in TRANSITIONS if k[0] == state]
        if possibles:
            self.log_display.addItem("Available options:")
            for p in possibles:
                self.log_display.addItem(f"  - {p}")
        self.log_display.addItem("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())