"""
	This is a tool set that creates a set of rigging tools to automate and speed up workflow.
	It is most likely that you have received an older version of this script feel free to concact me 
	to request the most up to date version or other tool sets. 

	Marley Kudiabor Kudiaborm@gmail.com

    Copyright (C) 2014  Marley Kudiabor

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    How to use:

    import riggingToolkit
	reload(riggingToolkit)
	riggingToolkit.main()

"""

import pymel.core as pm
import maya.OpenMaya as om
import customSdk

#########################################################################
# Miscellaneous tools
#########################################################################

def jointChainRename(*args):

	selection = pm.ls(selection=True)
	joint_chain = pm.ls(selection[0], dag=True)
	newPrefix = newNameField.getText()
	newSuffix = newSuffixField.getText()
	for i, current_item in enumerate(joint_chain):

		if i == len(joint_chain):
			newSuffix = '_end'
		new_name = newPrefix + '_{0:02d}'.format(i) + '_' + newSuffix
		pm.rename(current_item, new_name)

def defineWorld(*args):
	global worldGroup
	global moveAllCurve
	global clusterGrp


	worldGroupName = nameField.getText() + '_world'
	clusterGrp = pm.group(n = nameField.getText() + '_clusterGrp', w = True, em = True)

	moveAllName = nameField.getText() + '_moveAll'
	worldGroup = pm.group(n = worldGroupName, em = True)

	moveAllCurve = createMoveAllCurve(moveAllName)
	pm.setAttr(moveAllCurve + '.scaleX', k = False, cb = False)
	pm.setAttr(moveAllCurve + '.scaleZ', k = False, cb = False)

	pm.connectAttr(moveAllCurve + '.scaleY', moveAllCurve + '.scaleX')
	pm.connectAttr(moveAllCurve + '.scaleY', moveAllCurve + '.scaleZ')
	pm.parent(moveAllCurve, worldGroup)
	pm.parent(clusterGrp, worldGroup)


def setWorld(*args):
	global worldGroup
	global moveAllCurve
	global clusterGrp

	sel = pm.ls(selection = True)
	if len(sel) == 3:
		worldGroup = sel[0]
		moveAllCurve = sel[1]
		clusterGrp = sel[2]

	else:
		raise Exception('Please select the World Group, Move All curve and Cluster Group')



def replaceSuffix(inputObject, newSuffix):
	jChain = pm.ls(inputObject, dag = True)
	for i, j in enumerate(jChain):
		suffixIndex = j.rfind('_')
		if i == len(jChain) - 1:
			endSuffix = 'end'
			newName = j[:suffixIndex] + '_' + endSuffix
			pm.rename(j, newName)

		else:
			newName = j[:suffixIndex] + '_' + newSuffix
			pm.rename(j, newName)


def refGeo(*args):
	world = pm.ls('*_world', dag = True)
	for x in world:
		if x == '*_geo':
			x.overrideEnabled.set(True)
			x.overrideDisplayType.set(2)


def unRefGeo(*args):
	world = pm.ls('*_world', dag = True)
	for x in world:
		if x == '*_geo':
			x.overrideEnabled.set(True)
			x.overrideDisplayType.set(0)

def hideAcc(*args):
	world = pm.ls('*_world', dag = True)
	for x in world:
		if x == '*_accessories':
			x.visibility.set(False)

def unHideAcc(*args):
	world = pm.ls('*_world', dag = True)
	for x in world:
		if x == '*_accessories':
			x.visibility.set(True)
#################################
#Change Joint and IK Scale Functions  #
################################# 
    
"""
Change Joint Scale Function
"""
def changeJointScale(newScale):
    pm.jointDisplayScale(newScale)

"""
Change IKFK Scale Function
"""
def changeIKScale(newScale):
 
    pm.ikHandleDisplayScale(newScale)
#########################################################################
# Control tools
#########################################################################

def createMoveAllCurve(newName):
	moveAllCurve = pm.curve(d = 1, p = [(0, 0, -6.314364), (1.952926, 0, -4.7925),(1.05164, 0, -4.792499),
		(1.952926, 0, -1.952926), (4.7925, 0, -1.594463), (4.7925, 0, -1.952926),
		(6.725978, 0, 0), (4.7925, 0, 1.952926), (4.7925, 0, 1.594463), (1.952926, 0, 1.952926),
		(1.261715, 0, 4.699687), (1.952926, 0, 4.7925), (0, 0, 7.08783), (-1.952926, 0, 4.7925),
		(-1.261715, 0, 4.699687), (-1.952926, 0, 1.952926), (-4.7925, 0, 1.594463), (-4.7925, 0, 1.952926),
		(-6.725978, 0, 0), (-4.7925, 0, -1.952926), (-4.7925, 0, -1.594463), (-1.952926, 0, -1.952926),
		(-1.05164, 0, -4.792499), (-1.952926, 0, -4.7925), (0, 0, -6.314364)],
		k = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24],
		n = newName)
	return moveAllCurve

