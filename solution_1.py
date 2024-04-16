class Circle:
    '''
    Class represents circles and allows calculating their areas.
    Attributes:
        all_circles (list): List of all created circles.
        PI (float): Approximate value of the mathematical constant.
    '''

    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1):
        '''
        Initializes a Circle object with the specified radius.

        :param radius: The radius of the circle.
        '''

        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        '''
        Calculates the area of the circle.

        :return: The area of the circle.
        '''

        return Circle.pi * (self.radius) ** 2

    @staticmethod
    def total_area():
        '''
        Calculates and prints the total area of all circles.
        '''

        summ = 0
        for cir in Circle.all_circles:
            summ += cir.area()
        
        return summ

    def __repr__(self):
        '''
        Return formal string representation of an object (for developers).
        '''
        return f'{self.radius}'
