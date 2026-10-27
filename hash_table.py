class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
            return

        for i, (existing_key, _) in enumerate(self.table[index]):
            if existing_key == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if bucket is None:
            return None

        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if bucket is None:
            return

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                if not bucket:
                    self.table[index] = None
                return