def createAdvControl(newName):
	advControl = pm.curve(n = newName, d = 1, p = [( -0.12769, -0.476546, -2.848856 ),( 0.476546, -0.12769, -2.848856 ),( 0.12769, 0.476546, -2.848856 ),( -0.476546, 0.12769, -2.848856 ),( -0.12769, -0.476546, -2.848856 ),( 0, 0, -2.151144 ),( -0.476546, 0.12769, -2.848856 ),( 0.12769, 0.476546, -2.848856 ),( 0, 0, -2.151144 ),( 0.476546, -0.12769,-2.848856 ),( -0.12769, -0.476546, -2.848856 ),( 0, 0, -2.151144 ),( 0, 0, 2.151144 ),( -0.476546, 0.12769, 2.848856 ),( 0.12769, 0.476546, 2.848856 ),( 0, 0, 2.151144 ),( 0.476546, -0.12769,2.848856 ),( -0.12769, -0.476546, 2.848856 ),( 0, 0, 2.151144 ),( 0.12769, 0.476546, 2.848856 ),( -0.476546, 0.12769, 2.848856 ),( -0.12769, -0.476546, 2.848856 ),( 0.476546, -0.12769, 2.848856 ),( 0.12769, 0.476546, 2.848856)], k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

	return advControl

def createCube(cubeName):
    
    newCube = pm.curve(d = 1, p = [[0.5, -0.5, 0.5], [0.5, -0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, -0.5], [0.5, -0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, 0.5, -0.5], [0.5, 0.5, -0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5], [-0.5, 0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, -0.5, 0.5], [-0.5, 0.5, 0.5]], k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], n = cubeName)
    return newCube

def createCOG(*args):
   
    newCog = createCircle()[0]
    cvsToSelect = (newCOG.cv[::2])
    pm.select(cvsToSelect)
    pm.xform(s = [.5, .5, .5])
    return newCog

def createPointer(name = ''):
	newPointer = pm.curve(n = name, d = 1,p = [(0,0,0.5), (-0.5, 0.5, -0.5), (0.5,0.5,-0.5), (0.5,-0.5,-0.5), (-0.5,-0.5,-0.5), (-0.5,0.5,-0.5), (0,0,0.5), (0.5,0.5,-0.5), (0.5,-0.5,-0.5), (0,0,0.5), (-0.5,-0.5,-0.5)], k = [0,1,2,3,4,5,6,7,8,9,10])
	return newPointer

def createHandle(newName):
	newHandle = pm.curve(d = 1, p = [( 0,1.3769, 0),
		( 0.176983, 1.450208, 0 ),
		( 0.250291, 1.627191, 0 ),
		( 0.176983, 1.804174, 0 ),
		( 0, 1.877482, 0 ),
		( -0.176983, 1.804174, 0 ),
		( -0.250291, 1.627191, 0 ),
		( -0.176983, 1.450208, 0 ),
		( 0, 1.3769, 0 ),
		( 0, 1.450208, -0.176983 ),
		( 0, 1.627191, -0.250291 ),
		( 0, 1.804174, -0.176983 ),
		( 0, 1.877482, 0 ),
		( 0, 1.804174, 0.176983 ),
		( 0, 1.627191, 0.250291),
		( 0, 1.450208, 0.176983),
		( 0, 1.3769, 0 ),
		( 0, 0, 0)], k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]);

	pm.cmds.addAttr(ln = 'switch', keyable = True, attributeType = 'double', min = 0, max = 10)
 	return newHandle

def editControls(*args):
 	selectedCtrls = pm.ls(selection = True)
 	pm.select(cl = True)
 	for ctrl in selectedCtrls:
 		pm.select(ctrl + '.cv[*]', tgl = True)
#########################################################################
# Function tools
#########################################################################

def createPad(inputObject):

	pm.select(cl = True)

	paddingGroup = pm.group(em = True)
	upperPaddingGroup = pm.group(em = True)

	pm.parent(paddingGroup, upperPaddingGroup)
	movePivot = pm.parentConstraint(inputObject, upperPaddingGroup, mo = False)
	pm.delete(movePivot)
	pm.parent(inputObject, paddingGroup)
	pm.makeIdentity(apply = True, t = True, r = True, s = True, n = 0)

	pm.rename(paddingGroup, inputObject + '_sdkPad')
	pm.rename(upperPaddingGroup, inputObject + '_offsetPad')

	return upperPaddingGroup

def createPrime(target, inputObject):
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
	zeroTransforms(inputObject)

	return upperPrimingGrp

def zeroTransforms(objToZero):
	pm.setAttr(objToZero + '.translateX', 0)
	pm.setAttr(objToZero + '.translateY', 0)
	pm.setAttr(objToZero + '.translateZ', 0)
	pm.setAttr(objToZero + '.rotateX', 0)
	pm.setAttr(objToZero + '.rotateY', 0)
	pm.setAttr(objToZero + '.rotateZ', 0)
	pm.setAttr(objToZero + '.scaleX', 1)
	pm.setAttr(objToZero + '.scaleY', 1)
	pm.setAttr(objToZero + '.scaleZ', 1)

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


def separatorText(labelName):
    pm.text(label = labelName)
    pm.separator(height = 1, style = 'singleDash')
    pm.separator(height = 1, style = 'none')   
#########################################################################
# Joint Conversion Functions
#########################################################################

def makeFk(sel, inputRoot):

	currentChain = pm.ls(selection = True, dag = True)

	if sel == False:
		currentChain = pm.ls(inputRoot, dag = True)

	controlList = []
	primeList = []
	createPad(currentChain[0])

	for j, item in enumerate(currentChain):
		if j != len(currentChain) - 1:
			
			index = item.rfind('_')
			newName = item[:index] + '_ctrl'
			newControl = pm.circle(nr = [1,0,0], r = 1, n = newName)[0]
			newPrime = createPrime(item, newControl)
			pm.orientConstraint(newControl, item, mo = False)
			controlList.append(newControl)
			primeList.append(newPrime)

	for x, item in enumerate(primeList):
		if x != len(primeList) - 1:
			pm.parent(primeList[x + 1], controlList[x])



