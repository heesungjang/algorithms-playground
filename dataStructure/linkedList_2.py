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

    def print_all(self):
        """
        현재 연결 리스트에 모든 Node를 출력하는 method
        
        1. 노드의 next 즉 다음 node가 없는 마지막 tail 노드까지 순회하며 데이터를 출력한다.
        """
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        """
        index로 특정 노드 반환
        1. count 0 즉 0번째 index부터 인자 값으로 받은 index까지 순환하며 node를 옮겨간다.
        2. 해당 index에 이르면 현재 node를 반환.
        """
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        new_node = Node(value)
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node


# head_node = Node(1)
# print(head_node.data) # 첫번째 노드

new_linkedList = LinkedList(1)

print(new_linkedList.get_node(0).data)

