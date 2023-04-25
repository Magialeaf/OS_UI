import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QLabel,QPushButton,QApplication,QWidget,QDesktopWidget,QLineEdit,QTextEdit,QFormLayout
from PyQt5.QtGui import QIcon

class Spider(QWidget):
    def __init__(self):
        super(Spider, self).__init__()
        self.Win()

    def Win(self):
        # 设置窗口标题
        self.setWindowTitle("简单爬虫")
        # 展示窗口
        width = 500
        height = 400
        self.resize(width, height)
        center_point = QDesktopWidget().availableGeometry().center()
        x = center_point.x()
        y = center_point.y()
        self.move(x - width // 2,y - height // 2)

        # 布局
        self.main = QVBoxLayout(self)
        self.top = QHBoxLayout()

        self.tip = QLabel("网址：")
        self.line = QLineEdit("http://")
        self.bt = QPushButton("确认")


        self.bt.clicked.connect(self.get_Url)
        self.text = QTextEdit()

        self.top.addWidget(self.tip)
        self.top.addWidget(self.line)
        self.top.addWidget(self.bt)
        self.main.addLayout(self.top)
        self.main.addWidget(self.text)


    def get_Url(self):
        def getHTML(url: str) -> str:
            header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"}
            response = requests.get(url=url, timeout=15, headers=header)
            response.encoding = "UTF-8"
            page_text = response.text
            return page_text

        def getRes(text: str) -> str:
            bf = BeautifulSoup(text, "html.parser")
            text = bf.prettify()
            print("爬取的网页如下\n", text)
            return text

        url = self.line.text()
        response = getHTML(url)
        res = getRes(response)
        self.text.setPlainText(res)

if __name__ =="__main__":
    app = QApplication(sys.argv)

    demo = Spider()
    demo.show()

    app.exec()