def makeIk(sel, inputRoot):
	currentChain = pm.ls(selection = True, dag = True)

	if sel == False:
		currentChain = pm.ls(inputRoot, dag = True)
		
	ikControlName = nameField.getText() + '_ctrl'
	ikControl = createCube(ikControlName)
	should = currentChain[0]
	elb = currentChain[1]
	wrist = currentChain[2]
	poleName = nameField.getText() + '_poleVec'

	baseNameI = should.find('_')
	baseName = should[:baseNameI] + '_stretchy'

	poleVec = createPointer(name = poleName + '_ctrl')
	polePad = createPad(poleVec)

	aimGrp = pm.group(em = True, w = True)
	aimGrpUp = pm.group(em = True)
	pm.parent(aimGrpUp, aimGrp, a = True)
	pm.move(0,1,0, aimGrpUp, r = True)

	elbGrp = pm.group(em = True, w = True)

	pm.parent(polePad, aimGrp, a = True)
	pm.move(0, 0, -5, polePad, r =  True)

	tempConstA = pm.pointConstraint(should, wrist, aimGrp, mo = False)
	tempConstB = pm.pointConstraint(elb, elbGrp, mo = False)
	tempConstC = pm.aimConstraint(elbGrp, aimGrp, mo = False, aim = [0,0,-1])
	tempConstD = pm.pointConstraint(wrist, ikControl, mo = False)

	pm.delete(tempConstA, tempConstB, tempConstC, tempConstD)
	
	createPad(currentChain[0])

	pm.parent(polePad, w = True)
	pm.delete(aimGrp, elbGrp)

	poleVecCurve = pm.curve(n = poleName + '_curve', d = 1, p = [(0,0,0), (0,0,1)], k = [0,1])
	firstCluster = True

	clusterNameA = poleName + '_cluster_00'
	clusterNameB = poleName + '_cluster_01'

	newClusterA = pm.cluster(poleVecCurve + '.cv[0]', n = clusterNameA)[1]
	newClusterB = pm.cluster(poleVecCurve + '.cv[1]', n = clusterNameB)[1]
	pm.parentConstraint(elb, newClusterA)
	pm.parentConstraint(poleVec, newClusterB)
	pm.parent(newClusterA, clusterGrp)
	pm.parent(newClusterB, clusterGrp)

	newIkHandle = pm.ikHandle(n = poleName + '_ikHandle',sj = should, ee = wrist, sol = 'ikRPsolver', shf = False, s = 0)[0]
	pm.poleVectorConstraint(poleVec, newIkHandle)
	pm.parentConstraint(ikControl, newIkHandle)

	createPad(ikControl)

	if stretchyCheckBox.getValue():
		pm.addAttr(ikControl, ln = 'elbowLock', keyable = True, attributeType = 'double', min = 0, max = 1)
		pm.addAttr(ikControl, ln = 'stretchy', keyable = True, attributeType = 'double', min = 0, max = 1)

		shoulderNull = pm.group(em = True, w = True, n = baseName + '_should_DDNull')
		elbowNull = pm.group(em = True, w = True, n = baseName + '_elbow_DDNull')
		wristNull = pm.group(em = True, w = True, n = baseName + '_wrist_DDNull')

		pm.pointConstraint(should, shoulderNull)
		elbowPointConstraint = pm.pointConstraint(elb, elbowNull)
		pm.pointConstraint(ikControl, wristNull)
		pm.delete(elbowPointConstraint)

		totalDistanceDimension = pm.createNode('distanceDimShape', n = baseName + '_DDTot')
		upperArmDistanceDimension = pm.createNode('distanceDimShape', n = baseName + '_DDUp')
		lowerArmDistanceDimension = pm.createNode('distanceDimShape', n = baseName + '_DDLow')
		totArmMD = pm.createNode('multiplyDivide', 	n = baseName + '_MDTot')
		upArmMD = pm.createNode('multiplyDivide', 	n = baseName + '_MDUp')
		lowArmMD = pm.createNode('multiplyDivide', 	n = baseName + '_MDLow')

		totArmMD.operation.set(2)
		upArmMD.operation.set(1)
		lowArmMD.operation.set(1)

		shoulderNull.translate.connect(totalDistanceDimension.startPoint)
		wristNull.translate.connect(totalDistanceDimension.endPoint)

		shoulderNull.translate.connect(upperArmDistanceDimension.startPoint)
		elbowNull.translate.connect(upperArmDistanceDimension.endPoint)

		elbowNull.translate.connect(lowerArmDistanceDimension.startPoint)
		wristNull.translate.connect(lowerArmDistanceDimension.endPoint)

		totalLength = upperArmDistanceDimension.distance.get() + lowerArmDistanceDimension.distance.get()

		totArmMD.input2X.set(totalLength)
		upArmMD.input2X.set(upperArmDistanceDimension.distance.get())
		lowArmMD.input2X.set(lowerArmDistanceDimension.distance.get())

		totalDistanceDimension.distance.connect(totArmMD.input1X)
		totArmMD.outputX.connect(upArmMD.input1X)
		totArmMD.outputX.connect(lowArmMD.input1X)

		upperArmCondition = pm.createNode('condition', n = baseName + '_UpCond')
		lowerArmCondition = pm.createNode('condition', n = baseName + '_LowCond')
		upperArmCondition.operation.set(2)
		lowerArmCondition.operation.set(2)
		upperArmBlend = pm.createNode('blendTwoAttr', n = baseName + 'upBlend')
		lowerArmBlend = pm.createNode('blendTwoAttr', n = baseName + 'lowBlend')

		ikControl.elbowLock.connect(upperArmBlend.attributesBlender)
		ikControl.elbowLock.connect(lowerArmBlend.attributesBlender)

		totalDistanceDimension.distance.connect(upperArmCondition.firstTerm)
		totalDistanceDimension.distance.connect(lowerArmCondition.firstTerm)
		upperArmCondition.secondTerm.set(totalLength)
		lowerArmCondition.secondTerm.set(totalLength)
		upArmMD.outputX.connect(upperArmCondition.colorIfTrueR)
		lowArmMD.outputX.connect(lowerArmCondition.colorIfTrueR)
		upperArmCondition.colorIfFalseR.set(upperArmDistanceDimension.distance.get())
		lowerArmCondition.colorIfFalseR.set(lowerArmDistanceDimension.distance.get())
		upperArmDistanceDimension.distance.connect(upperArmBlend.input[0])
		upperArmCondition.outColorR.connect(upperArmBlend.input[1])
		lowerArmDistanceDimension.distance.connect(lowerArmBlend.input[0])
		lowerArmCondition.outColorR.connect(lowerArmBlend.input[1])

		#finishCondition

		#create second pv
		elbowLockConstraint = pm.poleVectorConstraint(elbowNull, newIkHandle, w = 0)
		#lower keyframe
		pm.setDrivenKeyframe(elbowLockConstraint, at = elbowLockConstraint.w0, cd = ikControl.elbowLock, v = 0, dv = 0 )
		pm.setDrivenKeyframe(elbowLockConstraint, at = elbowLockConstraint.w0, cd = ikControl.elbowLock, v = 1, dv = 1 )
		pm.setDrivenKeyframe(elbowLockConstraint, at = elbowLockConstraint.w1, cd = ikControl.elbowLock, v = 1, dv = 0 )
		pm.setDrivenKeyframe(elbowLockConstraint, at = elbowLockConstraint.w1, cd = ikControl.elbowLock, v = 0, dv = 1 )
		#create full stretch togle
		upperArmBlend.output.connect(elb.translateX)
		lowerArmBlend.output.connect(wrist.translateX)

		kneeLock = pm.circle(nr = [1,0,0], n = baseName + '_kneeLock_ctrl')[0]
		kneeLockPad = createPad(kneeLock)
		tempParent = pm.parentConstraint(elb, kneeLockPad, mo = False)
		pm.delete(tempParent)
		pm.parentConstraint(kneeLock, elbowNull, mo = True)

		pm.parentConstraint(kneeLockPad, (ikControl, should))
		
