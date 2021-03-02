import maya.cmds as cmds
import createLocators
import createIK

createLocators = reload(createLocators)
createIK = reload(createIK)

def createJointsWindow():
    
    global setPrefix
    setPrefix = "test"
    
    cmds.window("Joint Creation", h = 500, w = 200, rtf = True, title = 'JOINTS', titleBar = True)
    cmds.rowColumnLayout(nc = 1)
    cmds.image(i = "/Users/abhishekravi/Desktop/NEWMAYAWORK/Header3.png")
    cmds.separator(h = 10)
    cmds.button(l = "Create Joints", w = 100, c = "createJoints.createJoints(createLocators.returnSpineAmount(), createLocators.returnFingerAmount())")
    cmds.button(l = "Set Orientation", w = 100, c = "createJoints.setJointOrientation()")
    cmds.button(l = "Delete Joints", w = 100, c = "createJoints.deleteJoints()")
    cmds.separator(h = 10)
    cmds.button(l = "Create IK", w = 100, c = "createIK.IKHandles()")
    cmds.showWindow()
    

def createJoints(spineAmount, amount):
    
    cmds.select(deselect = True)
    
    
    if cmds.objExists('RIG'):
        print 'RIG already exists'
    else:
        jointGRP = cmds.group(em = True, name = "RIG")
        
    #Spine
    root = cmds.ls("Loc_ROOT")
    
    allSpines = cmds.ls("Loc_Spine_*", type = 'locator')
    spine = cmds.listRelatives(*allSpines, p = True, f = True)
    
    rootPos = cmds.xform(root, q = True, t = True, ws = True)
    rootJoint = cmds.joint(radius = 0.1, p = rootPos, name = "RIG_ROOT")
    
    #cmds.parent(rootJoint, w = True, a = True)
    #cmds.parent(rootJoint, 'RIG', a = True)
    
    for i, s in enumerate(spine):
        pos = cmds.xform(s, q = True, t = True, ws = True)
        j = cmds.joint(radius = 0.08, p = pos, name = "RIG_SPINE_" + str(i))
        
    createHead(spineAmount)
    createArmJoints(spineAmount)
    createFingerJoints(createLocators.returnFingerAmount())    
   
    if(cmds.objExists('Loc_L_inv_heel*')):
        createInverseFootroll()
    else:
        print ''
    
    createLegs()

def createHead(amount):
    
    cmds.select(deselect = True)
    cmds.select("RIG_SPINE_" + str(amount - 1))
    
    neckJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_Neck'), q = True, t = True, ws = True), name = "RIG_Neck")
    cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_Head'), q = True, t = True, ws = True), name = "RIG_Head")
    
    cmds.select(deselect = True)
    cmds.select("RIG_Neck")
    
    jawJointStart = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_Jaw_Start'), q = True, t = True, ws = True), name = 'RIG_Jaw_Start')
    jawJointEnd = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_Jaw_End'), q = True, t = True, ws = True), name = 'RIG_Jaw_End')   
   
   
def createArmJoints(amount):
    
    cmds.select(deselect = True)
    cmds.select("RIG_SPINE_" + str(amount - 1))
            
    L_Clavicle = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_Clavicle'), q = True, t = True, ws = True), name = "RIG_L_Clavicle")
    L_upperArmJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_upperArm'), q = True, t = True, ws = True), name = "RIG_L_upperArm")
    L_elbowJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_elbow'), q = True, t = True, ws = True), name = "RIG_L_elbow")
    
    if(cmds.objExists('Loc_L_armTwist_*')):
        L_armTwists = cmds.ls('Loc_L_armTwist_*', type = 'transform')
        #print L_armTwists
        
        for i, a in enumerate(L_armTwists):
            L_twistJoint = cmds.joint(radius = 0.1, p = cmds.xform(a, q = True, t = True, ws = True), name = "RIG_L_armTwist_" + str(i))
            
    else:
        print ''
        
    L_wristJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls("Loc_L_wrist"), q = True, t = True, ws = True), name = "RIG_L_wrist")
    
    cmds.select(deselect = True)
    cmds.select("RIG_SPINE_" + str(amount - 1))
    
    R_Clavicle = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_Clavicle'), q = True, t = True, ws = True), name = "RIG_R_Clavicle")
    R_upperArmJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_upperArm'), q = True, t = True, ws = True), name = "RIG_R_upperArm")
    R_elbowJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_elbow'), q = True, t = True, ws = True), name = "RIG_R_elbow")
    
    if(cmds.objExists('Loc_R_armTwist_*')):
        R_armTwists = cmds.ls('Loc_R_armTwist_*', type = 'transform')
        #print R_armTwists
        
        for i, a in enumerate(R_armTwists):
            R_twistJoint = cmds.joint(radius = 0.1, p = cmds.xform(a, q = True, t = True, ws = True), name = "RIG_R_armTwist_" + str(i))
            
    else:
        print ''
        
    R_wristJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls("Loc_R_wrist"), q = True, t = True, ws = True), name = "RIG_R_wrist")
    
