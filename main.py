import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the window title
        self.setWindowTitle('Calculator')
        # Create a grid layout and add it to the widget
        grid = QGridLayout()
        self.setLayout(grid)

        # Create a line edit for displaying the result
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Add the display to the top row of the grid
        grid.addWidget(self.display, 0, 0, 1, 5)

        # Create the buttons and add them to the grid
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(1, 6) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            # Customize the button's appearance
            button.setStyleSheet('QPushButton {background-color: #ddd; font-size: 20px;}')
            grid.addWidget(button, *position)
            button.clicked.connect(self.buttonClicked)

        # Create the square root button
        sqrt_button = QPushButton('√')
        grid.addWidget(sqrt_button, 1, 4)
        sqrt_button.clicked.connect(self.handleSqrt)

        # Create the logarithm button
        log_button = QPushButton('log')
        grid.addWidget(log_button, 2, 4)
        log_button.clicked.connect(self.handleLog)
            
        # Set some initial state for the calculator
        self.clear()

    def buttonClicked(self):
        # Get the sender of the signal (i.e., the button that was clicked)
        button = self.sender()
        # Get the button's text
        button_text = button.text()

        # Handle the different types of buttons
        if button_text == 'Cls':
            self.clear()
        elif button_text == 'Bck':
            self.backspace()
        elif button_text == 'Close':
            self.close()
        elif button_text in '+-*/':
            self.handleOperator(button_text)
        elif button_text == '=':
            self.handleEquals()
        else:
            self.display.setText(self.display.text() + button_text)

    def clear(self):
        # Clear the display and reset the last operator
        self.display.setText('')
        self.last_operator = None

    def backspace(self):
        # Get the current text in the display
        text = self.display.text()
        # Set the display text to be everything except the last character
        self.display.setText(text[:-1])

    def handleOperator(self, operator):
        # If there is a previous operator, handle the previous operation first
        if self.last_operator:
            self.handleEquals()
        # Set the last operator to the new operator
        self.last_operator = operator
        # Store the current operand in memory
        self.last_operand = float(self.display.text())
        # Clear the display
        self.display.setText('')

    def handleEquals(self):
        # Get the current operand from the display
        operand = float(self.display.text())
        # Perform the operation based on the last operator
        if self.last_operator == '+':
            result = self.last_operand + operand
        elif self.last_operator == '-':
            result = self.last_operand - operand
        elif self.last_operator == '*':
            result = self.last_operand * operand
        elif self.last_operator == '/':
            result = self.last_operand / operand
        # If there is no last operator, the result is just the current operand
        else:
            result = operand
        # Display the result and reset the last operator
        self.display.setText(str(result))
        self.last_operator = None

    def handleSqrt(self):
        # Get the current operand from the display
        operand = float(self.display.text())
        # Calculate the square root of the operand
        result = math.sqrt(operand)
        # Display the result
        self.display.setText(str(result))

    def handleLog(self):
        # Get the current operand from the display
        operand = float(self.display.text())
        # Calculate the logarithm of the operand
        result = math.log10(operand)
        # Display the result
        self.display.setText(str(result))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())