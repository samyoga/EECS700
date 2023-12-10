# -*- coding: utf-8 -*-

from collections import namedtuple
from enum import Enum


class Dataset(Enum):
    ADULT = 'adult'
    CAHOUSING = 'cahousing'
    ITALIA = 'italia'
    MGM = 'mgm'

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return str(other) == self.value


class AnonMethod(Enum):

    #Optimal Lattice Anonymization
    OLA = 'ola'

    # Cluster-based
    CLUSTER = 'cluster'

    # Datafly
    DATAFLY = 'datafly'

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return str(other) == self.value

class ClassifierModel(Enum):
    RF = 'rf'
    KNN = 'knn'

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return str(other) == self.value