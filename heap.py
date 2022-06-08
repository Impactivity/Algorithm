class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    #insert할때 크기비교하여 노드 위치 올리기
    def move_up(self,inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx//2
        if self.heap_array[parent_idx] < self.heap_array[inserted_idx]:
            return True
        else:
            return False

    def insert(self,data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[parent_idx], self.heap_array[inserted_idx] = self.heap_array[inserted_idx],self.heap_array[parent_idx]
            inserted_idx = parent_idx


    def move_down(self, parent_idx):
        if parent_idx >= len(self.heap_array) - 1:
            return False


        child_left = parent_idx * 2
        child_right = parent_idx * 2 + 1

        # case 1) 오른쪽 자식이 존재하는 경우
        if child_right < len(self.heap_array) - 1:
            #왼쪽 자식과 오른쪽 자식을 비교하여 next_idx를 결정한다.
            if self.heap_array[child_right] < self.heap_array[child_left]:
                next_idx = child_left
            else:
                next_idx = child_right
        # case 2) 오른쪽 자식이 없고 왼쪽 자식만 있는 경우
        elif child_left < len(self.heap_array)-1:
                next_idx = child_left
        # 자식이 존재하지 않는 경우
        else:
            return False



        if self.heap_array[parent_idx] >= self.heap_array[next_idx]:
            return False
        else:
            return next_idx


    def delete(self):
        if len(self.heap_array) <= 1:
            return None
        self.heap_array[-1],self.heap_array[1] = self.heap_array[1],self.heap_array[-1]
        del_data = self.heap_array.pop()
        cur_idx = 1
        while True:
            idx = self.move_down(cur_idx)
            if idx:
                self.heap_array[idx],self.heap_array[cur_idx] = self.heap_array[cur_idx],self.heap_array[idx]
                cur_idx = idx
            else:
                break

        return del_data