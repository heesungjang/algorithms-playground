# Linked list


# 노드 생성 (클래스)

class Node:
    # constructor 생성
    # init 실행 --> self 할당 --> 초기 data 값  할당
    # 초기 next(포인터 값)은 None으로 설정
    def __init__(self, data, next=None) -> None: 
        self.data = data
        self.next = next


node_1 = Node(1)
node_2 = Node(3)
node_1.next = node_2


print(node_1.data) #가장 첫번째 노드

print(node_1.next.data) # 첫번째 노드와 연결된 다음 노드 (node_2)

print(node_2.data)

# node_1.next.data === node_2
# 이 경우 둘다 3을 출력

