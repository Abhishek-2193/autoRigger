import maya.cmds as cmds


def createFields(spineValue, fingerValue):
    
    global spineCount
    global fingerCount
    
    #spineCount = 4
    #fingerCount = 5
    
def returnFingerAmount():
        return fingerCount
        
def returnSpineAmount():
        return spineCount
        
    

def createLocators(spineValue, fingerValue):
    
    global spineCount
    global fingerCount
    
    spineCount = spineValue
    fingerCount = fingerValue
    
    if cmds.objExists('Loc_MASTER'):
        print 'Master Locator already exists'
    else:
        MASTER = cmds.group(em = True, name = "Loc_MASTER")
        
    root = cmds.spaceLocator(n = "Loc_ROOT")
    root = cmds.scale(0.1, 0.1, 0.1, root)
    cmds.move(0, 1, 0, root)
    cmds.parent(root, MASTER)
    createSpine()
    
def createSpine():
    
    for i in range(0, spineCount):
        spine = cmds.spaceLocator(n = 'Loc_Spine_' + str(i))
        cmds.scale(0.1, 0.1, 0.1, spine)
        if i == 0:
            cmds.parent(spine, 'Loc_ROOT')
        else:
            cmds.parent(spine, 'Loc_Spine_' + str(i-1))
        cmds.move(0, 1.25 + (0.25 * i), 0, spine)
    
    createHead()    
    createArms(1)
    createArms(-1)
    createLegs(1)
    createLegs(-1)
    setColors()
    
def createHead():

    neck = cmds.spaceLocator(n = 'Loc_Neck')
    cmds.parent(neck, 'Loc_Spine_' + str(returnSpineAmount() - 1))
    cmds.scale(1, 1, 1, neck)
    cmds.move(0, 1.25 + (0.25 * returnSpineAmount()), 0, neck)
    
    head = cmds.spaceLocator(n = 'Loc_Head')
    cmds.parent(head, 'Loc_Neck')
    cmds.scale(1, 1, 1, head)
    cmds.move(0, 1.50 + (0.25 * spineCount), 0, head)
    
    jawEnd = cmds.spaceLocator(n = 'Loc_Jaw_End')
    jawStart = cmds.spaceLocator(n = 'Loc_Jaw_Start')
    cmds.parent(jawStart, 'Loc_Head')
    cmds.parent(jawEnd, jawStart)
    cmds.scale(1, 1, 1, jawEnd)
    cmds.scale(0.5, 0.5, 0.5, jawStart)
    cmds.move(0, 1.40 + (0.25 * spineCount), 0.02, jawStart)
    cmds.move(0, 1.40 + (0.25 * spineCount), 0.15, jawEnd)
    
    

