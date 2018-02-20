
class Matrix:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.matrix = []
    """
    SETTERS AND GETTERS FOR PROPERTIES
    """
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x_size):
        self._x = x_size

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y_size):
        self._y = y_size

    """
    METHODS
    """

    def create_matrix(self):
        self.matrix = [['+' for _ in range(self.x)]] * self.y
        return None

    def fill_matrix(self, ):
        pass

    def print_matrix(self):
        for item in self.matrix:
            print (str(item) + "\n")


