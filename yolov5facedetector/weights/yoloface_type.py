from pathlib import Path
import gdown

WEIGHT_PATH = Path(__file__).parent.resolve()
CONFIG_PATH = (Path(__file__).parent.parent / 'models').resolve()

YOLOv5FACE_OPTION = dict(
    yolov5n=dict(
        weights_name='yolov5n_state_dict.pt',
        config_name='yolov5n.yaml',
        weight_file_link='https://github.com/BenedictusAryo/yoloface/releases/download/models/yolov5n_state_dict.pt'
    ),
    # S Model type have issue
    # yolov5s=dict(
    #     weights_name='yolov5s_state_dict.pt',
    #     config_name='yolov5s.yaml',
    #     weight_file_link='https://github.com/BenedictusAryo/yoloface/releases/download/models/yolov5s_state_dict.pt'
    # ),
    yolov5m=dict(
        weights_name='yolov5m_state_dict.pt',
        config_name='yolov5m.yaml',
        weight_file_link='https://github.com/BenedictusAryo/yoloface/releases/download/models/yolov5m_state_dict.pt'
    ),
    yolov5l=dict(
        weights_name='yolov5l_state_dict.pt',
        config_name='yolov5l.yaml',
        weight_file_link='https://github.com/BenedictusAryo/yoloface/releases/download/models/yolov5l_state_dict.pt'
    ),
)

def download_weight_file(yoloface_type:str):
    """Download pytorch pretrained weight file for yolov5face
    Place it in the weight folder"""
    if yoloface_type not in YOLOv5FACE_OPTION:
        raise ValueError('Not a valid YOLOv5Face Type')
    download_link = YOLOv5FACE_OPTION[yoloface_type]['weight_file_link']
    filename = YOLOv5FACE_OPTION[yoloface_type]['weights_name']
    gdown.download(download_link, str(WEIGHT_PATH/filename), quiet=False)