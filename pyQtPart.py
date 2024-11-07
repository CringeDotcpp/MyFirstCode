import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

import LatexCompil
import calcuate

class LaTeX(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LaTeX")

        self.default_image = QLabel(self)
        self.default_image.setPixmap(QPixmap("formula.png"))
        self.default_image.setAlignment(Qt.AlignCenter)
        self.default_image.setScaledContents(True)

        self.input_field = QLineEdit(self)
        self.input_field.textChanged.connect(self.update)

        self.font = QFont()
        self.font.setPointSize(20)

        self.result_field = QLabel(self)
        self.result_field.setFixedHeight(50)
        self.result_field.setFont(self.font)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.result_field)
        self.layout.addWidget(self.default_image)

    def update(self, text):
        self.update_image(text)
        self.update_result(text)

    def update_result(self, text):
        try:
            result = calcuate.calc(text)            
            self.result_field.setText("Result: " + str(result))
        except: pass

    def update_image(self, text):
        try:
            LatexCompil.main(text)

            pixmap = QPixmap("formula.png")

            label_width = self.default_image.width()
            label_height = self.default_image.height()

            scale_factor = min(label_width / pixmap.width(), label_height / pixmap.height())

            scaled_pixmap = pixmap.scaled(
                int(pixmap.width() * scale_factor), 
                int(pixmap.height() * scale_factor), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )

            self.default_image.setPixmap(scaled_pixmap)
        except Exception as e: pass
            # print(f"Ошибка: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LaTeX()
    window.show()
    sys.exit(app.exec_())
