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

    def __init__(self, p=0.7):

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
                comb =  combination of n and x
        """
        self.n = n

        n_factorial = math.factorial(n)
        x_factorial = math.factorial(x)
        diff = n - x
        diff_factorial = math.factorial(diff)

        comb = n_factorial / (diff_factorial * x_factorial)

        self.comb = comb
        return comb

    def calculate_probability(self, x):
        """
            Function to calculate the possibility of an outcome 

            Args:
                n = number of trials
                p = probability of success
                q = probability of failure
                x (float) = number of success

            Returns:
                prob_of_x (float) = probability of x 

            Scenario:
                If a basketball player takes 8 independent free throws, with
                a probability of 0.7 of getting a basket on each shot, what
                is the probability that she gets exactly 6 baskets?
        """

        p = self.p
        q = 1 - p
        n = self.n
        self.x = x

        # TODO: calculate the probability of x. Store
        #       the result in the self probability of x attribute. Return the value
        #       of the probability.

        comb = self.combination(n, x)
        p_squared = (p)**2
        q_squared = (q)**2

        prob_of_x = (comb * p_squared * q_squared)
