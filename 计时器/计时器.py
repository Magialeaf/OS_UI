import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton


class TimerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)  # 连接新的timeout信号槽
        self.time = QTime(0, 0, 0)
        self.is_running = False

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label_time = QLabel('00:00:00')
        self.label_time.setAlignment(Qt.AlignCenter)
        self.label_time.setStyleSheet('border: 1px solid black; padding: 10px; font-size: 24px')

        layout.addWidget(self.label_time)

        self.button_start = QPushButton('开始')
        self.button_start.setStyleSheet('font-size: 16px')
        self.button_start.clicked.connect(self.start_timer)
        layout.addWidget(self.button_start)

        self.button_pause = QPushButton('暂停')
        self.button_pause.setStyleSheet('font-size: 16px')
        self.button_pause.setEnabled(False)  # 初始状态下禁用暂停按钮
        self.button_pause.clicked.connect(self.pause_timer)
        layout.addWidget(self.button_pause)

        self.button_reset = QPushButton('重置')
        self.button_reset.setStyleSheet('font-size: 16px')
        self.button_reset.setEnabled(False)  # 初始状态下禁用重置按钮
        self.button_reset.clicked.connect(self.reset_timer)
        layout.addWidget(self.button_reset)

        self.setLayout(layout)

        self.setWindowTitle('计时器')
        self.resize(300, 200)  # 设置界面宽度和高度

    def start_timer(self):
        if not self.is_running:
            if self.timer.isActive():
                self.timer.stop()

            self.timer.start(1000)  # 每隔1秒触发一次timeout事件
            self.is_running = True

            self.label_time.setStyleSheet(
                'border: 1px solid black; padding: 10px; font-size: 24px; background-color: yellow')  # 修改文本样式，增加背景颜色
            self.update_buttons_state(start_enabled=False, pause_enabled=True, reset_enabled=True)

    def pause_timer(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False

            self.label_time.setStyleSheet(
                'border: 1px solid black; padding: 10px; font-size: 24px; background-color: white')  # 恢复文本样式，移除背景颜色
            self.update_buttons_state(start_enabled=True, pause_enabled=False, reset_enabled=True)

    def reset_timer(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0)
        self.update_displayed_time()
        self.is_running = False

        self.label_time.setStyleSheet(
            'border: 1px solid black; padding: 10px; font-size: 24px; background-color: white')
        self.update_buttons_state(start_enabled=True, pause_enabled=False, reset_enabled=False)

    def update_time(self):
        self.time = self.time.addSecs(1)
        self.update_displayed_time()

    def update_displayed_time(self):
        time_text = self.time.toString('hh:mm:ss')
        self.label_time.setText(time_text)

    def update_buttons_state(self, start_enabled=True, pause_enabled=False, reset_enabled=False):
        # 更新按钮状态
        for button in [self.button_start, self.button_pause, self.button_reset]:
            button.setEnabled(False)  # 先禁用所有按钮
        self.button_start.setEnabled(start_enabled)
        self.button_pause.setEnabled(pause_enabled)
        self.button_reset.setEnabled(reset_enabled)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 设置图标路径
    icon_path = 'Zafkiel.jpg'
    app.setWindowIcon(QtGui.QIcon(icon_path))

    timer_widget = TimerWidget()
    timer_widget.setStyleSheet('font-size: 18px')
    timer_widget.resize(300, 200)
    timer_widget.show()
    sys.exit(app.exec_())

