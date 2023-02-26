class Jar:

    def __init__(self,capacity=12):

        if capacity < 0:
            raise ValueError("Wrong capacity of cookies")

        self._capacity = capacity
        self._size = 0


    def __str__(self):

        a = '🍪' * self._size

        return a


    def deposit(self, n):


        if n > self.capacity:
            raise ValueError("exceed")
        if self._size + n > self.capacity:
            raise ValueError("exceed")

        self._size = self._size + n

    def withdraw(self,n):

        # if n > existing count raise value error

        if n > self._size:
            raise ValueError("not available")

        self._size = self._size - n


    @property
    def capacity(self):

        return self._capacity

    @property
    def size(self):

        return self._size








def main():

    # object instance of class
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()