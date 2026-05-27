class PhoneBook:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def add(self, name, phone):
        index = self.hash_function(name)

        for item in self.table[index]:
            if item[0] == name:
                item[1] = phone
                return

        self.table[index].append([name, phone])

    def get(self, name):
        index = self.hash_function(name)

        for item in self.table[index]:
            if item[0] == name:
                return item[1]

        return "Контакт не знайдено"

    def remove(self, name):
        index = self.hash_function(name)

        for item in self.table[index]:
            if item[0] == name:
                self.table[index].remove(item)
                return "Контакт видалено"

        return "Контакт не знайдено"