def makeFkIk(*args):

	bindRoot = pm.ls(selection = True)[0]
	bindChain = pm.ls(bindRoot, dag = True)
	fkChain = pm.duplicate(bindRoot)
	replaceSuffix(fkChain, 'fk')
	makeFk(False, fkChain)
	ikChain = pm.duplicate(bindRoot)
	replaceSuffix(ikChain, 'ik')
	makeIk(False, ikChain)

	fkChainList = pm.ls(fkChain, dag = True)
	ikChainList = pm.ls(ikChain, dag = True)

	createPad(bindRoot)
	suffixIndex = bindChain[0].rfind('_')
	hanldeName = bindChain[0][:suffixIndex] + '_switch'
	handle = createHandle(hanldeName)
	pm.rename(handle, hanldeName)
	pm.parentConstraint(bindChain[-1], handle)
	constraintList = []
	for i, item in enumerate(bindChain):
		newConstraint = pm.orientConstraint(fkChainList[i], ikChainList[i], bindChain[i], mo = False)
		fkCon = pm.orientConstraint(newConstraint, q = True, wal = True)[1]
		ikCon = pm.orientConstraint(newConstraint, q = True, wal = True)[0]

		pm.setDrivenKeyframe(fkCon, cd = handle + '.switch', v = 1, dv = 10)
		pm.setDrivenKeyframe(fkCon, cd = handle + '.switch', v = 0, dv = 0)

		pm.setDrivenKeyframe(ikCon, cd = handle + '.switch', v = 0, dv = 10)
		pm.setDrivenKeyframe(ikCon, cd = handle + '.switch', v = 1, dv = 0)


def setupFootRoll(*args):
	
	global heelRFL
	global ballRFL
	global toeRFL
	global innerRFL
	global outerRFL
	global ankleRFL

	heelRFL = pm.joint(p = [0, 0, 0], n = 'xHeelRFL')
	pm.select(cl = True)
	ballRFL = pm.joint(p = [0,0,3], n = 'xBallRFL')
	pm.select(cl = True)
	toeRFL = pm.joint(p =[0, 0, 4], n = 'xToeRFL')
	pm.select(cl = True)
	innerRFL = pm.joint( p =[1, 0, 3], n = 'xInnerRFL')
	pm.select(cl = True)
	outerRFL = pm.joint( p = [ -1, 0, 3], n = 'xOuterRFL' )
	pm.select(cl = True)
	ankleRFL = pm.joint( p = [0, .5, 0], n = 'xAnkleRFL')

def acceptFootRoll(*args):
	pm.parent(ankleRFL, ballRFL)
	pm.parent(ballRFL, toeRFL)
	pm.parent(toeRFL, innerRFL)
	pm.parent(innerRFL, outerRFL)
	pm.parent(outerRFL, heelRFL)

#########################################################################
# Facial tools
#########################################################################

def conTrans(*args):
	driver = pm.ls(selection = True)[0]
	driven = pm.ls(selection = True)[1]

	pm.connectAttr( driver + '.t', driven + '.t')
def conRot(*args):
	driver = pm.ls(selection = True)[0]
	driven = pm.ls(selection = True)[1]

	pm.connectAttr( driver + '.r', driven + '.r')
def conScale(*args):
	driver = pm.ls(selection = True)[0]
	driven = pm.ls(selection = True)[1]

	pm.connectAttr( driver + '.s', driven + '.s')

def pointOnPol(*args):
	pointList = pm.ls(selection = True)
	for p in pointList:
		loc = pm.spaceLocator()
		pm.pointOnPolyConstraint(p, loc, mo = False)

