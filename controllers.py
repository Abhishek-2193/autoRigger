import maya.cmds as cmds

def createControllers(spineCount, fingerCount):

    createMaster()
    createPelvis()
    createWrists()
    createFeet()
    createSpines(spineCount)
    createClavicles(spineCount)
    createNeck(spineCount)
    createHead()
    createFingers(fingerCount)
    setColors()

def createMaster():

    master_ctrl = cmds.circle(nr = (0,1,0), c = (0,0,0), radius = 1, degree = 1, s = 16, name = "MASTER_CONTROLLER")
    cmds.move(0, -0.5, 0, master_ctrl)
    cmds.scale(2, 2, 2, master_ctrl)
    cmds.makeIdentity(master_ctrl, apply = True, t = 1, r = 1, s = 1)

def createPelvis():

    pelvis_ctrl = cmds.circle(nr = (0,1,0), c = (0,0,0), radius = 1, degree = 1, s = 8, name = "CTRL_PELVIS")
    rootPos = cmds.xform(cmds.ls("RIG_ROOT", type = 'joint'), q = True, t = True, ws = True)
    cmds.move(rootPos[0], rootPos[1], rootPos[2], pelvis_ctrl)
    cmds.scale(0.5, 0.5, 0.5, pelvis_ctrl)
    cmds.makeIdentity(pelvis_ctrl, apply = True, t = 1, r = 1, s = 1)
    cmds.parent(pelvis_ctrl, "MASTER_CONTROLLER")

def createWrists():

    sides = ['L', 'R']
    
    for side in sides:
    
        ctrl1 = cmds.circle(nr = (0,1,0), c = (0,0,0), radius = 1, degree = 1, s = 16, name = "CTRL_"+side+ "_wrist0")
        ctrl2 = cmds.circle(nr = (0,1,0), c = (0,0,0), radius = 1, degree = 1, s = 16, name = "CTRL_"+side+ "_wrist1")
        ctrl3 = cmds.circle(nr = (0,1,0), c = (0,0,0), radius = 1, degree = 1, s = 16, name = "CTRL_"+side+ "_wrist2")
        
        wrist_ctrl = cmds.group(em = True, name ="CTRL_"+side+"_Wrist")
        curves = [ctrl1, ctrl2, ctrl3]
        
        for cv in curves:
            crvShape = cmds.listRelatives(cv, shapes = True)
            cmds.parent(crvShape, wrist_ctrl, s = True, r = True)
            cmds.delete(cv)
            
        cmds.select("CTRL_"+side+"_Wrist")
        cmds.addAttr(shortName = "PV", longName = "Elbow_PV", attributeType = 'double', defaultValue = 0, minValue = -100, maxValue = 100, keyable = True)
        cmds.scale(0.07, 0.07, 0.07, wrist_ctrl)
        
        wristPos = cmds.xform(cmds.ls("RIG_" + side + "_wrist"), q = True, t = True, ws = True)
        #wristRot = cmds.joint(cmds.ls("RIG_" + side + "_wrist"), q = True, o = True)
        
        if cmds.objExists("RIG_L_armTwist_*"):
            armTwists = cmds.ls("RIG_L_armTwist_*")
            wristRotation = cmds.xform(cmds.ls("RIG_"+side+"_armTwist_"+str(len(armTwists) - 1)), q = True, ws = True, ro = True)
        else:
            wristRotation = cmds.xform(cmds.ls("RIG_"+side+"_Elbow"), q = True, ws = True, ro = True)
            
        cmds.move(wristPos[0], wristPos[1], wristPos[2], wrist_ctrl)
        wristGrp = cmds.group(em = True, name = 'CTRL_GRP_'+side+'_Wrist')
        cmds.move(wristPos[0],wristPos[1],wristPos[2], wristGrp)
        cmds.parent(wrist_ctrl, wristGrp)
        
        cmds.rotate(0,0, -wristRotation[2], wristGrp)
        cmds.parent(wristGrp, "MASTER_CONTROLLER")


