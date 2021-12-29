from utils.chemin import *

def test_pluscourtchemin():
    assert pluscourtchemin([(5,6),(3,2),(8,7),(6,9),(0,0)]) == [(6, 9), (8, 7), (3, 2), (0, 0), (5, 6)]
    assert pluscourtchemin([(20,13),(21,4),(45,9),(20,28),(8,7)]) == [(21, 4), (8, 7), (20, 28), (45, 9), (20, 13)]