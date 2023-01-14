from setuptools import setup

setup(
    name="Image Compressor",
    version="1.0",
    packages=["image_compressor"],
    url="https://github.com/dirkscgm/image-compressor",
    license="MIT",
    author="DirkSCGM",
    author_email="dirkscgm@gmail.com",
    description="A PyQt5 widget that allows the user to select an image, compress it and save it to a file.",
    install_requires=["pyinstaller", "Pillow"],
)