#########################################################################
# UI tools
#########################################################################

def buttonIndexUpdate(buttonIndex):
	global typeIndex
	typeIndex = buttonIndex


#########################################################################
# Joint Creation
#########################################################################

def locChain(*args):
	return 0

def createJointChain(*args):

	if typeIndex == 0:
		createNormalChain()

	else:
		createRibbonSpine()

def createNormalChain(*args):
	jointChainLenStr = jointChainLenField.getText()
	jointChainLen = int(jointChainLenField.getText())
	jointChainName = nameField.getText()
	jointSuffix = suffixField.getText()
	i = 0
	firstJointInChain = True
	pm.select(d = True)
	while i <= jointChainLen:
		pm.joint(p = (i,0,0))
		jointName = jointChainName + '_{0:02d}'.format(i) + '_' + jointSuffix
		newJoint = pm.joint(e=True, zso=True, oj='xyz', sao = 'yup', n = jointName)

		if i == jointChainLen:
			newJointName = jointName.replace(jointSuffix, 'end')
			pm.rename(newJoint, newJointName)

		i = i + 1

def createRibbonSpine(*args):

	jointChainLen = int(jointChainLenField.getText())

	nurbsPlnName = nameField.getText() + '_ribbonPlane'
	nurbsPln = pm.nurbsPlane(u = 1, v = jointChainLen, lr = jointChainLen, n = nurbsPlnName, ax = [0,0,1])
	pm.rebuildSurface(nurbsPln, ch = 1, rpo = 1, end = 1, kr = 0, kc = 0, su =1, du = 1, sv = 5, dv = 3, tol = .01, dir = 0)
	pm.select(nurbsPln, r = True)

	mNurbsPln = pm.ls(selection = True)[0]

# Ribbon Spine Control Adder
def addControl(inputObject):
	newControl = pm.circle(n = str(inputObject) + '_control', c = [0,0,0], nr = [0,1,0], sw = 360, r = 1, d = 3, s = 16, ch = 1)[0]
	tempPConstr = pm.pointConstraint( inputObject, newControl)
	tempOConst = pm.orientConstraint(inputObject, newControl)
	pm.delete(tempOConst, tempPConstr)
	newControlPad = createPad(newControl)
	pm.parent(inputObject, newControl)
	return newControlPad, newControl

def averageLocators(aimLoc, animLoc, outLoc, nodeName):

	newNodeName = nodeName + '_pmaNode'
	pmaNode = pm.shadingNode( 'plusMinusAverage', au = True, n = newNodeName)
	pm.setAttr(pmaNode + '.operation', 1)

	pm.connectAttr(aimLoc + '.rotate', pmaNode + '.input3D[0]', f = True)
	pm.connectAttr(animLoc + '.rotate', pmaNode + '.input3D[1]', f = True)

	pm.connectAttr(pmaNode + '.output3D', outLoc + '.rotate')


