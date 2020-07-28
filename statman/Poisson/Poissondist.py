import math
from ..Generaldistribution import statman


class Poisson(statman):
    """
        Poisson distribution class for calculating and
        visualizing a Poisson distribution
    """

    def __init__(self, mu=0.6):

        statman.__init__(self, mu)

        # constant
        self.e = 2.718282

    def calculate_mean(self):
        """
            Function to calculate the mean of the data set.

            Args:
                None

            Returns:
                Float: mean of the data set.
        """

        avg = 1.0 * sum(self.data) / len(self.data)

        self.mean = avg

        return mean

    def calculate_probability(self, u, x):
        """
            Function to calculate the poisson probability of an occurance

            Args:
                e, 
                u = mean of the dataset
                x = expected occurance in a time frame

            Returns:
                float: probability of the occurance of x

        """

        x_factorial = math.factorial(self.x)
        e_negativeu = self.e ^ -u

        possion_prob = e_negativeu * u ^ x / x_factorial

        return
