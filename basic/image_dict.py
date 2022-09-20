from pathlib import Path

from .bbox_list import BBoxList


class ImageDict(dict):
    """
    image_dict =
    {
        cat_id: bbox_list,
    }
    """
    def __init__(self, image_path: Path = None, dest_path: Path = None, conf_thres: float = None):
        super().__init__()

        self.path = image_path
        self.dest_path = dest_path
        self._conf_thres = conf_thres if conf_thres is not None else .0

    def set_conf_thres(self, conf_thres: float = None):
        self._conf_thres = conf_thres if conf_thres is not None else .0
        for cat_id in self:
            self[cat_id].set_conf_thres(conf_thres=self._conf_thres)

    @property
    def conf_thres(self) -> float:
        return self._conf_thres

    @property
    def len(self) -> int:
        length = 0
        for cat_id in self:
            length += self[cat_id].len
        return length

    @property
    def raw_len(self) -> int:
        raw_length = 0
        for cat_id in self:
            raw_length += self[cat_id].raw_len
        return raw_length

    def __setitem__(self, cat_id: int, bbox_list: BBoxList):
        assert isinstance(cat_id, int) and isinstance(bbox_list, BBoxList)
        dict.__setitem__(self, cat_id, bbox_list)
