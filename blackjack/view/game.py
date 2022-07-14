import os
import random
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QSplitter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QObjectCleanupHandler
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5 import QtTest


def get_random_card(number_of_cards = 1):
    """
    Returns a list of random cards.
    """
    
    cards = []
    directory = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 
            "../resources/assets/cards"
        )
    for i in range(number_of_cards):
        choice = random.choice(os.listdir(directory))
        path = os.path.join(directory, choice)
        if(number_of_cards == 1):
            return path
        cards.append(path)
    return cards


class Game(QWidget):
    """
    Main window class.
    """
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        
    
    def start_game(self):
        self.parent.start_button.hide()
        self.parent.Hit.show()
        self.parent.Hit.clicked.connect(self.click_hit)
        self.parent.Stay.show()
        # # Countdown animation
        view = QtWebEngineWidgets.QWebEngineView()
        file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 
            "../resources/html/countdown.html"
        )
        view.load(QtCore.QUrl.fromLocalFile(file))
        self.parent.widget.layout().addWidget(view, alignment=Qt.AlignCenter)
        QtTest.QTest.qWait(6000)
        view.hide()

        hbox = QHBoxLayout(self)

        splitter1 = QSplitter(self)
        splitter1.setOrientation(Qt.Horizontal)

        left = QFrame(splitter1)
        left.setFrameShape(QFrame.StyledPanel)

        right = QFrame(splitter1)
        right.setFrameShape(QFrame.StyledPanel)

        hbox.addWidget(splitter1)
        self.setGeometry(500, 500, 750, 750)
        
        # Remove old widget layout and set new one
        QObjectCleanupHandler().add(self.parent.widget.layout())
        self.parent.widget.setLayout(hbox)

        self.left_layout = QVBoxLayout(left)
        left_label = QLabel("Dealer")
        left_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.left_layout.addWidget(left_label)

        self.right_layout = QVBoxLayout(right)
        right_label = QLabel("Player")
        right_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.right_layout.addWidget(right_label)

        self.show_cards()


    def show_cards(self):
        
        # Dealer cards
        self.left_card_container = QWidget()
        self.left_container_layout = QHBoxLayout()
        self.left_card_container.setLayout(self.left_container_layout)
        self.left_layout.addWidget(self.left_card_container)

        card = get_random_card()
        dealer_card = QLabel(self.parent)
        dealer_card.setPixmap(QPixmap(card))
        self.left_container_layout.addWidget(dealer_card, alignment=Qt.AlignCenter)
        
        # Joker Card
        card = "blackjack/resources/assets/red_joker.svg"
        dealer_card = QLabel(self.parent)
        dealer_card.setPixmap(QPixmap(card))
        self.left_container_layout.addWidget(dealer_card, alignment=Qt.AlignCenter)

        # Player cards
        self.right_card_container = QWidget()
        self.right_container_layout = QHBoxLayout()
        self.right_card_container.setLayout(self.right_container_layout)
        self.right_layout.addWidget(self.right_card_container)
        
        cards = get_random_card(2)
        for card in cards:
            player_card = QLabel(self.parent)
            player_card.setPixmap(QPixmap(card))
            self.right_container_layout.addWidget(player_card, alignment=Qt.AlignCenter)
    
    def click_hit(self):
        card = get_random_card()
        player_card = QLabel(self.parent)
        player_card.setPixmap(QPixmap(card))
        self.right_container_layout.addWidget(player_card, alignment=Qt.AlignCenter)

        
