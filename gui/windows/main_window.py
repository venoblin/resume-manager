from PySide6.QtWidgets import QWidget, QStackedLayout
from gui.widgets.pages.finder import Finder

class MainWindow(QWidget):
  stack: QStackedLayout
  
  def __init__(self):
    super(MainWindow, self).__init__()
    self.setWindowTitle('Resume Manager')
    self.stack = QStackedLayout()

    self.stack.addWidget(Finder(stack=self.stack))
    self.stack.setCurrentIndex(0)
    
    self.setLayout(self.stack)
