pub struct RowIter {
    x: u8,
    y: u8,
    length: u8,
}

impl RowIter {
    pub fn new(length: u8) -> Self {
        Self { x: 0, y: 0, length }
    }

    fn curr(&self) -> Option<(u8, u8)> {
        if self.y < self.length && self.x < self.length {
            Some((self.y, self.x))
        } else {
            None
        }
    }

    fn clear(&mut self) {
        self.y = 0;
        self.x = 0;
    }
}

impl Iterator for RowIter {
    type Item = (u8, u8);

    fn next(&mut self) -> Option<Self::Item> {
        self.curr().map(|(y, x)| {
            let (new_x, carry) = if x < self.length - 1 {
                (x + 1, 0)
            } else {
                (0, 1)
            };
            let new_y = y + carry;
            let pos = (y, x);
            self.y = new_y;
            self.x = new_x;
            pos
        })
    }
}

struct InfiniteRowIter(RowIter);

impl Iterator for InfiniteRowIter {
    type Item = (u8, u8);

    fn next(&mut self) -> Option<Self::Item> {
        let pos = self.0.next().unwrap_or_else(|| {
            self.0.clear();
            self.0.next().unwrap()
        });
        Some(pos)
    }
}

pub struct ColumnIter(RowIter);

impl ColumnIter {
    pub fn new(length: u8) -> Self {
        Self(RowIter::new(length))
    }
}

impl Iterator for ColumnIter {
    type Item = (u8, u8);

    fn next(&mut self) -> Option<Self::Item> {
        self.0.next().map(|(y, x)| (x, y))
    }
}

pub struct SquareIter {
    sub_length: u8,
    length: u8,
    index: u8,
    outer: RowIter,
    inner: InfiniteRowIter,
}

impl SquareIter {
    pub fn new(sub_length: u8) -> Self {
        Self {
            sub_length,
            length: sub_length.pow(2),
            index: 0,
            outer: RowIter::new(sub_length),
            inner: InfiniteRowIter(RowIter::new(sub_length)),
        }
    }
}

impl Iterator for SquareIter {
    type Item = (u8, u8);

    fn next(&mut self) -> Option<Self::Item> {
        let (iy, ix) = self.inner.next().unwrap();
        let outer = if self.index == self.length - 1 {
            self.outer.next()
        } else {
            self.outer.curr()
        };
        self.index = (self.index + 1) % self.length;
        outer.map(|(oy, ox)| {
            let y = (self.sub_length * oy) + iy;
            let x = (self.sub_length * ox) + ix;
            (y, x)
        })
    }
}
