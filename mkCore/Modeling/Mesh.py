__author__ = 'Marley Kudiabor'

import pymel.core as pm

class Mesh():
    def __init__(self):
        pass

    @classmethod
    def combine(cls):
        name = pm.selected()[0].name()
        pm.polyUnite(ch=0, n=name)

    @classmethod
    def separate(cls):
        for item in pm.selected():
            objs = pm.polySeparate(item, ch=0)
            padding = len(str(len(objs))) + 1
            count = 0
            for obj in objs:
                pm.rename("{0}_{1:0{2}d}".format(item, count, padding))
                count += 1

    @classmethod
    def deleteHistory(cls):
        pm.delete(ch=True)