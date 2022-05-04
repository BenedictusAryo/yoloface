# Yolov5 Face Detection

## Description
The project is a wrap over [yolov5-face](https://github.com/deepcam-cn/yolov5-face) repo. Made simple portable interface for model import and inference. Model detects faces on images and returns bounding boxes and coordinates of 5 facial keypoints, which can be used for face alignment.
## Installation
```bash
pip install yolov5facedetector
```
## Usage example
```python
from yolov5facedetector.face_detector import YoloDetector
import numpy as np
from PIL import Image

model = YoloDetector(target_size=720,gpu=0,min_face=90)
rgb_array_img = np.array(Image.open('test_image.jpg')) # Will make RGB Numpy Array Image
bboxes, confs, points = model.predict(rgb_array_img)
```
You can also pass several images packed in a list to get multi-image predictions.
```python
bboxes, confs, points = model.predict([image1,image2])
```

## Other pretrained models
Currently Support YOLOv5 type n,m & l type of model from [yolov5-face](https://github.com/deepcam-cn/yolov5-face) repo. Default model type is 'yolov5n' but you can change to m & l (larger model version) which is auto download when first time used

Example below:

```python
model = YoloFace(yolo_type='yolov5l',target_size=720) # Will download weight file automatically
bboxes, confs, points = model.predict(rgb_array_img)
```

## Result example
<img src="/results/result_example.jpg" width="600"/>

## Citiation
Thanks to [deepcam-cn](https://github.com/deepcam-cn/yolov5-face) for pretrained models and [Rebrikov Artem](https://github.com/elyha7/yoloface) for providing wrapper function of YOLOv5Face.