def folliclify(*args):

	mNurbsPln = pm.ls(selection = True)[0]
	patchCount = float(jointChainLenField.getText())
	nurbsPlnName = nameField.getText() + '_ribbonPlane'
	pm.select(cl = True)
	follicleGrp = pm.group(n = str(nurbsPlnName) + '_follicleGrp')
	pm.select(cl = True)
	animLocGrp = pm.group(n = str(nurbsPlnName) + '_animLocGrp')

	createPad(mNurbsPln)

	#Ribbon spine Controls
	botCtrlTempFoll	= createFollicle(mNurbsPln, 0, 0.5)
	botCtrlJoint = pm.joint(n = str(nurbsPlnName) + '_bot_rbn_ctrlJoint', a = False)
	zeroTransforms(botCtrlJoint)
	pm.select(cl = True)
	pm.parent(botCtrlJoint, w = True)
	botControlPad, botControl = addControl(botCtrlJoint)
	
	topCtrlTempFoll = createFollicle(mNurbsPln, 1, 0.5)
	topCtrlJoint = pm.joint(n = str(nurbsPlnName) + '_top_rbn_ctrlJoint', a = False)
	zeroTransforms(topCtrlJoint)
	pm.select(cl = True)
	pm.parent(topCtrlJoint, w = True)
	topControlPad, topControl = addControl(topCtrlJoint)
	
	midCtrlTempFoll = createFollicle(mNurbsPln, 0.5, 0.5)
	midCtrlJoint = pm.joint(n = str(nurbsPlnName) + '_mid_rbn_ctrlJoint', a = True)
	zeroTransforms(midCtrlJoint)
	pm.select(cl = True)
	pm.parent(midCtrlJoint, w = True)
	midControlPad, midControl = addControl(midCtrlJoint)

	#Ribbon Spine interpolation locators
	
	locatorOffset = 3
	smallLocatorSize = .25

	midAimLoc = pm.spaceLocator(n = str(nurbsPlnName) + '_midAimLoc')
	midAnimLoc = pm.spaceLocator(n = str(nurbsPlnName) + '_midAnimLoc')
	midOutLoc = pm.spaceLocator(n = str(nurbsPlnName) + '_midOutLoc')
	midUp = pm.spaceLocator(n = str(nurbsPlnName) + '_midUp')
	pm.parent(midUp, midControl)
	pm.parent(midAnimLoc, midControl)
	pm.parent(midCtrlJoint, midOutLoc)
	pm.parent(midOutLoc, midControl)

	zeroTransforms(midUp)
	zeroTransforms(midAnimLoc)
	zeroTransforms(midOutLoc)
	pm.parent(midAnimLoc, animLocGrp)

	midAnimPar = pm.parentConstraint(midControl, midAnimLoc)

	averageLocators(midAimLoc, midAnimLoc, midOutLoc, 'mid')

	pm.setAttr(midUp + '.translateX', locatorOffset)
	pm.setAttr(midUp + '.localScaleX', smallLocatorSize)
	pm.setAttr(midUp + '.localScaleY', smallLocatorSize)
	pm.setAttr(midUp + '.localScaleZ', smallLocatorSize)

	pm.parent(midAimLoc, midControl)
	zeroTransforms(midAimLoc)

	topAimLoc = pm.spaceLocator(n = str(nurbsPlnName) + '_topAimLoc')
	topAnimLoc = pm.spaceLocator(n = str(nurbsPlnName) + '_topAnimLoc')
	topOutLoc = pm.spaceLocator(n = str(nurbsPlnName) + '_topOutLoc')
	topUp = pm.spaceLocator(n = str(nurbsPlnName) + '_topUp')
	pm.parent(topUp, topControl)
	pm.parent(topAnimLoc, topControl)
	pm.parent(topOutLoc, topControl)
	pm.parent(topCtrlJoint, topOutLoc)
	
	zeroTransforms(topUp)
	zeroTransforms(topAnimLoc)
	zeroTransforms(topOutLoc)
	pm.parent(topAnimLoc, animLocGrp)

	topAnimPar = pm.parentConstraint(topControl, topAnimLoc)

	averageLocators(topAimLoc, topAnimLoc, topOutLoc, 'top')

	pm.setAttr(topUp + '.translateX', locatorOffset)
	pm.setAttr(topUp + '.localScaleX', smallLocatorSize)
	pm.setAttr(topUp + '.localScaleY', smallLocatorSize)
	pm.setAttr(topUp + '.localScaleZ', smallLocatorSize)

	pm.parent(topAimLoc, topControl)
	zeroTransforms(topAimLoc)

	botAimLoc = pm.spaceLocator(n = str(nurbsPlnName) + '_botAimLoc')
	botAnimLoc = pm.spaceLocator(n = str(nurbsPlnName) + '_botAnimLoc')
	botOutLoc = pm.spaceLocator(n = str(nurbsPlnName) + '_botOutLoc')
	botUp = pm.spaceLocator(n = str(nurbsPlnName) + '_botUp')
	pm.parent(botUp, botControl)
	pm.parent(botAnimLoc, botControl)
	pm.parent(botCtrlJoint, botOutLoc)
	pm.parent(botOutLoc, botControl)

	zeroTransforms(botUp)
	zeroTransforms(botAnimLoc)
	zeroTransforms(botOutLoc)
	pm.parent(botAnimLoc, animLocGrp)

	botAnimPar = pm.parentConstraint(botControl, botAnimLoc)

	averageLocators(botAimLoc, botAnimLoc, botOutLoc, 'bot')

	pm.setAttr(botUp + '.translateX', locatorOffset)
	pm.setAttr(botUp + '.localScaleX', smallLocatorSize)
	pm.setAttr(botUp + '.localScaleY', smallLocatorSize)
	pm.setAttr(botUp + '.localScaleZ', smallLocatorSize)

	pm.parent(botAimLoc, botControl)
	zeroTransforms(botAimLoc)

	zeroTransforms(botCtrlJoint)
	zeroTransforms(midCtrlJoint)
	zeroTransforms(topCtrlJoint)
	
	#aim constraints
	botToTopAim = pm.aimConstraint(topAimLoc, botAimLoc, mo = False, aim = [0,1,0], u = [1,0,0], wut = 'object', wuo = botUp )
	topToBotAim = pm.aimConstraint(botAimLoc, topAimLoc, mo = False, aim = [0,-1,0], u = [1,0,0], wut = 'object', wuo = topUp )
	midToTopAim = pm.aimConstraint(topAimLoc, midAimLoc, mo = False, aim = [0,1,0], u = [1,0,0,], wut = 'object', wuo = midUp)

	midPos = pm.pointConstraint(topAimLoc, botControl, midControlPad, mo = True)

	#cleanup temp follicles
	tempFollicles = [botCtrlTempFoll, topCtrlTempFoll, midCtrlTempFoll]
	for tempFoll in tempFollicles:
		par = tempFoll.getParent()
		pm.delete(par)


	normalPlnSize = (1/patchCount)

	i = 1
	while i <= patchCount:
		mFoll = createFollicle(mNurbsPln, (i*(normalPlnSize))-(normalPlnSize/2), 0.5)
		newJoint = pm.joint(n = nurbsPlnName + '_joint_' + str(i), a = False)
		i = i + 1
		#pm.parent(newJoint, mFoll)
		pm.parent(mFoll, follicleGrp)

	follicleGrp.setAttr('visibility', 0)

	pm.skinCluster(botCtrlJoint, midCtrlJoint, topCtrlJoint, mNurbsPln, mi = 2, sw = .75, bm = 0, omi = 1, dr = 4, rui = True, )


