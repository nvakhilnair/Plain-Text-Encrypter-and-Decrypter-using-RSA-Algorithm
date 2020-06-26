from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import random


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(905, 531)

        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(
            "QWidget#Dialog {background-image: url('data/logo.png');background-repeat: no-repeat; background-position: bottom right;}")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("data\icon.ico")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        self.InsertText = QtGui.QPlainTextEdit(Dialog)
        self.InsertText.setGeometry(QtCore.QRect(10, 30, 421, 281))
        self.InsertText.setObjectName(_fromUtf8("InsertText"))
        self.outputText = QtGui.QPlainTextEdit(Dialog)
        self.outputText.setGeometry(QtCore.QRect(450, 30, 441, 281))
        self.outputText.setObjectName(_fromUtf8("outputText"))
        self.Encrypt = QtGui.QPushButton(Dialog)
        self.Encrypt.setGeometry(QtCore.QRect(350, 450, 75, 23))
        self.Encrypt.setObjectName(_fromUtf8("Encrypt"))
        self.Encrypt.clicked.connect(self.encryptdata)
        self.Decrypt = QtGui.QPushButton(Dialog)
        self.Decrypt.setGeometry(QtCore.QRect(450, 450, 75, 23))
        self.Decrypt.setObjectName(_fromUtf8("Decrypt"))
        self.Decrypt.clicked.connect(self.decryptdata)
        self.e = QtGui.QLineEdit(Dialog)
        self.e.setGeometry(QtCore.QRect(610, 340, 113, 20))
        self.e.setObjectName(_fromUtf8("e"))
        self.n = QtGui.QLineEdit(Dialog)
        self.n.setGeometry(QtCore.QRect(610, 370, 113, 20))
        self.n.setObjectName(_fromUtf8("n"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(460, 340, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(460, 370, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(610, 10, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.newline = QtGui.QLineEdit(Dialog)
        self.newline.setGeometry(QtCore.QRect(180, 340, 131, 20))
        self.newline.setObjectName(_fromUtf8("newline"))
        self.dcode = QtGui.QLabel(Dialog)
        self.dcode.setGeometry(QtCore.QRect(60, 340, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dcode.setFont(font)
        self.dcode.setObjectName(_fromUtf8("dcode"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def encryptdata(self):
        prime_numbers = [167, 389, 199, 431, 353, 349, 233, 197, 433, 467, 163, 491, 181, 383, 271, 227, 397, 191, 263, 439, 113, 137, 193, 317, 463, 479, 239, 401, 101, 179, 379, 131, 241,
                         229, 367, 211, 359, 269, 127, 149, 281, 283, 419, 107, 331, 421, 251, 457, 109, 151, 373, 277, 223, 103, 293, 139, 157, 487, 311, 307, 461, 409, 313, 443, 337, 347, 173, 257, 499, 449]
        p = random.choice(prime_numbers)
        q = random.choice(prime_numbers)
        n = p * q
        phi = (p-1) * (q-1)
        for i in range(1, phi):
            if((n % i) != 0 and (phi % i) != 0 and (i % 2) != 0):
                e = i
                break

        def modinv(a, m):
            for x in range(1, m):
                if (a * x) % m == 1:
                    return x
            return None
        d = modinv(e, phi)
        message = self.InsertText.toPlainText()
        text_to_ASCII = [ord(c) for c in message]
        cipher = []
        for i in text_to_ASCII:
            mes = int(i)
            temp = int(pow(mes, e) % n)
            cipher.append(temp)
        self.outputText.insertPlainText(str(cipher))
        code = str(d)+"," + str(n)
        self.newline.setText(code)
        error = QtGui.QMessageBox.information(
            self, 'Sucess', "Process Complete")

    def decryptdata(self):
        decrypted_message = []
        d = int(self.e.text())
        n = int(self.n.text())
        cipher = (self.InsertText.toPlainText())
        cipher = cipher[1:(len(cipher)-1)]
        cipher = list(cipher.split(", "))
        for i in cipher:
            mes = int(i)
            temp = pow(mes, d) % n
            decrypted_message.append(chr(temp))
        decrypted__message = ''.join(map(str, decrypted_message))
        self.outputText.insertPlainText(str(decrypted__message))
        error = QtGui.QMessageBox.information(
            self, 'Sucess', "Process Complete")

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "N&D cryption", None))
        self.Encrypt.setText(_translate("Dialog", "Encrypt", None))
        self.Decrypt.setText(_translate("Dialog", "Decrypt", None))
        self.label.setText(_translate("Dialog", "Decryption code \'e\'", None))
        self.label_2.setText(_translate(
            "Dialog", "Decryption code \'n\'", None))
        self.label_3.setText(_translate("Dialog", "Enter the Text", None))
        self.label_4.setText(_translate("Dialog", "Output", None))
        self.dcode.setText(_translate("Dialog", "Decryption code", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