def createLegs(side):
    
    if side == 1: #left
        
        if cmds.objExists('L_leg_grp'):
            print 'Left leg group already created'
        
        else:
            
            upperLegGrp = cmds.group(em = True, name = 'L_leg_grp')
            cmds.parent(upperLegGrp, 'Loc_ROOT')
            cmds.move(0.1, 1, 0, upperLegGrp)
            
        #upperleg
        upperLeg = cmds.spaceLocator(n = 'Loc_L_upperLeg')
        cmds.scale(0.1, 0.1, 0.1, upperLeg)
        cmds.move(0.15, 1, 0, upperLeg)
        cmds.parent(upperLeg, 'L_leg_grp')
        
        #lowerLeg
        lowerLeg = cmds.spaceLocator(n = 'Loc_L_lowerLeg')
        cmds.scale(0.1, 0.1, 0.1, lowerLeg)
        cmds.move(0.15, 0.2, 0.1, lowerLeg)
        cmds.parent(lowerLeg, 'Loc_L_upperLeg')
        
        #foot
        foot = cmds.spaceLocator(n = 'Loc_L_Foot')
        cmds.scale(0.1, 0.1, 0.1, foot)
        cmds.move(0.15, -0.4, 0, foot)
        cmds.parent(foot, 'Loc_L_lowerLeg')
        
        #footBall
        footBall = cmds.spaceLocator(n = 'Loc_L_FootBall')
        cmds.scale(0.1, 0.1, 0.1, footBall)
        cmds.move(0.15, -0.5, 0.15, footBall)
        cmds.parent(footBall, 'Loc_L_Foot')
        
        #toes
        toes = cmds.spaceLocator(n = 'Loc_L_Toes')
        cmds.scale(0.1, 0.1, 0.1, toes)
        cmds.move(0.15, -0.5, 0.3, toes)
        cmds.parent(toes, 'Loc_L_FootBall')
        
            
    else: #right
        if cmds.objExists('R_leg_grp'):
            print 'Right leg group already created'
        else:
            upperLegGrp = cmds.group(em = True, name = 'R_leg_grp')
            cmds.parent(upperLegGrp, 'Loc_ROOT')
            cmds.move(-0.1, 1, 0, upperLegGrp)
            

        upperLeg = cmds.spaceLocator(n = 'Loc_R_upperLeg')
        cmds.scale(0.1, 0.1, 0.1, upperLeg)
        cmds.move(-0.15, 1, 0, upperLeg)
        cmds.parent(upperLeg, 'R_leg_grp')
        
        
        #lowerLeg
        lowerLeg = cmds.spaceLocator(n = 'Loc_R_lowerLeg')
        cmds.scale(0.1, 0.1, 0.1, lowerLeg)
        cmds.move(-0.15, 0.2, 0.1, lowerLeg)
        cmds.parent(lowerLeg, 'Loc_R_upperLeg')
        
        #foot
        foot = cmds.spaceLocator(n = 'Loc_R_Foot')
        cmds.scale(0.1, 0.1, 0.1, foot)
        cmds.move(-0.15, -0.4, 0, foot)
        cmds.parent(foot, 'Loc_R_lowerLeg')
        
        #footBall
        footBall = cmds.spaceLocator(n = 'Loc_R_FootBall')
        cmds.scale(0.1, 0.1, 0.1, footBall)
        cmds.move(-0.15, -0.5, 0.15, footBall)
        cmds.parent(footBall, 'Loc_R_Foot')
        
        #toes
        toes = cmds.spaceLocator(n = 'Loc_R_Toes')
        cmds.scale(0.1, 0.1, 0.1, toes)
        cmds.move(-0.15, -0.5, 0.3, toes)
        cmds.parent(toes, 'Loc_R_FootBall')
            
def createArms(side):
    
    if side == 1: #left
        if cmds.objExists('L_arm_grp'):
            print 'Left arm group already created'
        else:
            L_arm = cmds.group(em = True, name = 'L_arm_grp')
            cmds.parent(L_arm, 'Loc_Spine_' + str(spineCount - 1))
            
            #clavicle
            clavicle = cmds.spaceLocator(n = 'Loc_L_Clavicle')
            cmds.scale(0.1, 0.1, 0.1, clavicle)
            cmds.parent(clavicle, 'Loc_Spine_' + str(spineCount - 1))
            cmds.move(0.1 * side, 1 + (0.25 * spineCount), 0.1, clavicle)
                      
            #upperarm
            upperArm = cmds.spaceLocator(n = 'Loc_L_upperArm')
            cmds.scale(0.1, 0.1, 0.1, upperArm)
            cmds.parent(upperArm, 'Loc_L_Clavicle')
            cmds.move(0.35 * side, 1 + (0.25 * spineCount), 0.1, upperArm)
            
            #elbow
            elbow = cmds.spaceLocator(n = 'Loc_L_elbow')
            cmds.scale(0.1, 0.1, 0.1, elbow)
            cmds.parent(elbow, upperArm)
            
            #wrist
            wrist = cmds.spaceLocator(n = 'Loc_L_wrist')
            cmds.scale(0.1, 0.1, 0.1, wrist)
            cmds.parent(wrist, elbow)
            
            #moving
            cmds.move(0.35 * side, 1 + (0.25 * spineCount), 0, L_arm)
            cmds.move(0.6 * side, 1.4, -0.2, elbow)
            cmds.move(0.8 * side, 1, 0, wrist)
            
            createHands(1, wrist)
            
    else: #right
        if cmds.objExists('R_arm_grp'):
            print 'Right arm group already created'
        else:
            R_arm = cmds.group(em = True, name = 'R_arm_grp')
            cmds.parent(R_arm, 'Loc_Spine_' + str(spineCount - 1))
            
            #clavicle
            clavicle = cmds.spaceLocator(n = 'Loc_R_Clavicle')
            cmds.scale(0.1, 0.1, 0.1, clavicle)
            cmds.parent(clavicle, 'Loc_Spine_' + str(spineCount - 1))
            cmds.move(0.1 * side, 1 + (0.25 * spineCount), 0.1, clavicle)
                      
            #upperarm
            upperArm = cmds.spaceLocator(n = 'Loc_R_upperArm')
            cmds.scale(0.1, 0.1, 0.1, upperArm)
            cmds.parent(upperArm, 'Loc_R_Clavicle')
            cmds.move(0.35 * side, 1 + (0.25 * spineCount), 0.1, upperArm)
            
            #elbow
            elbow = cmds.spaceLocator(n = 'Loc_R_elbow')
            cmds.scale(0.1, 0.1, 0.1, elbow)
            cmds.parent(elbow, upperArm)
            
            #wrist
            wrist = cmds.spaceLocator(n = 'Loc_R_wrist')
            cmds.scale(0.1, 0.1, 0.1, wrist)
            cmds.parent(wrist, elbow)
            
            #moving
            cmds.move(0.35 * side, 1 + (0.25 * spineCount), 0, R_arm)
            cmds.move(0.6 * side, 1.4, -0.2, elbow)
            cmds.move(0.8 * side, 1, 0, wrist)
            
            createHands(-1, wrist)
    
    #lockAll(editMode)


