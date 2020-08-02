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
            mean (float) - mean value of the distribution
            n (int) - number of independent trials
            p (float) - probability of success
            q (float) - probability of failure
            x (int) - number of successful outcomes
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
                n = number of independent trials
                p = probability of success
                q = probability of failure

            Args:
                x (float) = number of positive outcomes

            Returns:
                prob_of_x (float) = probability of x 

            Scenario:
                If a basketball player takes 8 independent free throws, with
                a probability of 0.7 of getting a basket on each shot, what
                is the probability that she gets exactly 6 baskets?
        """

        p = self.p
        q = 1.0 - p
        n = self.n
        self.x = x

        comb = self.combination(n, x)
        p_squared = (p)**2
        q_squared = (q)**2

        prob_of_x = (comb * p_squared * q_squared)

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args: 
            None

        Returns: 
            float: standard deviation of the data set

        """

        q = 1.0 - self.p
        stdev = math.sqrt(self.n * self.p * (q))

        self.stdev = stdev
        return stdev

    def pdf(self):
        """
            Probability density function calculator for the bernoulli distribution.

            Args:
                None

            Returns:
                float: probability density function output 
        """

        pdf = (1.0 / (self.stdev * math.sqrt(2*math.pi))) * \
            math.exp(-0.5*((self.x - self.mean) / self.stdev) ** 2)
        return pdf

    def plot_bar(self):
        """
            Function to output a histogram of the bernoulli instance variable data using 
            seaborn library.

            Args:
                None

            Returns:
                seaborn distplot for the bernoulli distribution
        """
        s = seed(42)

        data_bern = bernoulli.rvs(size=seed, p=self.p)

        ax = sns.distplot(data_bern, kde=False, color='green',
                          hist_kws={"linewidth": 15, "alpha": 1})
        plot = ax.set(xlabel="Instances", ylabel="Frequency")

        self.plot = plot
        return plot

    def __repr__(self):
        """
            Function to output characteristics of the bernoulli instance

            Args:
                None

            Returns:
                string: characteristics of the Bernoulli
        """

        mean = self.mean
        stdev = self.stdev
        n = self.n
        p = self.p
        q = 1 - p
        x = self.x

        return ("Mean: %s \n Standard Deviation: %s \n n(number of independent trials): %s \n p(probability of success): %s \n q(probability of failure): %s \n x(number of successful outcomes): %s" % (mean, stdev, n, p, q, x))
