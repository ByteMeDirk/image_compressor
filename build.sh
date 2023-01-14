pyinstaller \
--noconfirm \
--onefile \
--windowed \
--icon "image_compressor/icon.ico" \
--name "Image Compressor" \
--add-data "README.md;." \
--add-data "requirements.txt;." \
--add-data "setup.py;." \
--add-data "image_compressor;image_compressor/"  \
"app.py"