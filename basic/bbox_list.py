from .bbox import BBox


class BBoxList(list):
    def __init__(self, conf_thres: float = None, bbox_list: list = None):
        super().__init__()

        self._conf_thres = conf_thres if conf_thres is not None else .0

        self.raw_list = list()

        for bbox in bbox_list if bbox_list is not None else []:
            self.raw_list.append(bbox)
            if bbox.conf >= self._conf_thres:
                list.append(self, bbox)

    def append(self, bbox: BBox) -> bool:
        assert isinstance(bbox, BBox)
        self.raw_list.append(bbox)
        if bbox.conf >= self._conf_thres:
            list.append(self, bbox)
            return True
        return False

    def remove(self, bbox: BBox) -> None:
        if bbox in self.raw_list:
            self.raw_list.remove(bbox)
            if bbox in self:
                list.remove(self, bbox)

    def extend(self, bboxes) -> None:
        assert isinstance(bboxes, BBoxList)
        for bbox in bboxes:
            self.append(bbox)

    def all_clear(self):
        self._conf_thres = .0
        self.raw_list.clear()
        list.clear(self)

    def set_conf_thres(self, conf_thres: float = None) -> None:
        self._conf_thres = conf_thres if conf_thres is not None else .0
        list.clear(self)
        for bbox in self.raw_list:
            if bbox.conf >= self._conf_thres:
                list.append(self, bbox)

    @property
    def conf_thres(self) -> float:
        return self._conf_thres

    @property
    def len(self) -> int:
        return len(self)

    @property
    def raw_len(self) -> int:
        return len(self.raw_list)
