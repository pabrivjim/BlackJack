from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5 import uic

from blackjack.view.game import Game

class MainWindow(QMainWindow):
    """
    Main window class.
    """
    def __init__(self, project_path=None):
        super().__init__()
        uic.loadUi("blackjack/resources/ui/main.ui", self)
        self.setWindowTitle("BlackJack")
        self.set_buttons_layout()
        self.add_widgets_to_central_widget()
        self.game_widget = Game(self)
        self.init_game_interface()
    
    def init_game_interface(self):
        # Hide Hit and Stay Buttons
        self.Hit.hide()
        self.Stay.hide()
        self.start_button = QPushButton()
        self.start_button.setText("Start")
        self.start_button.setFixedSize(250, 200)
        self.start_button.clicked.connect(self.game_widget.start_game)
        layout = QHBoxLayout(self.widget)
        layout.addWidget(self.start_button, alignment=Qt.AlignCenter)

    def set_buttons_layout(self):
        self.button_widget = QWidget()
        button_widget_layout = QHBoxLayout()
        self.button_widget.setLayout(button_widget_layout)
        button_widget_layout.addWidget(self.Hit)
        button_widget_layout.addWidget(self.Stay)
    
    def add_widgets_to_central_widget(self):
        self.central_widget_layout = QGridLayout(self.centralwidget)
        self.centralwidget.layout().addWidget(self.BlackJack)
        self.centralwidget.layout().addWidget(self.widget)
        self.centralwidget.layout().addWidget(self.button_widget)
