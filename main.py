# --------------------------------------------------------------------------
# File: main.py
# Description: File where the main application is defined.
# Date: 29/06/22
# Version: 1.0.0
# Author: Pablo Rivera Jiménez
# --------------------------------------------------------------------------
import sys
from PyQt5.QtWidgets import QApplication
from blackjack.view.main_window import MainWindow




class App(QApplication):
    """
    Esta es la clase que se utiliza para iniciar la aplicación.
    """
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)


if __name__ == '__main__':
    app = App(sys.argv)

    # translator = QTranslator(app)
    # translator.load("i18n/eng-es")
    # app.instance().installTranslator(translator)

    # IT'S IMPORTANT TO INSTANTIATE THE MAIN CLASS HERE (QMainWindow)
    # OTHERWISE IT WONT WORK.
    # I MEAN, IF YOU INSTANTIATE THE APP IN __init__ WILL CRASH

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