def createClavicles(spineCount):
    
    l_clavicle = cmds.curve(p = [(1,0,0),(1,1,1), (1,1.5,2), (1,1.7,3), (1,1.5,4), (1,1,5), (1,0,6), (-1, 0,6), (-1,1,5), (-1,1.5,4), (-1,1.7,3), (-1,1.5,2), (-1,1,1), (-1,0,0) ], degree = 1, name = "CTRL_L_Clavicle")
    r_clavicle = cmds.curve(p = [(1,0,0),(1,1,1), (1,1.5,2), (1,1.7,3), (1,1.5,4), (1,1,5), (1,0,6), (-1, 0,6), (-1,1,5), (-1,1.5,4), (-1,1.7,3), (-1,1.5,2), (-1,1,1), (-1,0,0) ], degree = 1, name = "CTRL_R_Clavicle")
    
    cmds.scale(0.02, 0.02, 0.02, l_clavicle)
    cmds.scale(0.02, 0.02, 0.02, r_clavicle)
    
    l_ArmPos = cmds.xform(cmds.ls("RIG_L_upperArm"), q = True, t = True, ws = True)
    r_ArmPos = cmds.xform(cmds.ls("RIG_R_upperArm"), q = True, t = True, ws = True)
    
    l_claviclePos = cmds.xform(cmds.ls("RIG_L_Clavicle"), q = True, t = True, ws = True)
    r_claviclePos = cmds.xform(cmds.ls("RIG_R_Clavicle"), q = True, t = True, ws = True)
    
    cmds.move(l_ArmPos[0], l_ArmPos[1] + 0.125, l_ArmPos[2] - 0.1, l_clavicle)
    cmds.move(r_ArmPos[0], r_ArmPos[1] + 0.125, r_ArmPos[2] - 0.1, r_clavicle)
    
    cmds.move(l_claviclePos[0],l_claviclePos[1],l_claviclePos[2], l_clavicle+".scalePivot", l_clavicle+".rotatePivot")
    cmds.move(r_claviclePos[0],r_claviclePos[1],r_claviclePos[2], r_clavicle+".scalePivot", r_clavicle+".rotatePivot")

    cmds.makeIdentity(l_clavicle, apply = True, t = 1, r = 1, s = 1)
    cmds.makeIdentity(r_clavicle, apply = True, t = 1, r = 1, s = 1)
    
    cmds.parent(l_clavicle, "CTRL_SPINE_"+str(spineCount - 1))
    cmds.parent(r_clavicle, "CTRL_SPINE_"+str(spineCount - 1))

def createSpines(spineCount):
    
    for i in range(0, spineCount):
        spinePos = cmds.xform(cmds.ls("RIG_SPINE_"+str(i)), q = True, t = True, ws = True)
        spine = cmds.curve(p =[(0, spinePos[1], spinePos[2]), (0, spinePos[1], spinePos[2] - 1), (0, spinePos[1] + 0.1, spinePos[2] - 1.1), (0, spinePos[1] + 0.1, spinePos[2] - 1.4), (0, spinePos[1] - 0.1, spinePos[2] - 1.4), (0, spinePos[1] - 0.1, spinePos[2] - 1.1), (0, spinePos[1], spinePos[2] - 1)], degree = 1, name = "CTRL_SPINE_"+str(i))
        cmds.move(spinePos[0], spinePos[1], spinePos[2], spine+".scalePivot", spine+".rotatePivot")
        cmds.scale(0.5, 0.5, 0.5, spine)
        if (i == 0):
            cmds.parent(spine, "CTRL_PELVIS")
        else:
            cmds.parent(spine, "CTRL_SPINE_"+str(i-1))
      
