class InserationSort():

    def __init__(self, array):
        self.array = array

    def sort(self):
        i = 1
        while (i < len(self.array)):
            j = i
            while ((j > 0) and (self.array[j-1] > self.array[j])):
                temp = self.array[j-1]
                self.array[j-1] = self.array[j]
                self.array[j] = temp
                j -= 1
            i += 1
