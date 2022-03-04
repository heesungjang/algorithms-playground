class Node {
  constructor(value, next) {
    this.value = value;
    this.next = next;
  }
}

class Stack {
  constructor() {
    this.top = null;
  }

  pop() {
    if (this.top) {
      let topNode = this.top;
      this.top = this.top.next;
      return topNode.value;
    }
  }

  push(value) {
    let currTopNode = this.top;
    let newTopNode = new Node(value);
    newTopNode.next = currTopNode;
    this.top = newTopNode;
  }

  isEmpty() {
    return this.top === null;
  }
}

const stack = new Stack();

console.log(stack.isEmpty());
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack.isEmpty());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.isEmpty());
console.log(stack.pop());
