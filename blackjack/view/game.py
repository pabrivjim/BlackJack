import os
import random
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QSplitter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QObjectCleanupHandler
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5 import QtTest
from blackjack.utils.utils import get_random_card, calculate_points

# We init the list with the joker in it because it will be use like
# the reverse of the cards.

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
        self.parent.Stay.clicked.connect(self.click_stay)
        self.parent.Stay.show()
        # # Countdown animation
        # view = QtWebEngineWidgets.QWebEngineView()
        # file = os.path.join(
        #     os.path.dirname(os.path.realpath(__file__)), 
        #     "../resources/html/countdown.html"
        # )
        # view.load(QtCore.QUrl.fromLocalFile(file))
        # self.parent.widget.layout().addWidget(view, alignment=Qt.AlignCenter)
        # QtTest.QTest.qWait(6000)
        # view.hide()

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
        self.dealer_cards = []
        self.player_cards = []

        # Dealer cards
        self.left_card_container = QWidget()
        self.left_container_layout = QHBoxLayout()
        self.left_card_container.setLayout(self.left_container_layout)
        self.left_layout.addWidget(self.left_card_container)

        card = get_random_card()
        self.dealer_cards.append(card[1])
        dealer_card = QLabel(self.parent)

        # As get_random_card return a tuple with path of the pic and the name of the pic
        # we need to use index 0 to get the path
        dealer_card.setPixmap(QPixmap(card[0]))
        self.left_container_layout.addWidget(dealer_card, alignment=Qt.AlignCenter)
        
        # Joker Card
        card = "blackjack/resources/assets/cards/red_joker.svg"
        dealer_card = QLabel(self.parent)
        dealer_card.setObjectName("joker")
        dealer_card.setPixmap(QPixmap(card))
        self.left_container_layout.addWidget(dealer_card, alignment=Qt.AlignCenter)

        # Player cards
        self.right_card_container = QWidget()
        self.right_container_layout = QHBoxLayout()
        self.right_card_container.setLayout(self.right_container_layout)
        self.right_layout.addWidget(self.right_card_container)
        
        cards = get_random_card(2)
        # As get_random_card return a tuple with path of the pic and the name of the pic
        # we need to use index 0 to get the path and index 1 to get the name.
        for i in range (0, len(cards[0])):
            self.player_cards.append(cards[1][i])
            player_card = QLabel(self.parent)
            player_card.setPixmap(QPixmap(cards[0][i]))
            self.right_container_layout.addWidget(player_card, alignment=Qt.AlignCenter)
        
        points = calculate_points(self.player_cards)
        if(points==21):
            print("Winner")
    
    def click_hit(self):
        card = get_random_card()
        self.player_cards.append(card[1])
        player_card = QLabel(self.parent)
        player_card.setPixmap(QPixmap(card[0]))
        self.right_container_layout.addWidget(player_card, alignment=Qt.AlignCenter)
        points = calculate_points(self.player_cards)
        if(points>21):
            print("Loser")
    
    def click_stay(self):
        self.parent.Hit.hide()
        self.left_container_layout.removeWidget(self.parent.findChild(QLabel, "joker"))
        points = calculate_points(self.dealer_cards)
        def dealers_points():
            card = get_random_card()
            self.dealer_cards.append(card[1])
            dealer_card = QLabel(self.parent)
            dealer_card.setPixmap(QPixmap(card[0]))
            self.left_container_layout.addWidget(dealer_card, alignment=Qt.AlignCenter)
        while(points<=17):
            dealers_points()
            points = calculate_points(self.dealer_cards)
        

