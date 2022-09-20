from typing import Union


class BBox:
    def __init__(self, l_x, t_y, w, h, conf):
        self._conf = conf

        self._l_x = l_x
        self._t_y = t_y
        self._r_x = l_x + w
        self._b_y = t_y + h

        self._w = w
        self._h = h

        self._c_x = l_x + float(w / 2)
        self._c_y = t_y + float(h / 2)

    @property
    def l_x(self) -> Union[float, int]:
        return self._l_x

    @property
    def t_y(self) -> Union[float, int]:
        return self._t_y

    @property
    def r_x(self) -> Union[float, int]:
        return self._r_x

    @property
    def b_y(self) -> Union[float, int]:
        return self._b_y

    @property
    def c_x(self) -> Union[float, int]:
        return self._c_x

    @property
    def c_y(self) -> Union[float, int]:
        return self._c_y

    @property
    def w(self) -> Union[float, int]:
        return self._w

    @property
    def h(self) -> Union[float, int]:
        return self._h

    @property
    def conf(self) -> float:
        return self._conf

    @property
    def top_left(self) -> Union[list, tuple]:
        return [self._l_x, self._t_y]

    @property
    def bottom_right(self) -> Union[list, tuple]:
        return [self._r_x, self._b_y]

    @property
    def center(self) -> Union[list, tuple]:
        return [self._c_x, self._c_y]

    @property
    def box_tlbr(self):
        return [self._l_x, self._t_y, self._r_x, self._b_y]

    @property
    def box_tlwh(self):
        return [self._l_x, self._t_y, self._w, self._h]

    @property
    def area(self) -> Union[float, int]:
        return self._w * self._h

    def is_pt_in(self, pt: Union[list, tuple]) -> bool:
        assert isinstance(pt, (list, tuple)) and len(pt) == 2
        return self._l_x <= pt[0] <= self._r_x and self._t_y <= pt[1] <= self._b_y

    def IoU(self, other) -> Union[float, int]:
        assert isinstance(other, BBox)

        intersection_l_x = max(self._l_x, other._l_x)
        intersection_r_x = min(self._r_x, other._r_x)
        intersection_t_y = max(self._t_y, other._t_y)
        intersection_b_y = min(self._b_y, other._b_y)

        s_intersection = abs(max((intersection_r_x - intersection_l_x, 0)) * max((intersection_b_y - intersection_t_y), 0))
        if s_intersection == 0:
            return 0

        iou = s_intersection / float(self.area + other.area - s_intersection)

        return iou

    def __iadd__(self, other):
        assert isinstance(other, BBox)
        self._l_x = min(self._l_x, other._l_x)
        self._t_y = min(self._t_y, other._t_y)
        self._r_x = max(self._r_x, other._r_x)
        self._b_y = max(self._b_y, other._b_y)

        self._c_x = (self._l_x + self._r_x) / 2
        self._c_y = (self._t_y + self._b_y) / 2

        return self

    def __str__(self) -> str:
        return str(f"{[self._l_x, self._t_y, self._w, self._h, self._conf]}")


if __name__ == "__main__":
    b = BBox(0, 0, 10, 10, 1.)
    p = BBox(9, 9, 10, 10, 1.)
    print(b.IoU(p))
    print(p.IoU(b))