def schleiferify(*args):

	global moveAllCurve

	advRootJoint 		= pm.ls(selection = True)[0]
	createPad(advRootJoint)
	advJointChain 		= pm.ls(advRootJoint, dag = True)
	jointPosArray 		= []
	baseName 			= nameField.getText()
	curveName 			= baseName + '_curve'
	curveInfoName	 	= curveName + '_curveInfo'

	pm.select(cl = True)


	for i,j in enumerate(advJointChain):
		currentJointPos = pm.xform( j, q = True, ws = True, t = True)
		jointPosArray.append(currentJointPos)


	schleiferCurve = pm.curve(p = jointPosArray)
	pm.rename(schleiferCurve, curveName)

	clusterList = []

	for i,cvControl in enumerate(schleiferCurve.cv):

		clusterName = baseName + '_cluster{0:02d}'.format(i)
		newCluster 	= pm.cluster(cvControl, n = clusterName)[1]
		clusterList.append(newCluster)

	curveInfoNode 		= pm.createNode( 'curveInfo', n = curveInfoName )
	curvLenMD 			= pm.createNode( 'multiplyDivide', n = curveInfoName  + '_MD')
	curvLenNorm  		= pm.createNode( 'multiplyDivide', n = curveInfoName + '_norm') 
	pm.connectAttr( curveName + '.worldSpace', curveInfoName + '.inputCurve' )
	origCurvLen 		= pm.getAttr(curveInfoNode + '.arcLength')


	curvLenMD.operation.set(2)
	curvLenNorm.operation.set(1)
	curveInfoNode.arcLength.connect(curvLenMD.input1X)
	# curvvLenMD.input2X.set(origCurvLen)
	pm.setAttr(curvLenMD + '.input2X', origCurvLen)
	curvLenMD.outputX.connect(curvLenNorm.input1X)
	moveAllCurve.scaleY.connect(curvLenNorm.input2X)

	newIkHandle = pm.ikHandle(sj = advJointChain[0], ee = advJointChain[-1], sol = 'ikSplineSolver', ccv = False, pcv = False, c = schleiferCurve)[0]

	for i,j in enumerate(advJointChain):
		if i != 0:
			originalLen = pm.getAttr(j + '.translateX')
			currJointMD = pm.createNode('multiplyDivide', n = j + '_MD')
			currJointMD.operation.set(1)
			currJointMD.input2X.set(originalLen)
			curvLenMD.outputX.connect(currJointMD.input1X)
			currJointMD.outputX.connect(j.translateX)
			moveAllCurve.scaleY.connect(j.scaleY)
			moveAllCurve.scaleY.connect(j.scaleZ)


	lastObject = 'null'
	onFirstJoint = True
	for i,j in enumerate(advJointChain):
		controlName = nameField.getText() + '_{0:02d}'.format(i) + '_ctrl'
		advControlName = nameField.getText() + '{0:02d}'.format(i) + '_adv_ctrl'
		newControl = pm.circle(nr = [1,0,0], r = 2, n = controlName)[0]
		advControl = createAdvControl(advControlName)
		advControlPad = createPad(advControl)
		pm.parent(advControlPad, newControl)
		currentCtrl = createPrime(j, newControl)
		clusToAdv = pm.parentConstraint(advControl, clusterList[i])


		if i == 0:
			botControl = newControl

		topControl = newControl
		if i != 0:
			pm.parent(currentCtrl, prevCtrl)
		prevCtrl = newControl
	pm.parent(clusterList, clusterGrp)

	#setup advanced twist

	pm.setAttr( newIkHandle + '.dTwistControlEnable', 1)
	pm.setAttr( newIkHandle + '.dWorldUpType', 4)
	pm.setAttr( newIkHandle + '.dWorldUpAxis', 4)
	pm.setAttr( newIkHandle + '.dWorldUpVectorEndZ', -1)
	pm.setAttr( newIkHandle + '.dWorldUpVectorZ', -1)
	pm.setAttr( newIkHandle + '.dWorldUpVectorY', 0)
	pm.setAttr( newIkHandle + '.dWorldUpVectorEndY', 0)

	pm.connectAttr(botControl + '.worldMatrix[0]', newIkHandle + '.dWorldUpMatrix')
	pm.connectAttr(topControl + '.worldMatrix[0]', newIkHandle + '.dWorldUpMatrixEnd')

