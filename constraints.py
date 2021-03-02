import maya.cmds as cmds

import setAttributes

setAttributes = reload(setAttributes)

def createConstraints(spineAmount, fingerCount):
    
    #left
    l_wristCtrl = cmds.ls("CTRL_L_Wrist", type = 'transform')
    l_wristIK = cmds.ls("IK_L_Arm")
    l_wristJoint = cmds.ls("RIG_L_wrist")
        

    #right
    r_wristCtrl = cmds.ls("CTRL_R_Wrist", type = 'transform')
    r_wristIK = cmds.ls("IK_R_Arm")
    r_wristJoint = cmds.ls("RIG_R_wrist")
    
    cmds.pointConstraint(l_wristCtrl, l_wristIK, mo = True)
    cmds.orientConstraint(l_wristCtrl, l_wristJoint, mo = True)
    cmds.connectAttr("CTRL_L_Wrist.Elbow_PV", "IK_L_Arm.twist")
    
    cmds.pointConstraint(r_wristCtrl, r_wristIK, mo = True)
    cmds.orientConstraint(r_wristCtrl, r_wristJoint, mo = True)    
    cmds.connectAttr("CTRL_R_Wrist.Elbow_PV", "IK_R_Arm.twist") 
    
    cmds.orientConstraint("CTRL_L_Clavicle", "RIG_L_Clavicle", mo = True)
    cmds.orientConstraint("CTRL_R_Clavicle", "RIG_R_Clavicle", mo = True)
    cmds.orientConstraint("CTRL_NECK", "RIG_Neck", mo = True)
    cmds.orientConstraint("CTRL_HEAD", "RIG_Head", mo = True)
    cmds.orientConstraint("CTRL_JAW", "RIG_Jaw_Start", mo = True)
    if(cmds.objExists("CTRL_BREATHING")):
        cmds.orientConstraint("CTRL_BREATHING", "RIG_BREATHING_START", mo = True)
    
    cmds.connectAttr("CTRL_SPINE_"+str(spineAmount - 1)+".rotateY", "IK_Spine.twist")
    
    if cmds.objExists("RIG_L_armTwist_0"):
        l_twistJoints = cmds.ls("RIG_L_armTwist_*")
        r_twistJoints = cmds.ls("RIG_R_armTwist_*")
        for i, x in enumerate(l_twistJoints):   
            print "IN THE LOOP"
            l_wristMultiply = cmds.shadingNode("multiplyDivide", asUtility = True, n = "L_armTwist_Node_"+str(i))
            cmds.setAttr(l_wristMultiply+".operation", 1)
            cmds.setAttr(l_wristMultiply+".input2Y", (1.0 - (1.0 / len(l_twistJoints) * (i + 1))) * -1)
            
            if cmds.objExists("L_armTwist_Node_*"):
                print "NODE CREATED"
            #check connections
            print cmds.listConnections("L_armTwist_Node_"+str(i), plugs = True)
            
            #input
            cmds.connectAttr("CTRL_L_Wrist.rotateY", "L_armTwist_Node_"+str(i)+".input1Y")
            #output
            cmds.connectAttr("L_armTwist_Node_"+str(i)+".outputY", "RIG_L_armTwist_"+str(i)+".rotateX")
            
            r_wristMultiply = cmds.shadingNode("multiplyDivide", asUtility = True, n = "R_armTwist_Node_"+str(i))
            cmds.setAttr(r_wristMultiply+".operation", 1)
            cmds.setAttr(r_wristMultiply+".input2Y", (1.0 - (1.0 / len(r_twistJoints) * (i + 1))) * -1)
            #input
            cmds.connectAttr("CTRL_R_Wrist.rotateY", "R_armTwist_Node_"+str(i)+".input1Y")
            #output
            cmds.connectAttr("R_armTwist_Node_"+str(i)+".outputY", "RIG_R_armTwist_"+str(i)+".rotateX")
            
    
    clusters = cmds.ls("Spine_Cluster_*", type = 'transform')
    spineCtrl = cmds.ls("CTRL_SPINE_*", type = 'transform')      
    
    for j, cl in enumerate(clusters):
        if j > 0:
            print j
            cmds.parent(cl, spineCtrl[j - 1])
            #print spineCtrl[j - 1]
        else:
            cmds.parent(cl, "CTRL_PELVIS")     
            
                
    for k in range(0, fingerCount):
        l_allFingers = cmds.ls("RIG_L_Finger_"+str(k)+"_*")
        r_allFingers = cmds.ls("RIG_R_Finger_"+str(k)+"_*") 
        
        for l in range(0,3):
            if(k > 0):
                cmds.connectAttr("CTRL_L_Finger_"+str(k)+"_"+str(l)+".rotateZ", l_allFingers[l]+".rotateZ")
                cmds.connectAttr("CTRL_R_Finger_"+str(k)+"_"+str(l)+".rotateZ", r_allFingers[l]+".rotateZ")
                cmds.connectAttr("CTRL_L_Finger_"+str(k)+"_"+str(l)+".rotateX", l_allFingers[l]+".rotateY")
                cmds.connectAttr("CTRL_R_Finger_"+str(k)+"_"+str(l)+".rotateX", r_allFingers[l]+".rotateY")
            else:
                cmds.connectAttr("CTRL_L_Finger_"+str(k)+"_"+str(l)+".rotateZ", l_allFingers[l]+".rotateZ")
                cmds.connectAttr("CTRL_R_Finger_"+str(k)+"_"+str(l)+".rotateZ", r_allFingers[l]+".rotateZ")
                cmds.connectAttr("CTRL_L_Finger_"+str(k)+"_"+str(l)+".rotateX", l_allFingers[l]+".rotateY")
                cmds.connectAttr("CTRL_R_Finger_"+str(k)+"_"+str(l)+".rotateX", r_allFingers[l]+".rotateY")                
               
     
    if cmds.objExists("RIG_L_inv_heel"):
        cmds.pointConstraint("RIG_L_inv_toes", "IK_L_Toes", mo = True)
        cmds.pointConstraint("RIG_L_inv_ball", "IK_L_FootBall", mo = True)
        cmds.pointConstraint("RIG_L_inv_ankle", "IK_L_Leg", mo = True)
        
        cmds.pointConstraint("RIG_R_inv_toes", "IK_R_Toes", mo = True)
        cmds.pointConstraint("RIG_R_inv_ball", "IK_R_FootBall", mo = True)
        cmds.pointConstraint("RIG_R_inv_ankle", "IK_R_Leg", mo = True)
        
        cmds.pointConstraint("CTRL_L_Foot", "RIG_L_inv_heel", mo = True)
        cmds.orientConstraint("CTRL_L_Foot", "RIG_L_inv_heel", mo = True)
        
        cmds.pointConstraint("CTRL_R_Foot", "RIG_R_inv_heel", mo = True)
        cmds.orientConstraint("CTRL_R_Foot", "RIG_R_inv_heel", mo = True)
        
        cmds.connectAttr("CTRL_L_Foot.Foot_Roll", "RIG_L_inv_ball.rotateX")
        cmds.connectAttr("CTRL_L_Foot.Ball_Roll", "RIG_L_inv_toes.rotateX")
        
        cmds.connectAttr("CTRL_R_Foot.Foot_Roll", "RIG_R_inv_ball.rotateX")
        cmds.connectAttr("CTRL_R_Foot.Ball_Roll", "RIG_R_inv_toes.rotateX")
        
       
        
    else:
        cmds.parent("IK_L_Toes", "IK_L_FootBall")
        cmds.parent("IK_L_FootBall", "IK_L_Leg")              
        
        cmds.parent("IK_R_Toes", "IK_R_FootBall")
        cmds.parent("IK_R_FootBall", "IK_R_Leg")        
        
        cmds.pointConstraint("CTRL_R_Foot", "IK_R_Leg", mo = True)
        cmds.orientConstraint("CTRL_R_Foot", "IK_R_Leg", mo = True)
        
        cmds.pointConstraint("CTRL_L_Foot", "IK_L_Leg", mo = True)
        cmds.orientConstraint("CTRL_L_Foot", "IK_L_Leg", mo = True)
        
    
    #feet constraints    
    
    #lleft
    cmds.setAttr("IK_L_Leg.poleVectorX", 1)
    cmds.setAttr("IK_L_Leg.poleVectorZ", 0)
    l_footAverage = cmds.shadingNode("plusMinusAverage", asUtility = True, n = "L_Foot_Node") 
    cmds.setAttr(l_footAverage+".operation", 2)   
    cmds.connectAttr("CTRL_L_Foot.Knee_Fix", l_footAverage+".input1D[0]")
    cmds.connectAttr("CTRL_L_Foot.Knee_Twist", l_footAverage+".input1D[1]")  
    cmds.connectAttr(l_footAverage+".output1D", "IK_L_Leg.twist")  
    cmds.setAttr("CTRL_L_Foot.Knee_Fix", 90)
    
    #right
    cmds.setAttr("IK_R_Leg.poleVectorX", 1)
    cmds.setAttr("IK_R_Leg.poleVectorZ", 0)
    r_footAverage = cmds.shadingNode("plusMinusAverage", asUtility = True, n = "R_Foot_Node") 
    cmds.setAttr(r_footAverage+".operation", 2)   
    cmds.connectAttr("CTRL_R_Foot.Knee_Fix", r_footAverage+".input1D[0]")
    cmds.connectAttr("CTRL_R_Foot.Knee_Twist", r_footAverage+".input1D[1]")  
    cmds.connectAttr(r_footAverage+".output1D", "IK_R_Leg.twist")  
    cmds.setAttr("CTRL_R_Foot.Knee_Fix", 90)
    
    setAttributes.LockAttributes()    

def BindSkin():
    sel = cmds.ls(sl = True)
    if (len(sel) == 0):
        cmds.confirmDialog(title = "Empty Selection", message = "You have to select a mesh", button = ['Ok'])
    else:
        for i in range(0, len(sel)):
            cmds.skinCluster(sel[i], "RIG_ROOT", bm = 3, sm = 1, dr = 0.1, name = "Mesh"+str(i))
            cmds.geomBind('Mesh'+str(i), bm = 3, gvp = [256, 1])   
    
     

    if (cmds.objExists("RIG_LAYER")):
        _rig = cmds.select("RIG") 
        cmds.editDisplayLayerMembers("RIG_LAYER", "RIG")
    else:   
        _rig = cmds.select("RIG") 
        cmds.createDisplayLayer(nr = True, name = "RIG_LAYER")        
    
    _ik = cmds.ls("IK_*")
    cmds.editDisplayLayerMembers("RIG_LAYER", _ik)
    

    if (cmds.objExists("CONTROLLERS")):
        cmds.editDisplayLayerMembers("CONTROLLERS", "MASTER_CONTROLLER")
    else:
        _ctrl = cmds.select("MASTER_CONTROLLER")    
        cmds.createDisplayLayer(nr = True, name = "CONTROLLERS")
        