class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.length = 0;
  }

  //display
  display() {
    let currNode = this.head;
    let displayingString = "[";
    if (!this.head) {
      return console.log("[]");
    }

    while (currNode.next !== null) {
      displayingString += `${currNode.value}, `;
      currNode = currNode.next;
    }
    displayingString += `${currNode.value}, ]`;
    console.log(displayingString);
  }

  // unshift - 리스트 앞에 삽입
  unshift(value) {
    /**
     * 1. 새로운 노드의 next 값이 현재 head의 값이됨
     * 2. this.head는 새로 만들어진 node가 됨
     */
    this.head = new Node(value, this.head);
    this.length++;
  }

  //append

  append(value) {
    let newNode = new Node(value);
    let curr;

    if (!this.head) {
      this.head = newNode;
    } else {
      curr = this.head;

      while (curr.next) {
        curr = curr.next;
      }

      curr.next = newNode;
    }

    this.length++;
  }

  //insert at index - 중간 삽입

  insert(value, index) {
    // If index is out of range
    if (index > 0 && index >= this.length) {
      return;
    }

    // If first index
    if (index === 0) {
      this.head = new Node(value, this.head); //결국 unshift랑 같음
      this.size++;
      return;
    }

    const node = new Node(value);
    let curr, prev;

    curr = this.head;
    let count = 0;

    while (count < index) {
      prev = curr;
      count++;
      curr = curr.next;
    }

    node.next = curr;
    prev.next = node;
    this.length++;
  }

  getAt(index) {
    let current = this.head;
    let count = 0;

    while (current) {
      //해당 data의 값을 가져오기 위해 index와 값이 같아질때까지 loop한다.
      if (count == index) {
        return console.log(current.value);
      }

      count++;
      current = current.next;
    }
    return null;
  }

  removeAt(index) {
    if (index > 0 && index > this.size) {
      return;
    }

    let current = this.head; //current는 현재 첫번째 노드임
    let previous;
    let count = 0;

    // Remove first
    if (index === 0) {
      this.head = current.next;
    } else {
      //loop를 통해 해당 index의 연결고리를 끊는다.
      while (count < index) {
        count++;
        previous = current;
        current = current.next;
      }
      previous.next = current.next;
    }

    this.size--;
  }

  clearList() {
    this.head = null;
    this.size = 0;
  }
}

const newLinkedList = new LinkedList();
newLinkedList.append(200);
newLinkedList.append(200);
newLinkedList.append(200);

newLinkedList.display();
newLinkedList.append(2);
newLinkedList.display();
newLinkedList.unshift(1);
newLinkedList.display();
newLinkedList.insert("123", 2);

newLinkedList.display();

newLinkedList.getAt(1);