def main(*args):

	if pm.window('riggingToolkitWindow', exists = True):
	    pm.deleteUI('riggingToolkitWindow', window = True) 
	    print 'Pre-existing window ToolKit deleted'

	if pm.dockControl('riggingToolkitDockControl', exists = True):
		pm.deleteUI('riggingToolkitDockControl', control = True)


	#Declarations
	global windowWidth
	global windowHeight
	global jointChainLenField
	global nameField
	global suffixField
	global typeIndex
	global stretchyCheckBox

	global newNameField
	global newSuffixField

	windowWidth = 325
	windowHeight = 100000
	allowedAreas = ['left', 'right']
	buttonIndex = 0
	typeIndex = 0


	childFrameWidth = windowWidth - 5

	window_object = pm.window('riggingToolkitWindow', t = 'Rigging Toolkit', width = windowWidth, height = windowHeight, sizeable = False)

	scrollFieldColumnLayout = pm.rowColumnLayout(nc = 1)
	scrollField = pm.scrollLayout(w = 350, h = 600)
	mainColumnLayout = pm.rowColumnLayout(nc = 1)
	jointFrameLayout = pm.frameLayout('jointLayout', cll = True, cl = False, width = windowWidth, l = 'Joint Layout')

	jointChainColumn = pm.rowColumnLayout(nc = 2)

	pm.text(l = 'Name', al = 'center', width = windowWidth/2)
	pm.text(l = 'Suffix', al = 'center', width = windowWidth/2)
	nameField = pm.textField()
	suffixField = pm.textField()

	pm.setParent(jointFrameLayout)
	worldColumn = pm.rowColumnLayout(nc = 2)
	pm.button(l = 'Define World', w = (windowWidth/6) * 5, c = defineWorld)
	pm.button(l = 'Set', w = windowWidth/6, c = setWorld)

	pm.setParent(jointFrameLayout)

	jointChainColumnSecondary = pm.rowColumnLayout(nc = 2)

	jointChainLenField = pm.textField(w = windowWidth/8, tx = '5')
	jointChainButton = pm.button(l = 'Create Joint Chain', c = createJointChain, w = ((windowWidth/8)*7))

	pm.setParent(jointFrameLayout)

	radioButtonRColmn = pm.rowColumnLayout(nc = 2)
	jntChnTypRadioCollection = pm.radioCollection()
	normChain = pm.radioButton(l = 'Normal', w = windowWidth/2, onc = lambda *args: buttonIndexUpdate(0))
	ribnChain = pm.radioButton(l = 'Ribbon', w = windowWidth/2, onc = lambda *args: buttonIndexUpdate(1))

	pm.setParent(mainColumnLayout)	
	jointSetupFrmLyt = pm.frameLayout('jointSetup', cll = True, cl = True, w = windowWidth, l = 'Joint Setup')
	separatorText('Spine Setup')
	spineTypeClmnLyt = pm.rowColumnLayout(nc = 2)
	pm.button(l = 'Schleifer', c = schleiferify, w = (windowWidth/2))
	pm.button(l = 'Ribbon', c = folliclify, w = windowWidth/2)

	pm.setParent(jointSetupFrmLyt)
	separatorText('Switch Setup')

	fkIkSpineClmnLyt = pm.rowColumnLayout(nc = 2)
	pm.button(l = 'Fk', c =  lambda *args: makeFk( False, pm.ls(selection = True)[0]), w = windowWidth/2)
	pm.button(l = 'Ik', c = lambda *args: makeIk( False, pm.ls(selection = True)[0]), w = windowWidth/2)
	pm.setParent(jointSetupFrmLyt)
	pm.button(l = 'Fk Ik', c = makeFkIk, w = windowWidth)
	stretchyCheckBox = pm.checkBox(l = 'Stretchy', v = 0)

	footRollSetup = pm.frameLayout('footRollSetup', cll = True, cl = True, w = windowWidth, l = 'FootRoll Setup')
	separatorText('Setup')
	footRollRowCol = pm.rowColumnLayout( nc = 2)
	pm.button(l = 'Setup', c = setupFootRoll, w = childFrameWidth * 0.7)
	pm.button(l = 'Accept', c = acceptFootRoll, w = childFrameWidth * .3)

	pm.setParent(mainColumnLayout)
	miscFrmLyt = pm.frameLayout('miscTools', cll = True, cl = True, w = windowWidth, l = 'Miscellaneous Tools')
	renameFrmLyt = pm.frameLayout('renameTool', cll = True, cl = True, w = windowWidth, l = 'Joint Tools')
	jointChainColumn = pm.rowColumnLayout(nc = 2)

	pm.text(l = 'Name', al = 'center', width = windowWidth/2)
	pm.text(l = 'Suffix', al = 'center', width = windowWidth/2)
	newNameField = pm.textField(w = windowWidth/2, pht = "Type Name Here")
	newSuffixField = pm.textField(w = windowWidth/2, pht = "Type Suffix Here")
	pm.setParent(renameFrmLyt)
	pm.button(l = 'Rename', c = jointChainRename, w = windowWidth)
	pm.button(l = 'Pad', c = createPad, w = windowWidth)
	pm.button(l = 'Select hierarchy', c = lambda *args: pm.select(hi = True), w = windowWidth)


	pm.setParent(miscFrmLyt)
	ctrlsFrmLyt = pm.frameLayout('ctrlTools', cll = True, cl = True, w = windowWidth, l = 'Control Tools')
	separatorText('Controls')
	pm.button(l = 'Edit Controls', c = editControls, w = windowWidth)
	pm.button(l = 'SDK Creator', c = lambda *args: customSdk.gui(), w = windowWidth)


	pm.setParent(miscFrmLyt)
	visualScaleFrmLyt = pm.frameLayout(label = 'Visual Scale', cll = True, cl = True)

	separatorText('Visual Scale')

	jointSize = 1.00
	ikSize = 1.00

	pm.columnLayout(columnOffset = ['left', -100], adjustableColumn = True, cal = 'left')
	jointSizeSliderObject = pm.floatSliderGrp(min = 0.001, max = 10, l = 'Joint Size', pre = 2, f = True, v = jointSize, cc = changeJointScale, dc = changeJointScale, adjustableColumn = True,)

	ikSizeSliderObject = pm.floatSliderGrp(min = 0.001, max = 10, l = 'IK Size', f = True, v = ikSize, cc = changeIKScale, dc = changeIKScale, adjustableColumn = True)

	pm.setParent(miscFrmLyt)
	facialFrame = pm.frameLayout('facialTools', cll = True, cl = True, w = windowWidth, l = 'Facial Tools')
	separatorText('Direct Connect')
	directConRowCol = pm.rowColumnLayout(nc = 3)
	pm.button(l = 'Trans', c = conTrans, w = windowWidth/3)
	pm.button(l = 'Rot', c = conRot, w = windowWidth/3)
	pm.button(l = 'Scale', c = conScale, w = windowWidth/3)

	pm.setParent(miscFrmLyt)
	geoFrame = pm.frameLayout('geometryTools', cll = True, cl = True, w = windowWidth, l = 'Geometry Tools')
	pm.text(l = 'Geometry', al = 'center', w = windowWidth)
	pm.rowColumnLayout(nc = 2)
	pm.button(l = 'Reference', c = refGeo, w = windowWidth/2)
	pm.button(l = 'Unreference', c = unRefGeo, w = windowWidth/2)
	pm.setParent(geoFrame)
	pm.text(l = 'Accessories', al = 'center', w = windowWidth)
	pm.rowColumnLayout(nc = 2)
	pm.button(l = 'Hide', c = hideAcc, w = windowWidth/2)
	pm.button(l = 'Unhide', c = unHideAcc, w = windowWidth/2)
	pm.dockControl('riggingToolkitDockControl', l = 'Rigging Toolkit', area = 'right', content = window_object, allowedArea = allowedAreas)

