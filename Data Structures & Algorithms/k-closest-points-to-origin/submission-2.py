import math


def quicksort(points: List[List[int]], arr: List[float], s: int, e: int) -> List[List[int]]:

    if(e - s + 1 <= 1):
        return points

    pivot = arr[e]
    pivot_pt = points[e]
    left = s

    for i in range(s, e):
        if(arr[i] < pivot):
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp

            tmp = points[left]
            points[left] = points[i]
            points[i] = tmp

            left += 1

    arr[e] = arr[left]
    arr[left] = pivot

    points[e] = points[left]
    points[left] = pivot_pt

    quicksort(points, arr, s, left-1)
    quicksort(points, arr, left+1, e)

    return points


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance_results = []
        arr = []
        for i in range(len(points)):
            arr = points[i]
            distance = math.sqrt((arr[0])**2 + (arr[1])**2) 
            distance_results.append(distance)

        e = len(points) - 1
        s = 0
        quicksort(points, distance_results, s, e)

        return points[:k]