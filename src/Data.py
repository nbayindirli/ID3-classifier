from collections import namedtuple
import sys

FeatureVal = namedtuple("FeatureVal", "feature, value")        

class MushroomData:
    def __init__(self, fileName):
        self.data = []
        self.features = set()
        for line in open(fileName):
            line = line.strip()            
            attributes = line.split(',')
            for i in range(1,len(attributes)):
                self.features.add(FeatureVal(i, attributes[i]))
            self.data.append(attributes)
