# 노드 생성 (클래스)

class Node:
    # constructor 생성
    # init 실행 --> self 할당 --> 초기 data 값  할당
    # 초기 next(포인터 값)은 None으로 설정
    def __init__(self, data, next=None) -> None: 
        self.data = data
        self.next = next


# 링크드 리스트(클래스)

    class LinkedList:
        def __init__(self,value):
            """
            1. 첫 head로 초기
            2. 값으로 전달 받은 Node 설정
            """
            self.head = Node(value)  

        def append(self, value):
            """
            1. 링크드 리스트 노드 추가
            2. 가장 마지막 Node 다음에 추가해야 하므로
            3. 현재 Node의 next pointer 값이 없을때 까지 선회
            4. 마지막 node가 cur 값으로 들어왔을때 next 값을 추가하는 Node로 할당

            """
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(value)