def createHands(side, wrist):
    
    if side == 1:
        if cmds.objExists('L_hand_grp'):
            print 'Left hand group already exists'
        else:
            hand = cmds.group(em = True, name = 'L_hand_grp')
            pos = cmds.xform(wrist, q = True, t = True, ws = True)
            cmds.move(pos[0], pos[1], pos[2], hand)
            cmds.parent(hand, 'Loc_L_wrist')
            
            for i in range(0, fingerCount):
                createFingers(1, pos, i)

    else:
        if cmds.objExists('R_hand_grp'):
            print 'Right hand group already exists'
        else:
            hand = cmds.group(em = True, name = 'R_hand_grp')
            pos = cmds.xform(wrist, q = True, t = True, ws = True)
            cmds.move(pos[0], pos[1], pos[2], hand)
            cmds.parent(hand, 'Loc_R_wrist')
            
            for i in range(0, fingerCount):
                createFingers(-1, pos, i)
                       
                   
def createFingers(side, handPos, count):
    
    for x in range(0,4):
        
        if side == 1:
            
            finger = cmds.spaceLocator(n = 'Loc_L_finger_' + str(count) + '_' + str(x))
            cmds.scale(0.05, 0.05, 0.05, finger)
            
            if x == 0:
                cmds.parent(finger, 'Loc_L_wrist')
            else:
                cmds.parent(finger, 'Loc_L_finger_' + str(count) + '_' + str(x - 1))
            
            cmds.move(handPos[0] + (0.1 + (0.1 * x)) * side, handPos[1] - (0.1 + (0.1 * x)), handPos[2] + (0.05 * count), finger)
            
            
        else:
            finger = cmds.spaceLocator(n = 'Loc_R_finger_' + str(count) + '_' + str(x))
            cmds.scale(0.05, 0.05, 0.05, finger)
            
            if x == 0:
                cmds.parent(finger, 'Loc_R_wrist')
            else:
                cmds.parent(finger, 'Loc_R_finger_' + str(count) + '_' + str(x - 1))
            
            cmds.move(handPos[0] + (0.1 + (0.1 * x)) * side, handPos[1] - (0.1 + (0.1 * x)), handPos[2] + (0.05 * count), finger)
            
def mirrorLocators():

    allLeftLocators = cmds.ls('Loc_L*', type = 'transform')
    allRightLocators = cmds.ls('Loc_R*', type = 'transform')

    allRightLocators.remove('Loc_ROOT')

    for i, l in enumerate(allLeftLocators):
        
        if "finger" in str(l):
            pos = cmds.xform(l, q = True, t = True, ws = True)
            
            if "_0" in str(l):
                rot = cmds.xform(l, q = True, ro = True, ws = True)
                cmds.rotate(rot[0], -rot[1], rot[2], allRightLocators[i])
                cmds.move(-pos[0], pos[1], pos[2], allRightLocators[i])
            else:
                cmds.move(-pos[0], pos[1], pos[2], allRightLocators[i])
        else:        
            pos = cmds.xform(l, q = True, t = True, ws = True)
            rot = cmds.xform(l, q = True, ro = True, ws = True)
            cmds.move(-pos[0], pos[1], pos[2], allRightLocators[i])
                
def deleteLocators():
    nodes = cmds.ls('Loc_*')
    cmds.delete(nodes)

def setColors():
    cmds.setAttr('Loc_MASTER.overrideEnabled', 1)
    cmds.setAttr('Loc_MASTER.overrideRGBColors', 1)