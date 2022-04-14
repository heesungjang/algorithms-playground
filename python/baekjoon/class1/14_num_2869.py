from math import ceil
move_up, move_down, total_length = map(int, input().split())

count_day = 0

day = (((total_length - move_up)/(move_up-move_down))+1)

print(ceil(day))