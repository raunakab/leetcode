use rust_sudoku_iters::*;

fn main() {
    let row_iter = RowIter::new(9);
    for position in row_iter {
        println!("{:?}", position);
    }

    let column_iter = ColumnIter::new(9);
    for position in column_iter {
        println!("{:?}", position);
    }

    let square_iter = SquareIter::new(3);
    for position in square_iter {
        println!("{:?}", position);
    }
}
