import sys
import time
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout


class FadeWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        button = QPushButton(self)
        button.setText("Close")

        button.resize(200, 200)
        button.clicked.connect(self.fade)

        layout = QVBoxLayout(self)
        layout.addWidget(button)

        self.resize(300, 300)

    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()

    def close(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FadeWindow()
    window.show()
    sys.exit(app.exec_())