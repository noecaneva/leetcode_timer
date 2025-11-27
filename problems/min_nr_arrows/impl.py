from typing import List

def findMinArrowShots_naive(points: List[List[int]]) -> int:
    # Sort the right hand side of the ballons
    # at the end of the ballon we HAVE to pop it, it is a deadline
    # because at the latest at that point we have to throw an arrow
    points.sort(key=lambda x: x[1])
    arrows = 0
    while points:
        arrow_point = points[0][1]
        arrows += 1
        points[:] = [p for p in points if p[0] > arrow_point]
    
    return arrows

def findMinArrowShots_is_compare(points: List[List[int]]) -> int:
    points.sort(key=lambda x: x[1])
    arrows_shot = 0

    last_arrow_shot = None
    for start_ball, end_ball in points:
        # In case we have a new start which is not overlapping
        # shoot balloon, otherwhise it is already taken care of
        if (last_arrow_shot is None) or (start_ball > last_arrow_shot):
            arrows_shot += 1
            last_arrow_shot = end_ball

def findMinArrowShots_equal_compare(points: List[List[int]]) -> int:
    points.sort(key=lambda x: x[1])
    arrows_shot = 0

    last_arrow_shot = None
    for start_ball, end_ball in points:
        # In case we have a new start which is not overlapping
        # shoot balloon, otherwhise it is already taken care of
        if (last_arrow_shot == None) or (start_ball > last_arrow_shot):
            arrows_shot += 1
            last_arrow_shot = end_ball
        
        return arrows_shot

SOLUTIONS = {
    "find_arr_naive": findMinArrowShots_naive,
    "find_arr_compare_is": findMinArrowShots_is_compare,
    "find_arr_compare_equal": findMinArrowShots_equal_compare,
}