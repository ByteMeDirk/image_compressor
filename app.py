import sys

from PyQt5.QtWidgets import QApplication

from image_compressor import ImageCompressor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    compressor = ImageCompressor()
    compressor.show()
    sys.exit(app.exec_())
