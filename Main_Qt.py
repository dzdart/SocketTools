import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QRadioButton, QHBoxLayout, QVBoxLayout,
                             QApplication)


class dzd(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        B_UDP = QPushButton('UDP')
        B_UDP.clicked.connect(self.test)

        B_TCP = QPushButton('TCP')
        B_TCP.clicked.connect(dzd1)

        HB_Tile = QHBoxLayout()
        HB_Tile.addStrut(1)
        HB_Tile.addWidget(B_UDP)
        HB_Tile.addWidget(B_TCP)

        # 第一行，ip地址和端口
        QL_IpAddress = QLabel('IP地址')
        QLE_IpAddress = QLineEdit('127.0.0.1')
        QL_IpPort = QLabel('端口')
        QLE_IpPPort = QLineEdit('80')

        HB_1 = QHBoxLayout()
        HB_1.addStrut(1)
        HB_1.addWidget(QL_IpAddress)
        HB_1.addWidget(QLE_IpAddress)
        HB_1.addWidget(QL_IpPort)
        HB_1.addWidget(QLE_IpPPort)

        # 第二行：发送模式
        QL_SendMod = QLabel('发送模式')
        RB_SendMod1 = QRadioButton('单次')
        RB_SendMod1.clicked.connect(
            lambda: self.SetWidgetVisable([QL_SendCycles, QLE_SendCycles, QL_SendSleep, QLE_SendSleep], False))
        RB_SendMod1.setChecked(True)
        RB_SendMod2 = QRadioButton('循环')
        RB_SendMod2.clicked.connect(
            lambda: self.SetWidgetVisable([QL_SendCycles, QLE_SendCycles, QL_SendSleep, QLE_SendSleep], True))
        QL_SendCycles = QLabel('循环次数')
        QL_SendCycles.setVisible(False)
        QLE_SendCycles = QLineEdit('1')
        QLE_SendCycles.setValidator(QtGui.QIntValidator())
        QLE_SendCycles.setVisible(False)
        QL_SendSleep = QLabel('循环间隔')
        QL_SendSleep.setVisible(False)
        QLE_SendSleep = QLineEdit('1')
        QLE_SendSleep.setValidator(QtGui.QIntValidator())
        QLE_SendSleep.setVisible(False)

        HB_2 = QHBoxLayout()
        HB_2.addStrut(1)
        HB_2.addWidget(QL_SendMod, 0,Qt.AlignLeft)
        HB_2.addWidget(RB_SendMod1, 0,Qt.AlignLeft)
        HB_2.addWidget(RB_SendMod2, 0,Qt.AlignLeft)
        HB_2.addWidget(QL_SendCycles, 0,Qt.AlignLeft)
        HB_2.addWidget(QLE_SendCycles, 0,Qt.AlignLeft)
        HB_2.addWidget(QL_SendSleep, 0,Qt.AlignLeft)
        HB_2.addWidget(QLE_SendSleep, 0,Qt.AlignLeft)

        # 主框架布局，垂直排列
        VB_Main = QVBoxLayout()
        VB_Main.addStrut(1)
        VB_Main.addLayout(HB_Tile)
        VB_Main.addLayout(HB_1)
        VB_Main.addLayout(HB_2)

        self.setLayout(VB_Main)
        self.setGeometry(0, 0, 300, 150)
        self.setWindowTitle('瑶瑶')
        self.show()

    def test(self):
        print('1111111')

    def SetWidgetVisable(self, item, B):
        for i in item:
            i.setVisible(B)


def dzd1():
    print(222222)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = dzd()
    sys.exit(app.exec_())
