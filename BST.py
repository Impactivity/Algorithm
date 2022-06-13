class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = self



class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self,value):
        self.current_node = self.head

        while True:
            # 현재 head노드의 값보다 삽입하려는 값이 클 경우
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    insert_Node = Node(value)
                    insert_Node.parent = self.current_node
                    self.current_node.left = insert_Node
                    break

            # 현재 head노드의 값보다 삽입하려는 값이 작을 경우
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    insert_Node = Node(value)
                    insert_Node.parent = self.current_node
                    self.current_node.right = insert_Node
                    break


    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return self.current_node
            elif self.current_node.value < value:
                self.current_node = self.current_node.right
            else:
                self.current_node = self.current_node.left
        return None

    def delete(self,value):
        self.current_node = self.search(value)

        if self.current_node:
            #1. 삭제하려는 노드가 leaf node 일때 leaf 노드 삭제
            if self.current_node.left == None and self.current_node.right == None:
                self.current_node = None

            # 2. 삭제하려는 노드의 child node가 하나만 존재할 때
            # 2-1 삭제할 노드의 오른쪽 자식만 존재하는 경우
            elif self.current_node.right != None and self.current_node.left == None:
                # 삭제할 노드가 부모 왼쪽에 있는 경우
                if self.current_node.parent.left == self.current_node:
                    self.current_node.parent.left = self.current_node.right
                    self.current_node.right.parent = self.current_node.parent
                    self.current_node = None
                # 삭제할 노드가 오른쪽에 있는 경우
                else:
                    self.current_node.parent.right = self.current_node.right
                    self.current_node.right.parent = self.current_node.parent
                    self.current_node = None

            # 2-2 삭제할 노드의 왼쪽 노드만 존재하는 경우
            elif self.current_node.right == None and self.current_node.left != None:
                # 삭제할 노드가 부모 왼쪽에 있는 경우
                if self.current_node.parent.left == self.current_node:
                    self.current_node.parent.left  = self.current_node.left
                    self.current_node.left.parent = self.current_node.parent
                    self.current_node = None
                else:#삭제할 노드가 부모 오른쪽에 있는 경우
                    self.current_node.parent.right = self.current_node.left
                    self.current_node.left.parent = self.current_node.parent
                    self.current_node = None
            #3. 삭제하려는 노드의 child node가 두 개 존재할 때
            # 3-1 삭제하려는 노드의 오른쪽 노드의 child중 가장 왼쪽(가장 작은 값)에 있는 노드가 올라옴
            # 3-2 올라온 노드의 왼쪽 오른쪽은 삭제할 노드의 왼쪽, 오른쪽 자식을 가리키게 된다.
            # 3-3 만일 올라온 노드가 원래 오른쪽 자식을 가지고 있는 경우에는 올라온 노드의 오른쪽 자식이된다 ?
            else:
                print('여기 ')
                self.change_node = self.current_node.right

                while True:
                    if self.change_node.left != None:
                        self.change_node = self.change_node.left
                    else:
                        break

                print(f'현재 삭제하려는 노드 : {self.current_node.value}, 삭제하려는 노드의 parent : {self.current_node.parent.value} , 삭제노드를 대체할 노드 : {self.change_node.value}' )

                # 부모노드를 바꿔주고 부보노드에서 가리키는 자식노드도 바꿔준다.
                self.change_node.parent = self.current_node.parent
                if self.current_node.parent.right == self.current_node:
                    self.current_node.parent.right = self.change_node
                else:
                    self.current_node.parent.left = self.change_node

                # 대체할 노드가 Leaf 노드라면 바로 교체
                if self.change_node.right == None:
                    self.current_node = self.change_node
                    self.change_node.right = None

                else:
                    print('대체할 노드의 자식이 존재')
                    self.current_node = self.change_node
                    self.current_node.right.left = self.change_node.right

                print(f'현재 대체된  노드 : {self.current_node.value} , 대체된 노드의 parent: {self.current_node.parent.right.value}')

            return

        else: #현재 삭제하려는 노드가 존재하지 않을 경우 false
            return False






head = Node(4)
BST = NodeMgmt(head)

BST.insert(2)
BST.insert(6)
BST.insert(5)
BST.insert(7)
BST.insert(8)
BST.insert(5.5)
BST.delete(6)
print(BST.search(4).right.value , BST.search(4).right.right.value)


