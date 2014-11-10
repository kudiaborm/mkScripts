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
        self.name = kwargs.pop("name", "Control")
        self.name = kwargs.pop("n", self.name)

        self.parent = None

        if type(args[0]) == int:
            self.node = pm.group(em=True, n=self.name)
            self.setStyle(args[0])

        # Wrap an existing node
        elif type(args[0]) == pm.nt.Transform:
            if type(args[0].getShape()) == pymel.core.nodetypes.NurbsCurve:
                self.node = args[0]
            else:
                if self._isJointControl:
                    pm.select(cl=True)
                    self.node = pm.joint(n=self.name)
                    self.node.drawStyle.set(2)
                else:
                    self.node = pm.group(em=True, n=self.name)

        else:
            pm.displayError("Invalid argument: {0}".format(args[0]))

    def setStyle(self, style):

        self._deleteShape()
        #Circle
        if style == Control.Circle:
            tempA = pm.circle(nr=[1, 0, 0], sw=360, r=5, d=3, ch=False)[0]
            pm.parent([tempA.getShape()], self.node, r=True, s=True)
            pm.delete([tempA])

        #Sphere
        if style == Control.Sphere:
            tempA = pm.mel.eval("curve -d 1 -p 0 5 0 -p 1.545085 4.755283 0 -p 2.938926 4.045085 0 -p 4.045085 2.938926 0 -p 4.755283 1.545085 0 -p 5 0 0 -p 4.755283 -1.545085 0 -p 4.045085 -2.938926 0 -p 2.938926 -4.045085 0 -p 1.545085 -4.755283 0 -p 0 -5 0 -p -1.545085 -4.755283 0 -p -2.938927 -4.045085 0 -p -4.045086 -2.938926 0 -p -4.755284 -1.545085 0 -p -5.000001 0 0 -p -4.755284 1.545085 0 -p -4.045086 2.938926 0 -p -2.938927 4.045085 0 -p -1.545085 4.755283 0 -p 0 5 0 -p -4.60471e-08 4.755283 1.545085 -p -8.75868e-08 4.045085 2.938926 -p -1.20553e-07 2.938926 4.045085 -p -1.41718e-07 1.545085 4.755283 -p -1.49012e-07 0 5 -p -1.545085 0 4.755283 -p -2.938927 0 4.045085 -p -4.045086 0 2.938927 -p -4.755284 0 1.545085 -p -5.000001 0 0 -p -4.755284 0 -1.545085 -p -4.045086 0 -2.938927 -p -2.938927 0 -4.045086 -p -1.545086 0 -4.755285 -p 0 0 -5.000002 -p 1.545086 0 -4.755285 -p 2.938928 0 -4.045087 -p 4.045088 0 -2.938928 -p 4.755286 0 -1.545086 -p 5 0 0 -p 4.755283 0 1.545085 -p 4.045085 0 2.938926 -p 2.938926 0 4.045085 -p 1.545085 0 4.755283 -p -1.49012e-07 0 5 -p -1.41718e-07 -1.545085 4.755283 -p -1.20553e-07 -2.938926 4.045085 -p -8.75868e-08 -4.045085 2.938926 -p -4.60471e-08 -4.755283 1.545085 -p 0 -5 0 -p 0 -4.755283 -1.545086 -p 0 -4.045085 -2.938928 -p 0 -2.938926 -4.045087 -p 0 -1.545085 -4.755285 -p 0 0 -5.000002 -p 0 1.545085 -4.755285 -p 0 2.938926 -4.045087 -p 0 4.045085 -2.938928 -p 0 4.755283 -1.545086 -p 0 5 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 ;")
            pm.parent([pm.nt.Transform(tempA).getShape()], self.node, r=True, s=True)
            pm.delete(tempA)

        #Cube
        if style == Control.Cube:
            tempA = pm.mel.eval("curve -d 1 -p -5 5 5 -p 5 5 5 -p 5 -5 5 -p -5 -5 5 -p -5 5 5 -p -5 5 -5 -p 5 5 -5 -p 5 -5 -5 -p -5 -5 -5 -p -5 5 -5 -p -5 5 5 -p -5 -5 5 -p -5 -5 -5 -p 5 -5 -5 -p 5 -5 5 -p 5 5 5 -p 5 5 -5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;")
            pm.parent([pm.nt.Transform(tempA).getShape()], self.node, r=True, s=True)
            pm.delete(tempA)

        #Square
        if style == Control.Square:
            tempA = pm.mel.eval("curve -d 1 -ch 0 -p 0 0 0 -p 0 15 0 -k 0 -k 1 ;")
            pm.parent([pm.nt.Transform(tempA).getShape()], self.node, r=True, s=True)
            pm.delete([tempA])

        #Handle
        if style == Control.Handle:
            tempA = pm.mel.eval("curve -d 1 -p 0 15 0 -p 1.545085 15.244717 0 -p 2.938926 15.954915 0 -p 4.045085 17.061074 0 -p 4.755283 18.454915 0 -p 5 20 0 -p 4.755283 21.545085 0 -p 4.045085 22.938926 0 -p 2.938926 24.045085 0 -p 1.545085 24.755283 0 -p 0 25 0 -p -1.545085 24.755283 0 -p -2.938927 24.045085 0 -p -4.045086 22.938926 0 -p -4.755284 21.545085 0 -p -5.000001 20 0 -p -4.755284 18.454915 0 -p -4.045086 17.061074 0 -p -2.938927 15.954915 0 -p -1.545085 15.244717 0 -p 0 15 0 -p -4.60471e-08 15.244717 1.545085 -p -8.75868e-08 15.954915 2.938926 -p -1.20553e-07 17.061074 4.045085 -p -1.41718e-07 18.454915 4.755283 -p -1.49012e-07 20 5 -p 1.545085 20 4.755283 -p 2.938926 20 4.045085 -p 4.045085 20 2.938926 -p 4.755283 20 1.545085 -p 5 20 0 -p 4.755286 20 -1.545086 -p 4.045088 20 -2.938928 -p 2.938928 20 -4.045087 -p 1.545086 20 -4.755285 -p 0 20 -5.000002 -p -1.545086 20 -4.755285 -p -2.938927 20 -4.045086 -p -4.045086 20 -2.938927 -p -4.755284 20 -1.545085 -p -5.000001 20 0 -p -4.755284 20 1.545085 -p -4.045086 20 2.938927 -p -2.938927 20 4.045085 -p -1.545085 20 4.755283 -p -1.49012e-07 20 5 -p -1.41718e-07 21.545085 4.755283 -p -1.20553e-07 22.938926 4.045085 -p -8.75868e-08 24.045085 2.938926 -p -4.60471e-08 24.755283 1.545085 -p 0 25 0 -p 0 24.755283 -1.545086 -p 0 24.045085 -2.938928 -p 0 22.938926 -4.045087 -p 0 21.545085 -4.755285 -p 0 20 -5.000002 -p 0 18.454915 -4.755285 -p 0 17.061074 -4.045087 -p 0 15.954915 -2.938928 -p 0 15.244717 -1.545086 -p 0 15 0 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 ;")
            pm.parent(pm.nt.Transform(tempA).getShape(), self.node, r=True, s=True)
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