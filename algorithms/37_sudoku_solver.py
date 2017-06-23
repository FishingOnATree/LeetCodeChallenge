# https://leetcode.com/problems/sudoku-solver/#/description


class Solution(object):

    def __init__(self):
        self.rows = 'ABCDEFGHI'
        self.cols = '123456789'
        self.boxes = self.cross(self.rows, self.cols)
        row_units = [self.cross(r, self.cols) for r in self.rows]
        col_units = [self.cross(self.rows, c) for c in self.cols]
        box_units = [self.cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
        self.unitlist = row_units + col_units + box_units

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        values = self.grid_value(board)
        values = self.search(values)
        display(values, self.boxes, self.rows, self.cols)

    def search(self, values):
        values = self.reduce_choices(values)
        if not values:
            return False
        elif self.count_solved(values) == 81:
            return values
        else:
            # recursively search
            min_choice = 9
            min_boxes = []
            for box, choice in filter(lambda item: len(item[1]) > 1, values.items()):
                if len(choice) < min_choice:
                    min_boxes = [box]
                    min_choice = len(choice)
                elif len(choice) == min_choice:
                    min_boxes.append(box)
            print(min_boxes)
            display(values, self.boxes, self.rows, self.cols)
            chosen_box = min_boxes[0]
            for digit in values[chosen_box]:
                new_values = dict(values)
                new_values[chosen_box] = digit
                result = self.search(new_values)
                if result:
                    return result

    def reduce_choices(self, values):
        stalled = False
        while not stalled:
            solved_before = self.count_solved(values)
            values = self.eliminate(values)
            values = self.only_choice(values)
            solved_after = self.count_solved(values)
            stalled = solved_before == solved_after
            if len([1 for v in values.values() if len(v) == 0]):
                return False
        return values

    @staticmethod
    def count_solved(value):
        return sum([1 for v in value.values() if len(v) == 1])

    @staticmethod
    def cross(r, c):
        return [a + b for a in r for b in c]

    def grid_value(self, board):
        return {box: value if value != '.' else self.cols for box, value in zip(self.boxes, board)}

    def eliminate(self, values):
        # 123
        new_value = dict(values)
        for k, v in values.items():
            if len(v) > 1:
                not_possible = set(values[box] for unit in filter(lambda u: k in u, self.unitlist) for box in unit if len(values[box]) == 1)
                new_value[k] = ''.join(num for num in v if num not in not_possible)
        return new_value

    def only_choice(self, values):
        for unit in self.unitlist:
            for d in '123456789':
                d_possible = [box for box in unit if d in values[box]]
                if len(d_possible) == 1:
                    values[d_possible[0]] = d
        return values

def display(values, boxes, rows, cols):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

a = Solution()
#a.solveSudoku('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
a.solveSudoku('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')