class Sorter:
    def __init__(self, data):
        self.data = data

    def bubble_sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
        return self.data
    def selection_sort(self):
        n = len(self.data)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
        return self.data

    def recursive_sort(self, arr=None):
        if arr is None:
            arr = self.data
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return self.recursive_sort(less) + [pivot] + self.recursive_sort(greater)

# Exemplo de uso
data = [64, 34, 25, 12, 22, 11, 90]
sorter = Sorter(data)

print("Bubble Sort:", sorter.bubble_sort())
sorter.data = data  # Resetando os dados
print("Selection Sort:", sorter.selection_sort())
sorter.data = data  # Resetando os dados
print("Recursive Sort:", sorter.recursive_sort())

