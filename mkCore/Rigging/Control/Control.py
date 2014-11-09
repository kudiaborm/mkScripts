__author__ = 'Marley Kudiabor'

import pymel.core.nodetypes
import pymel.core as pm

class Control():

    Circle = 0
    Sphere = 1
    Cube = 2
    Square = 3
    Handle = 4
    Arrow = 5
    MoveAll = 6

    def __init__(self, *args, **kwargs):
        self._isJointControl = kwargs.pop("jointControl", False) | kwargs.pop("jc", False)
        self._style = kwargs.pop

        self._translateLocked = kwargs.pop("translate", True) | kwargs.pop("t", True)
        self._rotateLocked = kwargs.pop("rotate", True) | kwargs.pop("r", True)
        self._scaleLocked = kwargs.pop("scale", True) | kwargs.pop("s", True)
        self.name = kwargs.pop("name", True) | kwargs.pop("n", True)

        self.parent = None

        if args:
            if type(args[0].getShape()) == pymel.core.nodetypes.NurbsCurve:
                self.node = args[0]
            else:
                if self._isJointControl:
                    pm.select(cl=True)
                    self.node = pm.joint(n=self.name)
                    self.node.drawStyle.set(2)
                else:
                    self.node = pm.group(em=True, n=self.name)



    def setStyle(self, style):

        self._deleteShape()
        #Circle
        if style == Control.Circle:
            tempA = pm.circle(nr=[1, 0, 0], sw=360, r=5, d=3, ch=False)[0]
            tempB = pm.circle(nr=[0, 1, 0], sw=360, r=5, d=3, ch=False)[0]
            tempC = pm.circle(nr=[0, 0, 1], sw=360, r=5, d=3, ch=False)[0]

            pm.parent([tempA.getShape(), tempB.getShape(), tempC.getShape()], self.node, r=True, s=True)
            pm.delete([tempA, tempB, tempC])
        #Sphere
        if style == Control.Sphere:
            tempA = pm.mel.eval("curve -d 1 -p 0 1 0 -p -9.20942e-09 0.951057 0.309017 -p -1.75174e-08 0.809017 0.587785 -p -2.41106e-08 0.587785 0.809017 -p -2.83437e-08 0.309017 0.951057 -p -2.98023e-08 0 1 -p -2.83437e-08 -0.309017 0.951057 -p -2.41106e-08 -0.587785 0.809017 -p -1.75174e-08 -0.809017 0.587785 -p -9.20942e-09 -0.951057 0.309017 -p 0 -1 0 -p 0 -0.951057 -0.309017 -p 0 -0.809017 -0.587786 -p 0 -0.587785 -0.809017 -p 0 -0.309017 -0.951057 -p 0 0 -1 -p 0 0.309017 -0.951057 -p 0 0.587785 -0.809017 -p 0 0.809017 -0.587786 -p 0 0.951057 -0.309017 -p 0 1 0 -p 0.309017 0.951057 0 -p 0.587785 0.809017 0 -p 0.809017 0.587785 0 -p 0.951057 0.309017 0 -p 1 0 0 -p 0.951057 0 -0.309017 -p 0.809018 0 -0.587786 -p 0.587786 0 -0.809017 -p 0.309017 0 -0.951057 -p 0 0 -1 -p -0.309017 0 -0.951057 -p -0.587785 0 -0.809017 -p -0.809017 0 -0.587785 -p -0.951057 0 -0.309017 -p -1 0 0 -p -0.951057 0 0.309017 -p -0.809017 0 0.587785 -p -0.587785 0 0.809017 -p -0.309017 0 0.951057 -p -2.98023e-08 0 1 -p 0.309017 0 0.951057 -p 0.587785 0 0.809017 -p 0.809017 0 0.587785 -p 0.951057 0 0.309017 -p 1 0 0 -p 0.951057 -0.309017 0 -p 0.809017 -0.587785 0 -p 0.587785 -0.809017 0 -p 0.309017 -0.951057 0 -p 0 -1 0 -p -0.309017 -0.951057 0 -p -0.587785 -0.809017 0 -p -0.809017 -0.587785 0 -p -0.951057 -0.309017 0 -p -1 0 0 -p -0.951057 0.309017 0 -p -0.809017 0.587785 0 -p -0.587785 0.809017 0 -p -0.309017 0.951057 0 -p 0 1 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 ;")
            pm.parent([tempA.getShape()], self.node)
            pm.delete(tempA)

        #Cube
        if style == Control.Cube:
            tempA = pm.mel.eval("curve -d 1 -ch 0 -p -5 5 5 -p 5 5 5 -p 5 -5 5 -p -5 -5 5 -p -5 5 5 -p -5 5 -5 -p 5 5 -5 -p 5 -5 -5 -p -5 -5 -5 -p -5 5 -5 -p -5 5 5 -p -5 -5 5 -p -5 -5 -5 -p 5 -5 -5 -p 5 -5 5 -p 5 5 5 -p 5 5 -5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;")
            pm.parent([tempA.getShape()], self.node)
            pm.delete(tempA)
        #Square
        if style == Control.Square:
            tempA = pm.circle(nr=[1, 0, 0], sw=360, r=5, d=3, ch=False)[0]
            tempB = pm.circle(nr=[0, 1, 0], sw=360, r=5, d=3, ch=False)[0]
            tempC = pm.circle(nr=[0, 0, 1], sw=360, r=5, d=3, ch=False)[0]
            tempD = pm.mel.eval("curve -d 1 -ch 0 -p 0 0 0 -p 0 15 0 -k 0 -k 1 ;")
            pm.parent([tempA.getShape(), tempB.getShape(), tempC.getShape(), tempD.getShape()], self.node, r=True, s=True)
            pm.delete([tempA, tempB, tempC, tempD])

        #Handle
        if style == Control.Handle:
            tempA = pm.mel.eval("curve -d 1 -ch 0 -p 0 0 0 -p 0 15 0 -k 0 -k 1 ;")
            pm.parent(tempA.getShape(), self.node)
            pm.delete(tempA)

    @classmethod
    def combineGeo(cls):
        pass

    def addAttr(self, name):
        if type(name) != list:
            pass
        pass

    def _deleteShape(self):
        pm.delete(self.node.getShapes())