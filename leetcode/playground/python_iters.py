SUB_LENGTH = 2
LENGTH = SUB_LENGTH**2


class RowIter:
    def __init__(self, length):
        self.position = [0, 0]
        self.length = length

    def __iter__(self):
        return self

    def __next__(self):
        position = self.position
        y = position[0]
        x = position[1]
        length = self.length
        if y < length and x < length:
            if x < length - 1:
                new_x = x + 1
                carry = 0
            else:
                new_x = 0
                carry = 1
            new_y = y + carry
            self.position = [new_y, new_x]
            return position
        else:
            raise StopIteration


class ColumnIter:
    def __iter__(self, length):
        self.length = length
        self.position = [0, 0]
        return self

    def __next__(self):
        position = self.position
        y = position[0]
        x = position[1]
        length = self.length
        if y < length and x < length:
            if y < length - 1:
                new_y = y + 1
                carry = 0
            else:
                new_y = 0
                carry = 1
            new_x = x + carry
            self.position = [new_y, new_x]
            return position
        else:
            raise StopIteration

    pass


def calc_position(
    sub_length,
    oy,
    ox,
    iy,
    ix,
):
    y = (sub_length * oy) + iy
    x = (sub_length * ox) + ix
    return [y, x]


class SquareIter:
    def __init__(self, sub_length):
        self.inner = RowIter(sub_length)
        self.outer = RowIter(sub_length)
        self.sub_length = sub_length

    def __iter__(self):
        return self

    def __next__(self):
        sub_length = self.sub_length
        try:
            [inner_y, inner_x] = next(self.inner)
            [outer_y, outer_x] = self.outer.position
            return calc_position(sub_length, outer_y, outer_x, inner_y, inner_x)
        except StopIteration:
            try:
                [outer_y, outer_x] = next(self.outer)
                print(outer_y, outer_x)
                self.inner = RowIter(sub_length)
                [inner_y, inner_x] = next(self.inner)
                if outer_y == 0 and outer_x == 0 and inner_y == 0 and inner_x == 0:
                    print("all are zero 2")
                return calc_position(sub_length, outer_y, outer_x, inner_y, inner_x)
            except StopIteration:
                raise StopIteration

        # position = self.position
        # y_off = self.y_off
        # x_off = self.x_off
        # if y_off < SUB_LENGTH and x_off < SUB_LENGTH:
        #     sub_y = position[0] % SUB_LENGTH
        #     sub_x = position[1] % SUB_LENGTH
        #     if sub_x < SUB_LENGTH - 1:
        #         new_sub_x = sub_x + 1
        #         carry = 0
        #     else:
        #         new_sub_x = 0
        #         carry = 1
        #     new_sub_y = sub_y + carry
        #     self.position = [
        #         new_sub_y + (3 * y_off),
        #         new_sub_x + (3 * x_off),
        #     ]
        #     return position
        # else:
        #     raise StopIteration


# for position in RowIter():
# print(position)
# for position in ColumnIter():
#     print(position)
for position in SquareIter(sub_length=3):
    pass
    # print(position)
