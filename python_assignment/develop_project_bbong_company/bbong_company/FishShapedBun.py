from .enums.FishShapedBunType import FishShapedBunType


class FishShapedBun:
    def __init__(self, bun_type: FishShapedBunType):
        self.bun_type = bun_type
        self.name = bun_type.name
        self.price = bun_type.price


class RedBeanFishShapedBun:
    def __init__(self):
        super().__init__(bun_type=FishShapedBunType.RED_BEAN)


class PizzaFishShapedBun:
    def __init__(self):
        super().__init__(bun_type=FishShapedBunType.PIZZA)


class PuffFishShapedBun:
    def __init__(self):
        super().__init__(bun_type=FishShapedBunType.PUFF)
