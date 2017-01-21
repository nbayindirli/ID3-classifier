from collections import namedtuple
import sys
import math
from Data import *

DtNode = namedtuple("DtNode", "fVal, nPosNeg, gain, left, right")

POS_CLASS = 'e'

def InformationGain(data, f):
    #TODO: compute information gain of this dataset after splitting on feature F
    return 0

def Classify(tree, instance):
    if tree.left == None and tree.right == None:
        return tree.nPosNeg[0] > tree.nPosNeg[1]
    elif instance[tree.fVal.feature] == tree.fVal.value:
        return Classify(tree.left, instance)
    else:
        return Classify(tree.right, instance)

def Accuracy(tree, data):
    nCorrect = 0
    for d in data:
        if Classify(tree, d) == (d[0] == POS_CLASS):
            nCorrect += 1
    return float(nCorrect) / len(data)

def PrintTree(node, prefix=''):
    print("%s>%s\t%s\t%s" % (prefix, node.fVal, node.nPosNeg, node.gain))
    if node.left != None:
        PrintTree(node.left, prefix + '-')
    if node.right != None:
        PrintTree(node.right, prefix + '-')        
        
def ID3(data, features, MIN_GAIN=0.1):
    #TODO: implement decision tree learning
    return DtNode(FeatureVal(1,'x'), (100,0), 0, None, None)

if __name__ == "__main__":
    train = MushroomData(sys.argv[1])
    dev = MushroomData(sys.argv[2])

    dTree = ID3(train.data, train.features, MIN_GAIN=float(sys.argv[3]))
    
    PrintTree(dTree)

    print Accuracy(dTree, dev.data)
