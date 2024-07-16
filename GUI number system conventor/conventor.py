import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

# Conversion functions
def reverse(s):
    return s[::-1]

# Demical to (binary, octal, hexadecimal)
def demical_to_hexadecimal(num):
    num = int(num)
    hex_values = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    answer = ""
    while num != 0:
        if num % 16 < 10:
            i = str(num % 16)
        else:
            i = hex_values[num % 16]
        num = num // 16
        answer += i
    return reverse(answer)

def demical_to_binary(num):
    num = int(num)
    answer = ""
    while num > 0:
        answer += str(num % 2)
        num = num // 2
    return reverse(answer)

def demical_to_octal(num):
    num = int(num)
    answer = ""
    while num > 0:
        answer += str(num % 8)
        num = num // 8
    return reverse(answer)

# (binary, octal, hexadecimal) to decimal

def binary_to_decimal(num):
    return int(str(num), 2)

def octal_to_decimal(num):
    return int(str(num), 8)

def hexadecimal_to_decimal(num):
    hex_values = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    num = str(num)
    for i in num:
        if i in hex_values.values():
            j = int(str(list(hex_values.keys())[list(hex_values.values()).index(i)]))
            num = num.replace(i, "0")
            num = num.removesuffix(i)
            num = int(str(num), 16) + int(j)
            return num
        else:
            return int(str(num), 16)

# binary to (hexadecimal, octal)

def binary_to_octal(num):
    return demical_to_octal(binary_to_decimal(num))

def binary_to_hexadecimal(num):
    return demical_to_hexadecimal(binary_to_decimal(num))

# octal to (binary, hexadecimal)

def octal_to_binary(num):
    return demical_to_binary(octal_to_decimal(num))

def octal_to_hexadecimal(num):
    return demical_to_hexadecimal(octal_to_decimal(num))

# hexadecimal to (binary, octal)

def hexadecimal_to_binary(num):
    hex_values = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    num = str(num)
    for i in num:
        if i in hex_values.values():
            j = int(str(list(hex_values.keys())[list(hex_values.values()).index(i)]))
            j = demical_to_binary(j)
            num = num.replace(i, "0")
            num = num.removesuffix(i)
            num = int(str(num), 2) + int(j)
            return num
        else:
            return demical_to_binary(hexadecimal_to_decimal(num))

def hexadecimal_to_octal(num):
    hex_values = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    num = str(num)
    for i in num:
        if i in hex_values.values():
            j = int(str(list(hex_values.keys())[list(hex_values.values()).index(i)]))
            j = demical_to_octal(j)
            num = num.replace(i, "0")
            num = num.removesuffix(i)
            num = int(str(num), 8) + int(j)
            return num
        else:
            return demical_to_octal(hexadecimal_to_decimal(num))

# GUI class

class ConverterApp(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Number Systems Converter")
        self.setGeometry(560, 360, 500, 400) # x, y, width, height
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.systemFrom = QComboBox()
        self.systemFrom.addItems(["Binary", "Hexadecimal", "Octal", "Decimal"])
        layout.addWidget(self.systemFrom)

        self.numberEntry = QLineEdit()
        self.numberEntry.setPlaceholderText("Enter your number")
        layout.addWidget(self.numberEntry)

        self.systemCombo = QComboBox()
        self.systemCombo.addItems(["Binary", "Hexadecimal", "Octal", "Decimal"])
        layout.addWidget(self.systemCombo)

        self.convertButton = QPushButton("Convert")
        self.convertButton.clicked.connect(self.convert)
        layout.addWidget(self.convertButton)

        self.resultLabel = QLabel("Result: ")
        layout.addWidget(self.resultLabel)

        central_widget.setLayout(layout)

    def convert(self):
        num = self.numberEntry.text() 
        system = self.systemCombo.currentText()
        systemFrom = self.systemFrom.currentText()

        if systemFrom == "Decimal":

            if system == "Decimal":
                result = num
            elif system == "Hexadecimal":
                result = demical_to_hexadecimal(num)
            elif system == "Binary":
                result = demical_to_binary(num)
            elif system == "Octal":
                result = demical_to_octal(num)
            else:
                result = "Invalid system"

        if systemFrom == "Binary":

            if system == "Decimal":
                result = binary_to_decimal(num)
            elif system == "Hexadecimal":
                result = binary_to_hexadecimal(num)
            elif system == "Binary":
                result = num
            elif system == "Octal":
                result = binary_to_octal(num)
            else:
                result = "Invalid system"

        if systemFrom == "Hexadecimal":
                
                if system == "Decimal":
                    result = hexadecimal_to_decimal(num)
                elif system == "Hexadecimal":
                    result = num
                elif system == "Binary":
                    result = hexadecimal_to_binary(num)
                elif system == "Octal":
                    result = hexadecimal_to_octal(num)
                else:
                    result = "Invalid system"

        if systemFrom == "Octal":
                
                if system == "Decimal":
                    result = octal_to_decimal(num)
                elif system == "Hexadecimal":
                    result = octal_to_hexadecimal(num)
                elif system == "Binary":
                    result = octal_to_binary(num)
                elif system == "Octal":
                    result = num

        self.resultLabel.setText(f"Result: {result}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = ConverterApp()
    mainWindow.show()
    sys.exit(app.exec_())