def createFingerJoints(amount):

    for x in range(0, amount):
        createFingers(x)

def createFingers(i):
    
    cmds.select(deselect = True)
    cmds.select("RIG_L_wrist")
    l_allFingers = cmds.ls("Loc_L_finger_" + str(i) + "_*", type = 'transform')
    l_fingers = cmds.listRelatives(l_allFingers, p = True, s = False)
    
    for x, f in enumerate(l_allFingers):

        pos = cmds.xform(f, q = True, t = True, ws = True)
        j = cmds.joint(radius = 0.05, p = pos, name = "RIG_L_Finger_" + str(i) + "_" + str(x))
        
    cmds.select(deselect = True)
    cmds.select("RIG_R_wrist")
    r_allFingers = cmds.ls("Loc_R_finger_" + str(i) + "_*", type = 'transform')
    r_fingers = cmds.listRelatives(r_allFingers, p = True, s = False)
    
    for x, f in enumerate(r_allFingers):


        pos = cmds.xform(f, q = True, t = True, ws = True)
        j = cmds.joint(radius = 0.05, p = pos, name = "RIG_R_Finger_" + str(i) + "_" + str(x))
    
    

def createLegs():
    
    cmds.select(deselect = True)
    cmds.select('RIG_ROOT')
    
    L_upperLegJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_upperLeg', type = 'transform'), q = True, t = True, ws = True), name = "RIG_L_upperLeg")
    L_kneeJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_lowerLeg', type = 'transform'), q = True, t = True, ws = True), name = "RIG_L_lowerLeg")
    L_FootJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_Foot', type = 'transform'), q = True, t = True, ws = True), name = "RIG_L_Foot")
    L_FootBallJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_FootBall', type = 'transform'), q = True, t = True, ws = True), name = "RIG_L_FootBall")
    L_toeJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_Toes', type = 'transform'), q = True, t = True, ws = True), name = "RIG_L_Toes")
    
    cmds.select(deselect = True)
    cmds.select('RIG_ROOT')
    
    R_upperLegJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_upperLeg', type = 'transform'), q = True, t = True, ws = True), name = "RIG_R_upperLeg")
    R_kneeJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_lowerLeg', type = 'transform'), q = True, t = True, ws = True), name = "RIG_R_lowerLeg")
    R_FootJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_Foot', type = 'transform'), q = True, t = True, ws = True), name = "RIG_R_Foot")
    R_FootBallJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_FootBall', type = 'transform'), q = True, t = True, ws = True), name = "RIG_R_FootBall")
    R_toeJoint = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_Toes', type = 'transform'), q = True, t = True, ws = True), name = "RIG_R_Toes")
    
    
def createInverseFootroll():
    
    cmds.select(deselect = True)
    
    L_heel = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_inv_heel', type = 'transform'), q = True, t = True, ws = True), name = "RIG_L_inv_heel")
    L_toes = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_inv_toes', type = 'transform'), q = True, t = True, ws = True), name = "RIG_L_inv_toes")
    L_ball = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_inv_ball', type = 'transform'), q = True, t = True, ws = True), name = "RIG_L_inv_ball")
    L_ankle = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_L_inv_ankle', type = 'transform'), q = True, t = True, ws = True), name = "RIG_L_inv_ankle")
    
    cmds.select(deselect = True)
    
    R_heel = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_inv_heel', type = 'transform'), q = True, t = True, ws = True), name = "RIG_R_inv_heel")
    R_toes = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_inv_toes', type = 'transform'), q = True, t = True, ws = True), name = "RIG_R_inv_toes")
    R_ball = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_inv_ball', type = 'transform'), q = True, t = True, ws = True), name = "RIG_R_inv_ball")
    R_ankle = cmds.joint(radius = 0.1, p = cmds.xform(cmds.ls('Loc_R_inv_ankle', type = 'transform'), q = True, t = True, ws = True), name = "RIG_R_inv_ankle")
    
    
def deleteJoints():
    
    cmds.select(deselect = True)
    cmds.delete(cmds.ls('RIG*'))
    
    
def setJointOrientation():
    cmds.select('RIG_ROOT')
    cmds.joint(e = True, ch = True, oj = 'xyz', sao = 'xup')