def createNeck(spineCount):
    neck = cmds.curve(p = [(0.5,0,0), (0.25, -0.25, -0.5), (-0.25, -0.25, -0.5), (-0.5,0,0), (-0.25, -0.25, 0.5), (0.25, -0.25, 0.5), (0.5, 0,0)], degree = 1, name = "CTRL_NECK")
    neckPos = cmds.xform(cmds.ls("RIG_Neck"), q = True, t = True, ws = True)
    cmds.scale(0.3, 0.3, 0.3, neck)
    cmds.move(neckPos[0], neckPos[1]+0.1, neckPos[2], neck)
    cmds.move(neckPos[0], neckPos[1], neckPos[2], neck+".scalePivot", neck+".rotatePivot")
    cmds.parent(neck, "CTRL_SPINE_"+str(spineCount-1))
    
    cmds.makeIdentity(neck, apply = True, t = 1, r = 1, s = 1)
 
def createHead():
    
    head = cmds.curve(p = [(0.5,0,0), (0.25,-0.25,-0.5), (0.25,-0.5, -0.5), (0,-0.6,-0.5),(-0.25,-0.5,-0.5), (-0.25, -0.25, -0.5), (-0.5,0,0), (-0.25, -0.25, 0.5), (-0.25, -0.5, 0.5), (0,-0.6, 0.5) ,(0.25, -0.5, 0.5),(0.25, -0.25, 0.5), (0.5,0,0)], degree = 1, name = "CTRL_HEAD")
    cmds.scale(0.3, 0.3, 0.3, head)
    headPos = cmds.xform(cmds.ls("RIG_Head"), q= True, t = True, ws = True)
    neckPos = cmds.xform(cmds.ls("RIG_Neck"), q = True, t = True, ws = True)
    cmds.move(headPos[0], headPos[1], headPos[2], head)
    cmds.move(neckPos[0], neckPos[1], neckPos[2], head+".scalePivot", head+".rotatePivot")
    cmds.parent(head, "CTRL_NECK")
    cmds.makeIdentity(head, apply = True, t = 1, r = 1, s = 1)
    
    #jaw
    jaw = cmds.curve(p = [(0,0,0),(0.1, 0.1, 0), (0, 0.2,0), (-0.1, 0.1,0), (0,0,0)], degree = 1, name = "CTRL_JAW")
    cmds.move(0, 0.1, 0, jaw+".scalePivot", jaw+".rotatePivot")
    cmds.scale(0.3, 0.3, 0.3, jaw)
    jawPos = cmds.xform(cmds.ls("RIG_Jaw_End"), q = True, t = True, ws = True)
    jawStart = cmds.xform(cmds.ls("RIG_Jaw_Start"), q = True, t = True, ws = True)
    cmds.move(jawPos[0], jawPos[1]-0.1, jawPos[2]+0.1, jaw)
    cmds.move(jawStart[0], jawStart[1], jawStart[2], jaw+".scalePivot", jaw+".rotatePivot")
    cmds.parent(jaw, "CTRL_HEAD")
    cmds.makeIdentity(jaw, apply = True, t = 1, r = 1, s = 1)
    
        
