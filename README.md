QRScanner
QRScanner is a Python library and command-line tool for scanning and decoding QR codes from images or video streams.

Features
Scan QR codes from images or video streams
Decode QR code data
Support for various image formats (JPEG, PNG, etc.)
Command-line interface for easy usage
Simple and intuitive API for integration into Python applications
Installation
You can install QRScanner using pip:

bash
Copy code
pip install qrscanner
Usage
Command Line
Scan a QR code from an image file:

bash
Copy code
qrscan image.jpg
Scan a QR code from a video stream:

bash
Copy code
qrscan --video
For more options, use the --help flag:

bash
Copy code
qrscan --help
Python API
python
Copy code
from qrscanner import QRScanner

# Create a QRScanner instance
scanner = QRScanner()

# Scan QR code from an image file
result = scanner.scan_image('image.jpg')
print("QR Code Data:", result.data)

# Scan QR code from a video stream
result = scanner.scan_video()
print("QR Code Data:", result.data)
For more advanced usage and options, refer to the documentation.

Documentation
The official documentation for QRScanner can be found here.

Contributing
Contributions are welcome! If you have any ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

