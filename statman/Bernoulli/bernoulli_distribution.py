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
