from mmdet.datasets.builder import DATASETS
from mmdet.datasets.coco import CocoDataset


@DATASETS.register_module()
class GrapesDataset(CocoDataset):

    CLASSES = ('grapes')