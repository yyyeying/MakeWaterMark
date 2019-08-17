# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watermark_show.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsScene
import matlab.engine
import os
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 920)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_openpicture = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openpicture.setGeometry(QtCore.QRect(30, 710, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_openpicture.setFont(font)
        self.pushButton_openpicture.setObjectName("pushButton_openpicture")
        self.pushButton_openpicture.clicked.connect(self.open_cover)

        self.graphicsView_cover = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_cover.setGeometry(QtCore.QRect(30, 60, 410, 310))
        self.graphicsView_cover.setObjectName("graphicsView_cover")

        self.graphicsView_watermark = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_watermark.setGeometry(QtCore.QRect(30, 430, 256, 256))
        self.graphicsView_watermark.setObjectName("graphicsView_watermark")

        self.pushButton_openwatermark = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openwatermark.setGeometry(QtCore.QRect(30, 780, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_openwatermark.setFont(font)
        self.pushButton_openwatermark.setObjectName("pushButton_openwatermark")
        self.pushButton_openwatermark.clicked.connect(self.open_mark)

        self.label_coveritle = QtWidgets.QLabel(self.centralwidget)
        self.label_coveritle.setGeometry(QtCore.QRect(30, 20, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_coveritle.setFont(font)
        self.label_coveritle.setObjectName("label_coveritle")

        self.label_marktitle = QtWidgets.QLabel(self.centralwidget)
        self.label_marktitle.setGeometry(QtCore.QRect(30, 390, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_marktitle.setFont(font)
        self.label_marktitle.setObjectName("label_marktitle")

        self.graphicsView_picture = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_picture.setGeometry(QtCore.QRect(470, 60, 1000, 750))
        self.graphicsView_picture.setObjectName("graphicsView_picture")

        self.label_picturetitle = QtWidgets.QLabel(self.centralwidget)
        self.label_picturetitle.setGeometry(QtCore.QRect(470, 20, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_picturetitle.setFont(font)
        self.label_picturetitle.setObjectName("label_picturetitle")

        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(250, 710, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_reset.setFont(font)
        self.pushButton_reset.setObjectName("pushButton_reset")

        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(250, 780, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_save.clicked.connect(self.save_pic)

        self.label_coverinfo = QtWidgets.QLabel(self.centralwidget)
        self.label_coverinfo.setGeometry(QtCore.QRect(150, 20, 171, 30))
        self.label_coverinfo.setObjectName("label_coverinfo")

        self.label_markinfo = QtWidgets.QLabel(self.centralwidget)
        self.label_markinfo.setGeometry(QtCore.QRect(150, 390, 171, 30))
        self.label_markinfo.setObjectName("label_coverinfo_2")

        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(800, 20, 300, 30))
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_status")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 23))
        self.menubar.setObjectName("menubar")

        self.menu_visible = QtWidgets.QMenu(self.menubar)
        self.menu_visible.setObjectName("menu")

        self.menu_visible_space = QtWidgets.QMenu(self.menu_visible)
        self.menu_visible_space.setObjectName("menu_visible_space")

        self.menu_weak = QtWidgets.QMenu(self.menu_visible)
        self.menu_weak.setObjectName("menu_weak")

        self.menu_robust = QtWidgets.QMenu(self.menubar)
        self.menu_robust.setObjectName("menu_robust")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.action_visible_DCT = QtWidgets.QAction(MainWindow)
        self.action_visible_DCT.setObjectName("action_visible_DCT")
        self.action_visible_DCT.triggered.connect(self.visible_DCT)

        self.action_visible_space_1 = QtWidgets.QAction(MainWindow)
        self.action_visible_space_1.setObjectName("action_visible_space_1")
        self.action_visible_space_1.triggered.connect(lambda: self.visible_space('1'))

        self.action_visible_space_2 = QtWidgets.QAction(MainWindow)
        self.action_visible_space_2.setObjectName("action_visible_space_2")
        self.action_visible_space_2.triggered.connect(lambda: self.visible_space('2'))

        self.action_visible_space_3 = QtWidgets.QAction(MainWindow)
        self.action_visible_space_3.setObjectName("action_visible_space_3")
        self.action_visible_space_3.triggered.connect(lambda: self.visible_space('3'))

        self.menu_visible_space.addAction(self.action_visible_space_1)
        self.menu_visible_space.addAction(self.action_visible_space_2)
        self.menu_visible_space.addAction(self.action_visible_space_3)

        self.action_weak_embed = QtWidgets.QAction(MainWindow)
        self.action_weak_embed.setObjectName("action_weak_embed")
        self.action_weak_embed.triggered.connect(self.weak_embed)

        self.action_weak_extract = QtWidgets.QAction(MainWindow)
        self.action_weak_extract.setObjectName("action_weak_extract")
        self.action_weak_extract.triggered.connect(self.weak_extract)

        self.action_robust_embed = QtWidgets.QAction(MainWindow)
        self.action_robust_embed.setObjectName("action_robust_embed")
        self.action_robust_embed.triggered.connect(self.robust_embed)

        self.action_robust_extract_no_cover = QtWidgets.QAction(MainWindow)
        self.action_robust_extract_no_cover.setObjectName("action_robust_extract")
        self.action_robust_extract_no_cover.triggered.connect(self.robust_extract_no_cover)

        self.action_robust_extract_with_cover = QtWidgets.QAction(MainWindow)
        self.action_robust_extract_with_cover.setObjectName("action_robust_extract")
        self.action_robust_extract_with_cover.triggered.connect(self.robust_extract_with_cover)

        self.action_robust_QIM_embed = QtWidgets.QAction(MainWindow)
        self.action_robust_QIM_embed.setObjectName("action_robust_QIM_embed")
        self.action_robust_QIM_embed.triggered.connect(self.robust_QIM_embed)

        self.action_robust_QIM_extract = QtWidgets.QAction(MainWindow)
        self.action_robust_QIM_extract.setObjectName("action_robust_QIM_embed")
        self.action_robust_QIM_extract.triggered.connect(self.robust_QIM_extract)

        self.menu_robust.addAction(self.action_robust_embed)
        self.menu_robust.addAction(self.action_robust_extract_no_cover)
        self.menu_robust.addAction(self.action_robust_extract_with_cover)
        self.menu_robust.addAction(self.action_robust_QIM_embed)
        self.menu_robust.addAction(self.action_robust_QIM_extract)

        self.menu_weak.addAction(self.action_weak_embed)
        self.menu_weak.addAction(self.action_weak_extract)

        self.menu_visible.addAction(self.menu_visible_space.menuAction())
        self.menu_visible.addAction(self.action_visible_DCT)

        self.menubar.addAction(self.menu_visible.menuAction())
        self.menubar.addAction(self.menu_weak.menuAction())
        self.menubar.addAction(self.menu_robust.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "搞水印"))
        self.pushButton_openpicture.setText(_translate("MainWindow", "打开图片"))
        self.pushButton_openwatermark.setText(_translate("MainWindow", "打开水印"))
        self.label_coveritle.setText(_translate("MainWindow", "图片"))
        self.label_marktitle.setText(_translate("MainWindow", "水印"))
        self.label_picturetitle.setText(_translate("MainWindow", "处理后"))
        self.pushButton_reset.setText(_translate("MainWindow", "重置"))
        self.pushButton_save.setText(_translate("MainWindow", "保存"))
        self.label_coverinfo.setText(_translate("MainWindow", ""))
        self.label_markinfo.setText(_translate("MainWindow", ""))
        self.label_status.setText(_translate("MainWindow", "正在启动程序..."))
        self.menu_visible.setTitle(_translate("MainWindow", "可见水印"))
        self.menu_weak.setTitle(_translate("MainWindow", "脆弱水印"))
        self.menu_visible_space.setTitle(_translate("MainWindow", "空间域可见水印..."))
        self.menu_robust.setTitle(_translate("MainWindow", "鲁棒水印"))
        self.action_visible_DCT.setText(_translate("MainWindow", "频域可见水印"))
        self.action_visible_space_1.setText(_translate("MainWindow", "直接叠加"))
        self.action_visible_space_2.setText(_translate("MainWindow", "加性叠加"))
        self.action_visible_space_3.setText(_translate("MainWindow", "乘性叠加"))
        self.action_weak_embed.setText(_translate("MainWindow", "嵌入脆弱水印..."))
        self.action_weak_extract.setText(_translate("MainWindow", "提取脆弱水印..."))
        self.action_robust_embed.setText(_translate("MainWindow", "嵌入直接扩频水印..."))
        self.action_robust_extract_no_cover.setText(_translate("MainWindow", "提取直接扩频水印（无原图）..."))
        self.action_robust_extract_with_cover.setText(_translate("MainWindow", "提取直接扩频水印（有原图）..."))
        self.action_robust_QIM_embed.setText(_translate("MainWindow", "嵌入直接扩频+QIM水印..."))
        self.action_robust_QIM_extract.setText(_translate("MainWindow", "提取直接扩频+QIM水印..."))

    def make_cache_dir(self):
        self.label_status.setText('正在设置缓存目录...')
        self.cache_path = 'C:\\myFiles\\python\\pymatlab\\cache\\'
        if not os.path.exists(self.cache_path):
            print("-- making cache dictionary --")
            os.mkdir(self.cache_path)
            return
        print("-- cache dictionary exsists --")

    def init_engine(self):
        print("-- initializing engine --")
        self.label_status.setText('正在加载Matlab引擎...')
        self.engine = matlab.engine.start_matlab()
        self.label_status.setText('启动完毕。')

    def open_cover(self):
        cover_file = self.open_pic()
        if cover_file:
            self.cover_path = cover_file['name']
            # print(cover_file[0])
            try:
                self.label_status.setText('正在打开原图...')
                cover_map = QPixmap(cover_file['name'])
                format = cover_file['format']
                cover_width = cover_map.width()
                cover_height = cover_map.height()
                coverinfo_text = str(cover_width) + '×' + str(cover_height) + ', ' + format
                self.label_coverinfo.setText(coverinfo_text)
                cover_map = cover_map.scaled(QSize(400, 300), aspectRatioMode=Qt.KeepAspectRatio)
                new_graphicsScene = QGraphicsScene()
                new_graphicsScene.addPixmap(cover_map)
                self.graphicsView_cover.setScene(new_graphicsScene)
                self.graphicsView_cover.show()
                self.label_status.setText('')
            except Exception as ex:
                print(ex)

    def open_mark(self):
        mark_file = self.open_pic()
        if mark_file:
            self.mark_path = mark_file['name']
            try:
                self.label_status.setText('正在打开水印图片...')
                mark_map = QPixmap(self.mark_path)
                format = mark_file['format']
                mark_width = mark_map.width()
                mark_height = mark_map.height()
                markinfo_text = str(mark_width) + '×' + str(mark_height) + ', ' + format
                self.label_markinfo.setText(markinfo_text)
                mark_map = mark_map.scaled(QSize(250, 250), aspectRatioMode=Qt.KeepAspectRatio)
                new_graphicsScene = QGraphicsScene()
                new_graphicsScene.addPixmap(mark_map)
                self.graphicsView_watermark.setScene(new_graphicsScene)
                self.graphicsView_watermark.show()
                self.label_status.setText('')
            except Exception as ex:
                print(ex)

    def open_pic(self):
        file_select = QFileDialog.getOpenFileName(caption="选择图片",
                                                  directory="C:\\",
                                                  filter="Image files( *.jpg *.png *.gif *.bmp);;"
                                                         "All files (*.*)")
        file_name = file_select[0]
        if file_name:
            print("file = " + file_name)
            format = file_name.split('.')[1]
            file = {'name': file_name, 'format': format}
            return file
        else:
            return

    def save_pic(self):
        try:
            pic_file_save_select = QFileDialog.getSaveFileName(caption='保存图片',
                                                               directory='C:\\',
                                                               filter="JPEG file( *.jpg);;"
                                                                      "BMP file( *.bmp)")
            self.label_status.setText('正在保存图片...')
            pic_file = open(self.picture_path, 'rb')
            pic_text = pic_file.read()
            pic_file_save = open(pic_file_save_select[0], 'wb')
            pic_file_save.write(pic_text)
            self.label_status.setText('')
        except Exception as ex:
            print(ex)
        return

    def visible_space(self, option):
        self.label_status.setText('正在执行水印嵌入...')
        try:
            self.picture_path = self.engine.visible_watermark_for_GUI(self.cover_path, self.mark_path, option)
            picture_map = QPixmap(self.picture_path)
            picture_map = picture_map.scaled(QSize(990, 740), aspectRatioMode=Qt.KeepAspectRatio)
            new_graphicsScene = QGraphicsScene()
            new_graphicsScene.addPixmap(picture_map)
            self.graphicsView_picture.setScene(new_graphicsScene)
            self.graphicsView_picture.show()
            self.label_status.setText('水印嵌入完成。')
        except Exception as ex:
            print(ex)
        return

    def visible_DCT(self):
        self.label_status.setText('正在执行水印嵌入...')
        try:
            self.picture_path = self.engine.visible_watermark_DCT_for_GUI(self.cover_path, self.mark_path)
            picture_map = QPixmap(self.picture_path)
            picture_map = picture_map.scaled(QSize(990, 740), aspectRatioMode=Qt.KeepAspectRatio)
            new_graphicsScene = QGraphicsScene()
            new_graphicsScene.addPixmap(picture_map)
            self.graphicsView_picture.setScene(new_graphicsScene)
            self.graphicsView_picture.show()
            self.label_status.setText('水印嵌入完成。')
        except Exception as ex:
            print(ex)
        return

    def weak_embed(self):
        watermark_file_select = QFileDialog.getOpenFileName(caption="选择一个水印文件",
                                                      directory="C:\\",
                                                      filter="text files( *.txt);;"
                                                             "All files (*.*)")
        watermark_file_name = watermark_file_select[0]
        if watermark_file_name:
            self.label_status.setText('正在执行水印嵌入...')
            format = watermark_file_name.split('.')[1]
            if format == 'txt' and self.cover_path:
                try:
                    path = self.engine.weak_embed_for_GUI(self.cover_path, watermark_file_name)
                    print(path)
                    self.picture_path = path.split(',')[0]
                    key_path = path.split(',')[1]
                    picture_map = QPixmap(self.picture_path)
                    picture_map = picture_map.scaled(QSize(990, 740), aspectRatioMode=Qt.KeepAspectRatio)
                    new_graphicsScene = QGraphicsScene()
                    new_graphicsScene.addPixmap(picture_map)
                    self.graphicsView_picture.setScene(new_graphicsScene)
                    self.graphicsView_picture.show()
                    self.label_status.setText('水印嵌入完成。')
                    key_file = open(key_path, 'r')
                    key_text = key_file.read()
                    key_file_save_select = QFileDialog.getSaveFileName(caption='保存密钥',
                                                                directory='C:\\',
                                                                filter="text files( *.txt);;")
                    print(key_file_save_select)
                    key_file_save = open(key_file_save_select[0], 'w')
                    key_file_save.write(key_text)
                except Exception as ex:
                    print(ex)
            else:
                reply_text = '水印文件格式错误。'
                msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                       "错误提示",
                                                       reply_text,
                                                       QMessageBox.Yes,
                                                       QMessageBox.Yes)
        return

    def weak_extract(self):
        key_file_select = QFileDialog.getOpenFileName(caption="选择一个密钥文件",
                                                      directory="C:\\",
                                                      filter="text files( *.txt);;"
                                                             "All files (*.*)")
        key_file_name = key_file_select[0]
        if key_file_name:
            self.label_status.setText('正在执行水印提取...')
            format = key_file_name.split('.')[1]
            if format == 'txt' and self.cover_path:
                try:

                    watermark = self.engine.jpeg_lbs_extract(self.cover_path, key_file_name)
                    reply_text = '提取出来的水印：\n'+watermark
                    self.label_status.setText('')
                    msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                           "提取完毕",
                                                           reply_text,
                                                           QMessageBox.Yes,
                                                           QMessageBox.Yes)
                except Exception as ex:
                    print(ex)
            else:
                reply_text = '密钥文件格式错误。'
                msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                       "错误提示",
                                                       reply_text,
                                                       QMessageBox.Yes,
                                                       QMessageBox.Yes)
        else:
            reply_text = '未选择密钥文件。'
            msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                   "错误提示",
                                                   reply_text,
                                                   QMessageBox.Yes,
                                                   QMessageBox.Yes)
        return

    def robust_embed(self):
        watermark_file_select = QFileDialog.getOpenFileName(caption="选择一个水印文件",
                                                            directory="C:\\",
                                                            filter="text files( *.txt);;"
                                                                   "All files (*.*)")
        watermark_file_name = watermark_file_select[0]
        if watermark_file_name:
            format = watermark_file_name.split('.')[1]
            if format == 'txt' and self.cover_path:
                try:
                    self.label_status.setText('正在执行水印嵌入...')
                    path = self.engine.robust_embed_for_GUI(self.cover_path, watermark_file_name)
                    print(path)
                    self.picture_path = path.split(',')[0]
                    key_path = path.split(',')[1]
                    picture_map = QPixmap(self.picture_path)
                    picture_map = picture_map.scaled(QSize(990, 740), aspectRatioMode=Qt.KeepAspectRatio)
                    new_graphicsScene = QGraphicsScene()
                    new_graphicsScene.addPixmap(picture_map)
                    self.graphicsView_picture.setScene(new_graphicsScene)
                    self.graphicsView_picture.show()
                    self.label_status.setText('水印嵌入完成。')
                    key_file = open(key_path, 'r')
                    key_text = key_file.read()
                    key_file_save_select = QFileDialog.getSaveFileName(caption='保存密钥',
                                                                       directory='C:\\',
                                                                       filter="text files( *.txt);;")
                    print(key_file_save_select)
                    key_file_save = open(key_file_save_select[0], 'w')
                    key_file_save.write(key_text)
                except Exception as ex:
                    print(ex)
            else:
                reply_text = '密钥文件格式错误。'
                msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                       "错误提示",
                                                       reply_text,
                                                       QMessageBox.Yes,
                                                       QMessageBox.Yes)
        return

    def robust_extract_no_cover(self):
        key_file_select = QFileDialog.getOpenFileName(caption="选择一个密钥文件",
                                                      directory="C:\\",
                                                      filter="text files( *.txt);;"
                                                             "All files (*.*)")
        key_file_name = key_file_select[0]
        if key_file_name:
            format = key_file_name.split('.')[1]
            if format == 'txt' and self.cover_path:
                try:
                    self.label_status.setText('正在执行水印提取...')
                    watermark = self.engine.watermark_spreading_extract(0, self.cover_path, key_file_name)
                    reply_text = '提取出来的水印：\n' + watermark
                    self.label_status.setText('')
                    msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                           "提取完毕",
                                                           reply_text,
                                                           QMessageBox.Yes,
                                                           QMessageBox.Yes)
                except Exception as ex:
                    print(ex)
            else:
                reply_text = '密钥文件格式错误。'
                msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                       "错误提示",
                                                       reply_text,
                                                       QMessageBox.Yes,
                                                       QMessageBox.Yes)
        else:
            reply_text = '未选择密钥文件。'
            msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                   "错误提示",
                                                   reply_text,
                                                   QMessageBox.Yes,
                                                   QMessageBox.Yes)
        return

    def robust_extract_with_cover(self):
        key_file_select = QFileDialog.getOpenFileName(caption="选择一个密钥文件",
                                                      directory="C:\\",
                                                      filter="text files( *.txt);;"
                                                             "All files (*.*)")
        key_file_name = key_file_select[0]
        origin_file_select = QFileDialog.getOpenFileName(caption="选择一个原图文件",
                                                      directory="C:\\",
                                                      filter="picture files( *.jpg *.bmp);;"
                                                             "All files (*.*)")
        origin_file_name = origin_file_select[0]
        if key_file_name and origin_file_name:
            format = key_file_name.split('.')[1]
            if format == 'txt' and self.cover_path:
                try:
                    self.label_status.setText('正在执行水印提取...')
                    watermark = self.engine.watermark_spreading_extract(origin_file_name, self.cover_path, key_file_name)
                    reply_text = '提取出来的水印：\n' + watermark
                    self.label_status.setText('')
                    msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                           "提取完毕",
                                                           reply_text,
                                                           QMessageBox.Yes,
                                                           QMessageBox.Yes)
                except Exception as ex:
                    print(ex)
            else:
                reply_text = '密钥文件格式错误。'
                msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                       "错误提示",
                                                       reply_text,
                                                       QMessageBox.Yes,
                                                       QMessageBox.Yes)
        else:
            reply_text = '未选择原图文件或密钥文件。'
            msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                   "错误提示",
                                                   reply_text,
                                                   QMessageBox.Yes,
                                                   QMessageBox.Yes)
        return

    def robust_QIM_embed(self):
        watermark_file_select = QFileDialog.getOpenFileName(caption="选择一个水印文件",
                                                            directory="C:\\",
                                                            filter="text files( *.txt);;"
                                                                   "All files (*.*)")
        watermark_file_name = watermark_file_select[0]
        if watermark_file_name:
            format = watermark_file_name.split('.')[1]
            if format == 'txt' and self.cover_path:
                try:
                    self.label_status.setText('正在执行水印嵌入...')
                    path = self.engine.robust_QIM_embed_for_GUI(self.cover_path, watermark_file_name)
                    print(path)
                    self.picture_path = path.split(',')[0]
                    key_path = path.split(',')[1]
                    picture_map = QPixmap(self.picture_path)
                    picture_map = picture_map.scaled(QSize(990, 740), aspectRatioMode=Qt.KeepAspectRatio)
                    new_graphicsScene = QGraphicsScene()
                    new_graphicsScene.addPixmap(picture_map)
                    self.graphicsView_picture.setScene(new_graphicsScene)
                    self.graphicsView_picture.show()
                    self.label_status.setText('水印嵌入完成。')
                    key_file = open(key_path, 'r')
                    key_text = key_file.read()
                    key_file_save_select = QFileDialog.getSaveFileName(caption='保存密钥',
                                                                       directory='C:\\',
                                                                       filter="text files( *.txt);;")
                    print(key_file_save_select)
                    key_file_save = open(key_file_save_select[0], 'w')
                    key_file_save.write(key_text)
                except Exception as ex:
                    print(ex)
            else:
                reply_text = '水印文件格式错误。'
                msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                       "错误提示",
                                                       reply_text,
                                                       QMessageBox.Yes,
                                                       QMessageBox.Yes)
        return

    def robust_QIM_extract(self):
        key_file_select = QFileDialog.getOpenFileName(caption="选择一个密钥文件",
                                                      directory="C:\\",
                                                      filter="text files( *.txt);;"
                                                             "All files (*.*)")
        key_file_name = key_file_select[0]
        if key_file_name:
            format = key_file_name.split('.')[1]
            if format == 'txt' and self.cover_path:
                try:
                    self.label_status.setText('正在执行水印提取...')
                    watermark = self.engine.watermark_spreading_QIM_extract(self.cover_path, key_file_name)
                    reply_text = '提取出来的水印：\n' + watermark
                    self.label_status.setText('')
                    msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                           "提取完毕",
                                                           reply_text,
                                                           QMessageBox.Yes,
                                                           QMessageBox.Yes)
                except Exception as ex:
                    print(ex)
            else:
                reply_text = '密钥文件格式错误。'
                msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                       "错误提示",
                                                       reply_text,
                                                       QMessageBox.Yes,
                                                       QMessageBox.Yes)
        else:
            reply_text = '未选择密钥文件。'
            msgbox_reply = QMessageBox.information(widgets_loginwindow,
                                                   "错误提示",
                                                   reply_text,
                                                   QMessageBox.Yes,
                                                   QMessageBox.Yes)
        return


if __name__ == "__main__":
    app_loginwindow = QtWidgets.QApplication(sys.argv)
    widgets_loginwindow = QtWidgets.QMainWindow()
    ui_loginwindow = Ui_MainWindow()
    ui_loginwindow.setupUi(widgets_loginwindow)
    widgets_loginwindow.show()
    ui_loginwindow.make_cache_dir()
    ui_loginwindow.init_engine()
    sys.exit(app_loginwindow.exec_())
