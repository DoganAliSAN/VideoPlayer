from PyQt5.QtCore import Qt, QUrl, QPoint, QMargins
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.dragPosition = QPoint()
        self.initUI()
    def initUI(self):
        layout = QVBoxLayout(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.webview = QWebEngineView(self)
        layout.addWidget(self.webview)
        
        video_url = "https://www.youtube.com/embed/BLrHTHUjPuw"

        self.webview.load(QUrl(video_url))
        self.webview.setFixedSize(800, 600)
        self.webview.setContextMenuPolicy(Qt.NoContextMenu)
        self.webview.setContentsMargins(QMargins(0, 0, 0, 0))

        # Set the initial position of the window to the top left corner of the screen
        screen = QApplication.desktop().screenGeometry()
        self.move(0, 0)
            
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = QPoint()

    # Change the cursor to a hand when hovering over the drag frame
    def enterEvent(self, event):
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def leaveEvent(self, event):
        self.setCursor(QCursor(Qt.ArrowCursor))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setGeometry(0, 0, 800, 620)
    window.show()
    app.exec_()
