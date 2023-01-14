import os

from PIL import Image
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (
    QFileDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ImageCompressor(QWidget):
    """
    A PyQt5 widget that allows the user to select an image, compress it and save it to a file.
    """

    def __init__(self):
        super().__init__()

        self.file_name: str

        # Create widgets
        self.image_label = QLabel()
        self.select_button = QPushButton("Select Image")
        self.compress_button = QPushButton("Compress Image")
        self.new_filename = QLineEdit()
        self.new_filename.setPlaceholderText("New Filename")

        # Connect buttons to functions
        self.select_button.clicked.connect(self.select_image)
        self.compress_button.clicked.connect(self.compress_image)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.new_filename)
        layout.addWidget(self.compress_button)

        # Set layout
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("Super Simple Image Compressor")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + "icon.ico"))
        self.setGeometry(100, 100, 400, 400)

    def select_image(self):
        """
        Open a file dialog for the user to select an image.
        The selected image is displayed on the self.image_label widget.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.png *.xpm *.jpg *.bmp);;All Files (*)",
            options=options,
        )
        if self.file_name:
            # Show image on label
            pixmap = QPixmap(self.file_name)
            self.image_label.setPixmap(pixmap)

    def compress_image(self):
        """
        Compress the currently displayed image on the self.image_label widget and save it to a file.
        The compressed image is saved in the same directory as the original image with the name 'compressed_image.jpg'
        or with a user-specified name if provided. A notification is displayed on the self.image_label widget showing
        the save location of the compressed image.
        """
        # Get image data
        image_data = self.image_label.pixmap().toImage()

        # Convert to PIL Image
        pil_image = Image.fromqimage(image_data)

        # Get save location
        original_location = "/".join(self.file_name.split("/")[:-1])
        new_filename = self.new_filename.text()

        if new_filename:
            new_file_location = f"{original_location}/{new_filename}.jpg"
        else:
            new_file_location = f"{original_location}/compressed_image.jpg"

        # Save image
        if new_filename:
            pil_image.save(new_file_location, "JPEG", optimize=True, quality=85)
        else:
            pil_image.save(
                f"{original_location}/compressed_image.jpg",
                "JPEG",
                optimize=True,
                quality=85,
            )

        # Show notification
        self.image_label.setText(f"Image Compressed to {new_file_location}")
