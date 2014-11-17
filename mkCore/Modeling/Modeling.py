__author__ = 'Marley Kudiabor'

import pymel.core as pm

class Modeling():
    def __init__(self):
        pass

    @classmethod
    def combine(cls):
        name = pm.selected()[0].name()
        pm.polyUnite(ch=0, n=name)
        cls.deleteHistory()

    @classmethod
    def separate(cls):
        pm.undoInfo(ock=True)
        for item in pm.selected():
            objs = pm.polySeparate(item, ch=0)
            padding = len(str(len(objs))) + 1
            count = 0
            for obj in objs:
                pm.rename("{0}_{1:0{2}d}".format(item, count, padding))
                count += 1
        cls.deleteHistory()
        pm.undoInfo(cck=True)
    @classmethod
    def deleteHistory(cls):
        pm.delete(ch=True)

    @classmethod
    def toggleWireframe(cls):
        currPanel = pm.getPanel(wf=True)
        state = pm.modelEditor(currPanel, q=True, wos=True)
        pm.modelEditor(currPanel, e=True, wos=not state)

    @classmethod
    def freezeTransformations(cls):
        pm.makeIdentity(a=True)
