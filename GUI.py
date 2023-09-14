import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class NumberBox(QWidget):
    def __init__(self):
        super().__init__()

        # Create a label to display the number
        self.number_label = QLabel('0')
        self.number_label.setAlignment(0x0082)  # Align center

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.number_label)
        self.setLayout(layout)

        self.setWindowTitle('Number Box')
        self.setGeometry(100, 100, 200, 100)  # Set window dimensions

    def set_number(self, number):
        self.number_label.setText(str(number))

def main():
    app = QApplication(sys.argv)

    window = NumberBox()
    window.set_number(42)  # Set the number to display

    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
