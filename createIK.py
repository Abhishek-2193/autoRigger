import maya.cmds as cmds
import createLocators

createLocators = reload(createLocators)

def IKHandles():
    
    if not cmds.objExists("RIG_L_ArmTwist_*"):

        cmds.ikHandle(name = "IK_L_Arm", sj = cmds.ls("RIG_L_upperArm")[0], ee = cmds.ls("RIG_L_wrist")[0], sol = 'ikRPsolver')
        cmds.ikHandle(name = "IK_R_Arm", sj = cmds.ls("RIG_R_upperArm")[0], ee = cmds.ls("RIG_R_wrist")[0], sol = 'ikRPsolver')
    
    else:

        cmds.ikHandle(name = "IK_L_Arm", sj = cmds.ls("RIG_L_upperArm")[0], ee = cmds.ls("RIG_L_armTwist_0")[0], sol = 'ikRPsolver')
        cmds.ikHandle(name = "IK_R_Arm", sj = cmds.ls("RIG_R_upperArm")[0], ee = cmds.ls("RIG_R_armTwist_0")[0], sol = 'ikRPsolver')     

        leftWristPos = cmds.xform(cmds.ls("RIG_L_wrist"), q = True, ee = True)
        rightWristPos = cmds.xform(cmds.ls("RIG_R_wrist"), q = True, ee = True)
        
        leftIK = cmds.ikHandle("IK_L_Arm", q = True, ee = True)
        rightIK = cmds.ikHandle("IK_R_Arm", q = True, ee = True)

        cmds.move(leftWristPos[0], leftWristPos[1], leftWristPos[2], leftIK + ".scalePivot", leftIK + ".rotatePivot")
        cmds.move(rightWristPos[0], rightWristPos[1], rightWristPos[2], rightIK + ".scalePivot", rightIK + ".rotatePivot")

    cmds.ikHandle(name = "IK_L_Leg", sj = cmds.ls("RIG_L_upperLeg")[0], ee = cmds.ls("RIG_L_Foot")[0], sol = 'ikRPsolver')
    cmds.ikHandle(name = "IK_R_Leg", sj = cmds.ls("RIG_R_upperLeg")[0], ee = cmds.ls("RIG_R_Foot")[0], sol = 'ikRPsolver')

    cmds.ikHandle(name = "IK_L_FootBall", sj = cmds.ls("RIG_L_Foot")[0], ee = cmds.ls("RIG_L_FootBall")[0], sol = 'ikSCsolver')
    cmds.ikHandle(name = "IK_L_Toes", sj = cmds.ls("RIG_L_FootBall")[0], ee = cmds.ls("RIG_L_Toes")[0], sol = 'ikSCsolver')
    
    cmds.ikHandle(name = "IK_R_FootBall", sj = cmds.ls("RIG_R_Foot")[0], ee = cmds.ls("RIG_R_FootBall")[0], sol = 'ikSCsolver')
    cmds.ikHandle(name = "IK_R_Toes", sj = cmds.ls("RIG_R_FootBall")[0], ee = cmds.ls("RIG_R_Toes")[0], sol = 'ikSCsolver')
    

    rootPos = cmds.xform(cmds.ls("RIG_ROOT", type = 'joint'), q = True, t = True, ws = True)
    spines = cmds.ls("RIG_SPINE_*", type = 'joint')
    spinePos = []
    

    for i, sp in enumerate(spines):
        spinePos.append(cmds.xform(spines[i], q = True, t = True, ws = True))

    cmds.curve(p = [(rootPos[0], rootPos[1], rootPos[2])], n = "spineCurve", degree = 1)

    for j, sp in enumerate(spinePos):
        cmds.curve('spineCurve', a = True, p = [(spinePos[j][0], spinePos[j][1], spinePos[j][2])])


    curveCV = cmds.ls('spineCurve.cv[0:]', fl = True)
    print curveCV
    for k, cv in enumerate(curveCV):
        print str(k)
        c = cmds.cluster(cv, cv, n = "Spine_Cluster_" + str(k) + "_")

    cmds.ikHandle(n = "IK_Spine", sj = "RIG_ROOT", ee = "RIG_SPINE_3", sol = 'ikSplineSolver', c = 'spineCurve')
