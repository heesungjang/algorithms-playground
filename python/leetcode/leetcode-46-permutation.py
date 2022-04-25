from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    # 탐색이 끝나면 조합된 순열을 추가
    result = []

    # 현재 탐색중인 순열 조합
    nums_set = []

    def dfs(elements):
        # 종료 케이스
        if len(elements) == 0:
            # 다름 dfs 탐색에서 같은 리스트를 사용하기 때문에 레프런스가 아닌 새로운 배열을 추가
            result.append(nums_set[:])

        for num in elements:
            # 마찬가지로 elements는 다음 num에도 같은 같으로 사용되므로
            # 새로운 리스트를 생성
            new_list = elements[:]
            # 방문처리 := 현재 이미 사용한 숫자는 다음 dfs 탐색에서 제외
            new_list.remove(num)

            nums_set.append(num)
            dfs(new_list)

            # 백트래킹 하면서 올라올때 num을 다시 pop해줘서 빈 배열로 다시 만들어줌
            nums_set.pop()

    # dfs 탐색 시작
    dfs(nums)

    # dfs 탐색이 끝나면 result 반환
    return result


result = permute([1, 2, 3])

print(result)
