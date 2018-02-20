
class Matrix():
    def __init__(self,x,y):
        self._x = x
        self._y = y
    """
    SETTERS AND GETTERS FOR PROPERTIES
    """
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,x_size):
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

    def createMatrix(self):
        pass

    def fillMatrix(self):
        pass

    def printMatrix(self):
        pass


