# https://leetcode.com/problems/insert-interval/
# Definition for an interval.
import random

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[%d, %d]" % (self.start, self.end)

    def __repr__(self):
        return "[%d, %d]" % (self.start, self.end)


class Solution(object):
    def insert(self, intervals, newInterval):
        n = len(intervals)

        left = bisect_left(intervals, newInterval.start)
        if left > 0 and newInterval.start <= intervals[left-1].end:
            new_interval_start = intervals[left-1].start
        else:
            new_interval_start = newInterval.start

        right = bisect_right(intervals, newInterval.end)
        if right < n and newInterval.end >= intervals[right].start:
            new_interval_end = intervals[right].end
        else:
            new_interval_end = newInterval.end

        updated_new_interval = Interval(s=new_interval_start, e=new_interval_end)
        left = bisect_left(intervals, updated_new_interval.start)
        right = bisect_right(intervals, updated_new_interval.end)
        return intervals[0:left] + [updated_new_interval] + intervals[right:]


def bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid].start < x: lo = mid+1
        else: hi = mid
    return lo


def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid].end: hi = mid
        else: lo = mid+1
    return lo




def generate_test(n, interval):
    min_value = -100
    test_list = [0] * n
    start = int(random.random() * min_value)
    end = 0
    for index in range(n):
        end = start + int(random.random() * interval) + 1
        test_list[index] = Interval(s=start, e=end)
        start = end + int(random.random() * interval) + 1
    entire_range = end - min_value
    p1 = 0
    p2 = 0
    while p1 == p2:
        p1 = int(random.random() * entire_range) + min_value
        p2 = int(random.random() * entire_range) + min_value
    test_interval = Interval(s=min(p1, p2), e=max(p1, p2))
    return test_list, test_interval


def check_ans(ori_list, interval, new_list):
    verify_list = list(ori_list)
    verify_list.append(interval)
    for x in verify_list:
        start_bool = False
        end_bool = False
        for new_interval in new_list:
            if new_interval.start <= x.start <= new_interval.end:
                start_bool = True
            if new_interval.start <= x.end <= new_interval.end:
                end_bool = True
            if start_bool and end_bool:
                break
        if not start_bool or not end_bool:
            return False
    return True


def verify_ans(ori_list, interval, new_list):
        print("====================")
        print(ori_list)
        print(interval)
        print(new_list)
        print("result = ", check_ans(ori_list, interval, new_list))


def convert_interval(value_list):
    return_list = []
    for value in value_list:
        start, end = value
        return_list.append(Interval(s=start, e=end))
    return return_list


a = Solution()
a_list = convert_interval([[1, 3], [5, 6], [9, 12]])
# x = Interval(s=-1, e=0)
# verify_ans(a_list, x, a.insert(a_list, x))
# x = Interval(s=-1, e=1)
# verify_ans(a_list, x, a.insert(a_list, x))
# x = Interval(s=13, e=15)
# verify_ans(a_list, x, a.insert(a_list, x))
# x = Interval(s=12, e=15)
# verify_ans(a_list, x, a.insert(a_list, x))
# x = Interval(s=4, e=7)
# verify_ans(a_list, x, a.insert(a_list, x))
# x = Interval(s=3, e=9)
# verify_ans(a_list, x, a.insert(a_list, x))
for _ in range(50):
    test_list, test_interval = generate_test(20, 10)
    print(test_list)
    print(test_interval)
    new_intervals = a.insert(test_list, test_interval)


