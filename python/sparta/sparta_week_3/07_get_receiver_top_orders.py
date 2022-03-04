top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0] * len(top_heights)  # [0, 0, 0, 0, 0]
    while top_heights:
        height = heights.pop()
        for idx in range(len(heights) - 1, 0, -1):
            if top_heights[idx] > height:
                answer[len(heights)] = idx + 1


print(get_receiver_top_orders(top_heights))  # 출력 = [0, 0, 2, 2, 4]
