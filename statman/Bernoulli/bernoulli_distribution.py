import math
from scipy.stats import bernoulli
from random import seed
from ..Generaldistribution import statman


# import and setup seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize': (5, 5)})


class Bernoulli(statman):
    """
        Bernoulli distribution class for calculating and 
        visualizing a Bernoulli distribution

        Attributes:
            Coming Soon...
    """

    def __init__(self, p=0.3):

        statman.__init__(self)

        self.p = p

    def calculate_mean(self):
        """
            Function to get the mean of the data set.

            Args: 
                None

            Returns:
                float: the mean value

        """

        p = self.p

        mean, variance, skew, kurt = bernoulli.stats(p, moments='mvsk')

        self.mean = mean

        return mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args: 
            None

        Returns: 
            float: standard deviation of the data set

        """

        # TODO: calculate the standard deviation of the Bernoulli distribution. Store
        #       the result in the self standard deviation attribute. Return the value
        #       of the standard deviation.

    def combination(self, n, x):
        """
            Function to perform the mathematical combination operation

            Args:
                n = number of independent trials
                x = number of successful outcomes

            Returns:
                c =  combination of n and x
        """

        n_factorial = math.factorial(n)
        x_factorial = math.factorial(x)
        diff = n - x
        diff_factorial = math.factorial(diff)

        c = n_factorial / diff_factorial * x_factorial

        self.c = c
        return c

    def calculate_probability(self):
        """
            Function to calculate the possibility of an outcome 

            Args:
                n = number of trials
                p = probability of success
                q = probability of failure

            Returns:
                x (float) = number of success


        """

        # TODO: calculate the probability of x. Store
        #       the result in the self probability of x attribute. Return the value
        #       of the probability.