def createFeet():
    l_arrow = cmds.curve(p = [(1,0,0),(1,0,2), (2,0,2),(0,0,6), (-2,0,2), (-1,0,2), (-1,0,0), (1,0,0)], degree = 1, name = "CTRL_L_Foot")
    cmds.addAttr(shortName = "KF", longName = "Knee_Twist", attributeType = 'double', defaultValue = 0, minValue = -100, maxValue = 100, keyable = True)
    cmds.addAttr(shortName = "KR", longName = "Knee_Fix", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True)
    cmds.addAttr(shortName = "FR", longName = "Foot_Roll", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True)
    cmds.addAttr(shortName = "BR", longName = "Ball_Roll", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True)


    r_arrow = cmds.curve(p = [(1,0,0),(1,0,2), (2,0,2),(0,0,6), (-2,0,2), (-1,0,2), (-1,0,0), (1,0,0)], degree = 1, name = "CTRL_R_Foot")
    cmds.addAttr(shortName = "KF", longName = "Knee_Twist", attributeType = 'double', defaultValue = 0, minValue = -100, maxValue = 100, keyable = True)
    cmds.addAttr(shortName = "KR", longName = "Knee_Fix", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True)
    cmds.addAttr(shortName = "FR", longName = "Foot_Roll", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True)
    cmds.addAttr(shortName = "BR", longName = "Ball_Roll", attributeType = 'double', defaultValue = 0, minValue = 0, maxValue = 100, keyable = True)
    
    cmds.scale(0.08, 0.08, 0.08, l_arrow)
    cmds.scale(0.08, 0.08, 0.08, r_arrow)

    l_footPos = cmds.xform(cmds.ls("RIG_L_Foot"), q = True, t = True, ws = True)
    r_footPos = cmds.xform(cmds.ls("RIG_R_Foot"), q = True, t = True, ws = True)

    cmds.move(l_footPos[0], l_footPos[1], l_footPos[2], l_arrow)
    cmds.move(r_footPos[0], r_footPos[1], r_footPos[2], r_arrow)
    
    cmds.makeIdentity(l_arrow, apply = True, t = 1, r = 1, s = 1)
    cmds.makeIdentity(r_arrow, apply = True, t = 1, r = 1, s = 1)
        
    cmds.parent(l_arrow, "MASTER_CONTROLLER")
    cmds.parent(r_arrow, "MASTER_CONTROLLER")
 
def createFingers(fingerCount):
    sides = ['L', 'R']
    for side in sides:
        for i in range(0, fingerCount):
            
            for j in range(0, 3):
                
                #fingerRotation = cmds.joint(cmds.ls("RIG_" + side + "_Finger_" + str(i) + "_" + str(j)), q = True, o = True)
                fingerRotation = cmds.xform(cmds.ls("Loc_" + side + "_finger_" + str(i) + "_" + str(j)), q = True, ws = True, ro = True)
                fingerPosition = cmds.xform(cmds.ls("Loc_" + side + "_finger_" + str(i) + "_" + str(j)), q = True, ws = True, t = True)
                
                allFingers =  cmds.ls("RIG_" + side + "_Finger_" + str(i) + "_" + str(j))

        
                finger = cmds.curve(p =[(0,0,0), (0,0,0.5), (0.2, 0, 0.7),(0,0,0.9), (-0.2, 0, 0.7), (0,0,0.5)], degree = 1, name = "CTRL_"+side+"_Finger_"+str(i)+"_"+str(j))
                cmds.rotate(-90,0,0, finger)
                
                for k, fi in enumerate(allFingers):
                    fingerPos = cmds.xform(fi, q = True, t = True, ws = True)
                    fingerRot = cmds.joint(fi, q = True, o = True)
                    cmds.scale(0.1, 0.1, 0.1, finger)
                    cmds.move(fingerPos[0], fingerPos[1], fingerPos[2], finger)
                
                fingerGrp = cmds.group(em = True, n = "CTRL_GRP_"+side+"_Finger_"+str(i)+"_"+str(j))
                cmds.move(fingerPosition[0], fingerPosition[1], fingerPosition[2], fingerGrp)
                cmds.rotate(0, fingerRotation[1], 0, finger, r = True)
                cmds.makeIdentity(finger, apply = True, t = 1, r = 1, s = 1)
                cmds.makeIdentity(fingerGrp, apply = True, t = 1, r = 1, s = 1)
                cmds.parent(finger, fingerGrp)
                cmds.rotate(0, fingerRotation[1], 0, fingerGrp, r = True)

                if j > 0:
                    cmds.parent(fingerGrp, "CTRL_"+side+"_Finger_"+str(i)+"_"+str(j-1))
                else:
                    cmds.parent(fingerGrp, "CTRL_"+side+"_Wrist")

  
def setColors():
    cmds.setAttr('MASTER_CONTROLLER.overrideEnabled', 1)
    cmds.setAttr('MASTER_CONTROLLER.overrideRGBColors', 1)
    cmds.setAttr('MASTER_CONTROLLER.overrideColorRGB', 1,1,1)