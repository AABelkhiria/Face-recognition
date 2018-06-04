# Face-recognition

Face Detection is a field of computer vision that detects a human face in a digital image.
This is a specific case of object detection, where one seeks to detect the presence and precise location of one or more faces in an image.
It is one of the most studied areas of computer vision, with numerous publications, patents, and specialized conferences.

OpenCV (Open Computer Vision) is a free graphics library, originally developed by Intel, specializing in real-time image processing.

* The OpenCV library provides a wide range of features to create programs from raw data to basic graphical user interfaces.

**This project is done under Raspberry Pi.**

A sample was developed on the Raspberry Pi under Python 2.7, and the rest of the applications were developed under PC with Python 3. The choice of the Python version is the version of OpenCV available under these two platforms.

### Installation

The installation is done by

```
pip install opencv-python
```

### Usage

The function that captures data from the camera is:

```python
cap = cv2.VideoCapture(0)
```

* This function is not valid for the Raspberry Pi camera as it is not considered a device. So the best solution is to save the data under a binary data stream under the IOStream library.

Python at Raspbian OS includes a library to use the camera of the Raspberry Pi, this one is called by:

```python
from picamera       import PiCamera
from picamera.array import PiRGBArray
```

* For speed of execution, it is best to process the image after it has been converted to gray level (An RGB image is a structure made up of 3 matrices, one for each base color, although a gray-level image is a matrix for the shade of gray for each pixel varying from 0 to 255)
