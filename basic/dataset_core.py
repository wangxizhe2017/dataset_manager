class DatasetCore(dict):
    def __init__(self, conf_thres: float = None):
        super().__init__()

        self._conf_thres = conf_thres if conf_thres is not None else .0

    @property
    def len(self) -> int:
        length = 0
        for image_id in self:
            length += self[image_id].len
        return length

    @property
    def raw_len(self) -> int:
        raw_length = 0
        for image_id in self:
            raw_length += self[image_id].raw_len
        return raw_length
