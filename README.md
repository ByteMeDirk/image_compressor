# Image Compressor

[Download](https://github.com/DirksCGM/image_compressor/raw/main/dist/Image%20Compressor.exe)

A PyQt5 widget that allows the user to select an image, compress it and save it to a file.

The code is totally opensource, so check it out, it simply does what it says on the box :D

## Getting Started

Clone the repository to your local machine

```commandline
git clone https://github.com/yourusername/image-compressor.git
```

Install the requirements

```commandline
pip install -r requirements.txt
```

Run the app

```commandline
python main.py
```

## Using the App

### By Using the app.py file

Click on the 'Select Image' button to select an image from your local machine.
Click on the 'Compress Image' button to compress the selected image.
The compressed image will be saved in the same directory as the original image with the name 'compressed_image.jpg' or
with a user-specified name if provided.
A notification will be displayed on the self.image_label widget showing the save location of the compressed image.

### By using the .exe

Simply download the `dist/Image Compressor.exe` to your computers applications directory, create a shortcut to your
Desktop or pin it, and use it like any other applciation.

## Built With

PyQt5 - The GUI framework used
Pillow - A Python Imaging Library

## Contributing

Fork the repository
Create your feature branch (git checkout -b my-new-feature)
Commit your changes (git commit -am 'Add some feature')
Push to the branch (git push origin my-new-feature)
Create a new Pull Request

## Authors

DirkSCGM

# License

This project is licensed under the MIT License - see the LICENSE.md file for details
