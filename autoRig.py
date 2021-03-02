import maya.cmds as cmds
import createJoints
import createLocators
import createSecondaryWindow
import controllers
import constraints

#reloading
createLocators = reload(createLocators)
createJoints = reload(createJoints)
createSecondaryWindow = reload(createSecondaryWindow)
controllers = reload(controllers)
constraints = reload(constraints)

#global declarations
global selected
global prefix

class autoRig():
    
    
    def __init__(self):
        self.buildUI()
        
        
    def buildUI(self):
        
        #creating window

        cmds.window("Auto Rig", h = 500, w = 200, rtf = True, title = 'BIPED RIG GENERATOR', titleBar = True)

        cmds.rowColumnLayout(adj = True)

        cmds.image(i = "/Users/abhishekravi/Desktop/NEWMAYAWORK/Header.png")
        cmds.separator(h = 10)
        self.spineCount = cmds.intSliderGrp(l = "Spine Count", min = 1, max = 10, value = 4, step = 1, field = True)
        self.fingerCount = cmds.intSliderGrp(l = "Finger Count", min = 1, max = 10, value = 5, step = 1, field = True)
        cmds.separator(h = 10)        
        cmds.separator(h = 10)
        cmds.button(l = "Create Base Locators", w = 100, c = self.startLocators)
        cmds.separator(st = 'single', h = 10)
        cmds.button(l = "Mirror Locators L->R", w = 100, c = "createLocators.mirrorLocators()")
        cmds.separator(st = 'single', h = 10)
        cmds.button(l = "Secondary Locators", w = 100, c = "createSecondaryWindow.secLocators()")
        cmds.separator(st = 'single', h = 10)
        cmds.button(l = "Joints", w = 200, c = "createJoints.createJointsWindow()")
        cmds.separator(st = 'single', h = 10)
        cmds.button(l = "Create Controllers", w = 100, c = self.startControllers)
        cmds.separator(st = 'single', h = 10)
        cmds.button(l = "Create Constraints", w = 100, c = self.startConstraints)
        cmds.separator(st = 'single', h = 10)
        cmds.button(l = "Delete All Locators", w = 100, c = "createLocators.deleteLocators()")
        cmds.separator(st = 'single', h = 10)
        cmds.button(l = "Bind skin", w = 100, c = "constraints.BindSkin()")

        cmds.showWindow()

    def startLocators(self, void):

        _spineCount = cmds.intSliderGrp(self.spineCount, q = True, v = True)
        _fingerCount = cmds.intSliderGrp(self.fingerCount, q = True, v =True)
        createLocators.createLocators(_spineCount, _fingerCount)

    def startControllers(self, void):

        _spineCount = cmds.intSliderGrp(self.spineCount, q = True, v = True)
        _fingerCount = cmds.intSliderGrp(self.fingerCount, q = True, v =True)
        controllers.createControllers(_spineCount, _fingerCount)

    def startConstraints(self, void):

        _spineCount = cmds.intSliderGrp(self.spineCount, q = True, v = True)
        _fingerCount = cmds.intSliderGrp(self.fingerCount, q = True, v =True)
        constraints.createConstraints(_spineCount, _fingerCount)