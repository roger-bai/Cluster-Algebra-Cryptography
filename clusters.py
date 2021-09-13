import numpy


class Cluster:
    # The mutation matrix of the cluster object.
    def __init__(self, matrix=None):
        if matrix is None:
            matrix = [[]]
        self.matrix = matrix

    # Mutation of a cluster object in a sequence of directions l.
    def mutate(self, mut_list):
        for k in mut_list:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if i == k or j == k:
                        self.matrix[i][j] = -self.matrix[i][j]
                    else:
                        self.matrix[i][j] = self.matrix[i][j] + numpy.sign(
                            self.matrix[i][k]) * max(0, self.matrix[i][k] *
                                                     self.matrix[k][j])

    # Print the exchange matrix.
    def __str__(self):
        return "{}".format(self.matrix)