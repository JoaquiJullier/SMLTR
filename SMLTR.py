if __name__ == "__main__":

    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    from PyQt5.QtGui import QIcon
    icon = QIcon("/files/ICON.ico")
    app.setWindowIcon(icon)

    from lib.WDW import WDW

    main_window = WDW()
    main_window.show()

    sys.exit(app.exec_())