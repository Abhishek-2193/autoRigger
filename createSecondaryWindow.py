import maya.cmds as cmds

from math import pow, sqrt, cos, acos, radians

class secLocators():

    def __init__(self):
        self.createSecLocatorWindows()

    def createSecLocatorWindows(self):
    
        cmds.window("Secondary Controllers", h = 500, w = 200, rtf = True, title = 'SECONDARY LOCATORS', titleBar = True)
        cmds.rowColumnLayout(nc = 1)
        cmds.image(i = "/Users/abhishekravi/Desktop/NEWMAYAWORK/Header2.png")
        cmds.separator(h = 10)
        cmds.button(l = "Create Reverse Footroll", w = 100, c = self.createReverseFootroll)
        cmds.separator(st = 'single', h = 10)
        #cmds.text("Twist Amount", l = "Amount of twist joints")
        #armTwist = cmds.intField(minValue = 2, maxValue = 10, value = 3)
        self.armTwistCount = cmds.intSliderGrp(l = "Number of twist joints", min = 4, max = 10, value = 4, step = 1, field = True)
        cmds.separator(h = 10)
        cmds.button(l = "Create Forearm Twist", w = 100, c = self.armTwist)
        cmds.separator(st = 'single', h = 10)
        cmds.button(l = "Delete Locators", w = 100, c = self.deleteSecondary)
        self.checkGroup(self)
        cmds.showWindow()
    

    def checkGroup(self, void):
        
        if cmds.objExists('SECONDARY'):
            print "Secondary Group Exists"
        else:
            cmds.group(em = True, n = 'SECONDARY')
            
        self.setColors(self)
        

    def createReverseFootroll(self, void):
        
        #Left
        #heel
        cmds.select(deselect = True)
        l_rev_heel = cmds.spaceLocator(n = 'Loc_L_inv_heel')
        cmds.scale(0.05, 0.05, 0.05, l_rev_heel)
        cmds.move(0.15, -0.5, 0, l_rev_heel)
        cmds.parent(l_rev_heel, 'SECONDARY')

        #toes
        l_rev_toes = cmds.spaceLocator(n = 'Loc_L_inv_toes')
        cmds.scale(0.05, 0.05, 0.05, l_rev_toes)
        cmds.move(0.15, -0.5, 0.3, l_rev_toes)
        cmds.parent(l_rev_toes, 'Loc_L_inv_heel')
        
        #ball
        l_rev_ball = cmds.spaceLocator(n = 'Loc_L_inv_ball')
        cmds.scale(0.05, 0.05, 0.05, l_rev_ball)
        cmds.move(0.15, -0.5, 0.15, l_rev_ball)
        cmds.parent(l_rev_ball, 'Loc_L_inv_toes')

        #ankle
        l_rev_ankle = cmds.spaceLocator(n = 'Loc_L_inv_ankle')
        cmds.scale(0.05, 0.05, 0.05, l_rev_ankle)
        cmds.move(0.15, -0.4, 0, l_rev_ankle)
        cmds.parent(l_rev_ankle, 'Loc_L_inv_ball')

        #Right
        #heel
        cmds.select(deselect = True)
        r_rev_heel = cmds.spaceLocator(n = 'Loc_R_inv_heel')
        cmds.scale(0.05, 0.05, 0.05, r_rev_heel)
        cmds.move(-0.15, -0.5, 0, r_rev_heel)
        cmds.parent(r_rev_heel, 'SECONDARY')
        
        #toes
        r_rev_toes = cmds.spaceLocator(n = 'Loc_R_inv_toes')
        cmds.scale(0.05, 0.05, 0.05, r_rev_toes)
        cmds.move(-0.15, -0.5, 0.3, r_rev_toes)
        cmds.parent(r_rev_toes, 'Loc_R_inv_heel')
        
        #ball
        r_rev_ball = cmds.spaceLocator(n = 'Loc_R_inv_ball')
        cmds.scale(0.05, 0.05, 0.05, r_rev_ball)
        cmds.move(-0.15, -0.5, 0.15, r_rev_ball)
        cmds.parent(r_rev_ball, 'Loc_R_inv_toes')
        
        #ankle
        r_rev_ankle = cmds.spaceLocator(n = 'Loc_R_inv_ankle')
        cmds.scale(0.05, 0.05, 0.05, r_rev_ankle)
        cmds.move(-0.15, -0.4, 0, r_rev_ankle)
        cmds.parent(r_rev_ankle, 'Loc_R_inv_ball')    
        
        
    def armTwist(self, void):
        _amount = cmds.intSliderGrp(self.armTwistCount, q = True, v = True)
        self.createForeArmTwist(self, _amount)

    def createForeArmTwist(self, void, amount):
        
        cmds.select(deselect = True)
        
        L_elbowPos = cmds.xform(cmds.ls('Loc_L_elbow'), q = True, t = True, ws = True)
        L_wristPos = cmds.xform(cmds.ls('Loc_L_wrist'), q = True, t = True, ws = True)
        
        L_vectorX = L_wristPos[0] - L_elbowPos[0]
        L_vectorY = L_wristPos[1] - L_elbowPos[1]
        L_vectorZ = L_wristPos[2] - L_elbowPos[2]
        
        print amount
        
        for i in range(amount -1):
            
            L_twistLoc = cmds.spaceLocator(n = 'Loc_L_armTwist_' + str(i))
            cmds.move(L_elbowPos[0] + (L_vectorX / amount) + ((L_vectorX / amount) * i), L_elbowPos[1] + (L_vectorY / amount) + ((L_vectorY / amount) * i), L_elbowPos[2] + (L_vectorZ / amount) + ((L_vectorZ / amount) * i), L_twistLoc)
            cmds.scale(0.05, 0.05, 0.05, L_twistLoc)
            cmds.parent(L_twistLoc, 'SECONDARY')
        

        R_elbowPos = cmds.xform(cmds.ls('Loc_R_elbow'), q = True, t = True, ws = True)
        R_wristPos = cmds.xform(cmds.ls('Loc_R_wrist'), q = True, t = True, ws = True)
        
        R_vectorX = R_wristPos[0] - R_elbowPos[0]
        R_vectorY = R_wristPos[1] - R_elbowPos[1]
        R_vectorZ = R_wristPos[2] - R_elbowPos[2]
        
            
        for j in range(amount - 1):
            
            r_twistLoc = cmds.spaceLocator(n = 'Loc_R_armTwist_' + str(j))
            cmds.move(R_elbowPos[0] + (R_vectorX / amount) + ((R_vectorX / amount) * j), R_elbowPos[1] + (R_vectorY / amount) + ((R_vectorY / amount) * j), R_elbowPos[2] + (R_vectorZ / amount) + ((R_vectorZ / amount) * i), r_twistLoc)
            cmds.scale(0.05, 0.05, 0.05, r_twistLoc)
            cmds.parent(r_twistLoc, 'SECONDARY')
        
        
    def setColors(self, void):
        
        cmds.setAttr('SECONDARY.overrideEnabled', 1)    
        cmds.setAttr('SECONDARY.overrideRGBColors', 1)
        cmds.setAttr('SECONDARY.overrideColorRGB', 1, 1, 1)
        
        
    def deleteSecondary(self, void):
        
        cmds.delete(cmds.ls('SECONDARY'))
