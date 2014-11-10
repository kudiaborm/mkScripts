__author__ = 'Marley Kudiabor'

import pymel.core as pm

class Common():
    def __init__(self):
        pass

    @classmethod
    def refGeo(cls):
        world = pm.ls('*_world', dag = True)
        for x in world:
            if x == '*_geo':
                x.overrideEnabled.set(True)
                x.overrideDisplayType.set(2)

    @classmethod
    def unRefGeo(cls):
        world = pm.ls('*_world', dag = True)
        for x in world:
            if x == '*_geo':
                x.overrideEnabled.set(True)
                x.overrideDisplayType.set(0)

    @classmethod
    def hideAcc(cls):
        world = pm.ls('*_world', dag = True)
        for x in world:
            if x == '*_accessories':
                x.visibility.set(False)

    @classmethod
    def unHideAcc(cls):
        world = pm.ls('*_world', dag = True)
        for x in world:
            if x == '*_accessories':
                x.visibility.set(True)

    @classmethod
    def changeJointScale(cls, newScale):
        pm.jointDisplayScale(newScale)

    @classmethod
    def changeIKScale(cls, newScale):
        pm.ikHandleDisplayScale(newScale)

    @classmethod
    def createPad(cls, *args):

        if args:
            inputObject = args[0]
        else:
            inputObject = pm.selected()

        if type(inputObject) != list:
            inputObject = [inputObject]
        pads = []
        for obj in inputObject:
            pm.select(cl = True)

            paddingGroup = pm.group(em = True)
            upperPaddingGroup = pm.group(em = True)

            pm.parent(paddingGroup, upperPaddingGroup)
            movePivot = pm.parentConstraint(obj, upperPaddingGroup, mo = False)
            pm.delete(movePivot)
            pm.parent(obj, paddingGroup)
            pm.makeIdentity(apply = True, t = True, r = True, s = True, n = 0)

            pm.rename(paddingGroup, obj + '_sdkPad')
            pm.rename(upperPaddingGroup, obj + '_offsetPad')

            pads.append(upperPaddingGroup)
        return pads



    @classmethod
    def createPrime(cls, target, inputObject):
        groupName = inputObject
        upperPrimingGrpName = groupName + '_offsetPrime'
        lowerPrimingGrpName = groupName + '_sdkPrime'

        lowerPrimingGrp = pm.group(em = True, n = lowerPrimingGrpName)
        upperPrimingGrp = pm.group(em = True, n = upperPrimingGrpName)

        pm.parent(lowerPrimingGrp, upperPrimingGrp)

        tempOri = pm.orientConstraint(target, upperPrimingGrp, mo = False)
        tempPos = pm.pointConstraint(target, upperPrimingGrp, mo = False)

        pm.delete(tempOri, tempPos)

        pm.parent(inputObject, lowerPrimingGrp)
        cls.zeroTransforms(inputObject)
        return upperPrimingGrp

    @classmethod
    def zeroTransforms(cls, *args):

        if args:
            objToZero = args[0]

        else:
            objToZero = pm.selected()

        if type(objToZero) == list:
            for obj in objToZero:
                cls.zeroTransforms(obj)
            return None
        pm.setAttr(objToZero + '.translateX', 0)
        pm.setAttr(objToZero + '.translateY', 0)
        pm.setAttr(objToZero + '.translateZ', 0)
        pm.setAttr(objToZero + '.rotateX', 0)
        pm.setAttr(objToZero + '.rotateY', 0)
        pm.setAttr(objToZero + '.rotateZ', 0)
        pm.setAttr(objToZero + '.scaleX', 1)
        pm.setAttr(objToZero + '.scaleY', 1)
        pm.setAttr(objToZero + '.scaleZ', 1)

    @classmethod
    def createFollicle(mNurbs, vPos, uPos):

        fName = '_'.join(('follicle','#'.zfill(2)))

        nFoll = pm.createNode('follicle', name=fName)
        mNurbs.local.connect(nFoll.inputSurface)

        mNurbs.worldMatrix[0].connect(nFoll.inputWorldMatrix)
        nFoll.outRotate.connect(nFoll.getParent().rotate)
        nFoll.outTranslate.connect(nFoll.getParent().translate)
        nFoll.parameterU.set(uPos)
        nFoll.parameterV.set(vPos)
        nFoll.getParent().t.lock()
        nFoll.getParent().r.lock()

        return nFoll