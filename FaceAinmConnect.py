# -*- coding: utf-8 -*-
import maya.mel as mel
import pymel.core.general as pcg
import pymel.core.windows as pcw
import pymel.core.system as pcs
import pymel.core.animation as pca
import pymel.core.modeling as pcm
import pymel.core.datatypes as pcdt


class FaceCrt:
    def __init__(self):
        self.FirstGrp = pcg.ls(sl=1)[0]
        #self.BrowR = []
        #self.BrowL = []
        self.FirstGrpChild = pcg.listRelatives(self.FirstGrp,ad=1,type="nurbsCurve")
        self.selectgrp = pcg.ls(sl=1)[1]
        for sel in self.FirstGrpChild:
            #眉毛控制器
            if sel == u"BrowRtMainControlShape":
                self.BrowR = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"BrowLfMainControlShape":
                self.BrowL = pcg.listRelatives(sel,p=1,type="transform")
            #下巴控制器
            if sel == u"JawControlShape":
                self.Jaw = pcg.listRelatives(sel,p=1,type="transform")
            #嘴唇控制器
            if sel == u"LipMainControlShape":
                self.LipMain = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"LipSdkControlShape":
                self.LipSdk = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"LipSdkRtControlShape":
                self.LipSdkRt = pcg.listRelatives(sel,p=1,type="transform")
            #眉毛关节控制器
            if sel == u"BrowRtArcControlShape":
                self.BrowRtArc = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"BrowLfArcControlShape":
                self.BrowLfArc = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"BrowRt05ControlShape":
                self.BrowRt05 = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"BrowLf05ControlShape":
                self.BrowLf05 = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"BrowRt03ControlShape":
                self.BrowRt03 = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"BrowLf03ControlShape":
                self.BrowLf03 = pcg.listRelatives(sel, p=1, type="transform")
            if sel == u"BrowRt02ControlShape":
                self.BrowRt02 = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"BrowLf02ControlShape":
                self.BrowLf02 = pcg.listRelatives(sel,p=1,type="transform")
            #嘴唇控制器
            if sel == u"LipSdkUpControlShape":
                self.LipSdkUp = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"LipSdkDnControlShape":
                self.LipSdkDn = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"LipSdkLfControlShape":
                self.LipSdkLf = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"LipSdkRtControlShape":
                self.LipSdkRt = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"LipSdkLfControlShape":
                self.LipSdkRf = pcg.listRelatives(sel, p=1, type="transform")
            #鼻子控制器
            if sel == u"NoseMainControlShape":
                self.NoseMain = pcg.listRelatives(sel,p=1,type="transform")
            #眼皮控制器
            if sel == u"EyelidRtUpMdControlShape":
                self.EyelidRtUp = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"EyelidLfUpMdControlShape":
                self.EyelidLfUp = pcg.listRelatives(sel,p=1,type="transform")
            if sel == u"EyelidRtUpInControlShape":
                self.EyelidRtUpIn = pcg.listRelatives(sel, p=1, type="transform")
            if sel == u"EyelidLfUpInControlShape":
                self.EyelidLfUpIn = pcg.listRelatives(sel, p=1, type="transform")
            if sel == u"EyelidRtDnMdControlShape":
                self.EyelidRtDn = pcg.listRelatives(sel, p=1, type="transform")
            if sel == u"EyelidLfDnMdControlShape":
                self.EyelidLfDn = pcg.listRelatives(sel, p=1, type="transform")
            if sel == u"EyelidRtUpOtControlShape":
                self.EyelidRtUpOt = pcg.listRelatives(sel, p=1, type="transform")
            if sel == u"EyelidLfUpOtControlShape":
                self.EyelidLfUpOt = pcg.listRelatives(sel, p=1, type="transform")
            if sel == u"EyelidRtDnInControlShape":
                self.EyelidRtDnIn = pcg.listRelatives(sel, p=1, type="transform")
            if sel == u"EyelidLfDnInControlShape":
                self.EyelidLfDnIn = pcg.listRelatives(sel, p=1, type="transform")
            #脸颊控制器
            if sel == u"PufferRtControlShape":
                self.PufferRt = pcg.listRelatives(sel, p=1, type="transform")
            if sel == u"PufferLfControlShape":
                self.PufferLf = pcg.listRelatives(sel, p=1, type="transform")
        #创建新生成列表
            #self.Create()

            #def Create(self):
        self.R_BrowUpper()
        self.R_BrowLower()
        self.R_BrowInner()
        self.R_BrowUpper1()
        self.R_BrowUpper2()
        self.R_BrowUpper3()
        self.R_BrowLower1()
        self.R_BrowLower2()
        self.R_BrowLower3()
        self.R_BrowInner1()
        self.R_BrowInner2()
        self.R_BrowInner3()
        self.R_BrowInner4()
        self.R_LidUpperLower()
        self.R_LidUpperUpper()
        self.R_LidLowerUpper()
        self.R_LidLowerLower()
        self.R_LidInnerLower1()
        self.R_LidInnerUpper1()
        self.R_LidInnerUpper2()
        self.R_LidInnerLower3()
        self.R_Smile()
        self.R_Frown()
        self.R_Wide()
        self.R_Narrow()
        self.R_Cheek()
        self.L_BrowUpper()
        self.L_BrowLower()
        self.L_BrowInner()
        self.L_BrowUpper1()
        self.L_BrowUpper2()
        self.L_BrowUpper3()
        self.L_BrowLower1()
        self.L_BrowLower2()
        self.L_BrowLower3()
        self.L_BrowInner1()
        self.L_BrowInner2()
        self.L_BrowInner3()
        self.L_BrowInner4()
        self.L_LidUpperLower()
        self.L_LidUpperUpper()
        self.L_LidLowerUpper()
        self.L_LidLowerLower()
        self.L_LidInnerLower1()
        self.L_LidInnerUpper1()
        self.L_LidInnerUpper2()
        self.L_LidInnerLower3()
        self.L_Smile()
        self.L_Frown()
        self.L_Wide()
        self.L_Narrow()
        self.L_Cheek()
        self.LipUpperUp()
        self.LipLowerLower()
        self.JawOpen()
        self.JawLeft()
        self.JawRight()
        self.JawRotateRight()
        self.JawRotateLeft()
        self.LipLeft()
        self.LipRight()
        self.LipUp()
        self.LipDn()

        self.NewCreateList = ["R_BrowUpper", "R_BrowLower", "R_BrowInner", "R_BrowUpper1", "R_BrowUpper2",
                              "R_BrowUpper3", "R_BrowLower1", "R_BrowLower2",
                              "R_BrowLower3", "R_BrowInner1", "R_BrowInner2", "R_BrowInner3", "R_BrowInner4",
                              "R_LidUpperLower","R_LidUpperUpper", "R_LidLowerUpper", "R_LidLowerLower","R_LidInnerLower1",
                              "R_LidInnerUpper1", "R_LidInnerUpper2", "R_LidInnerLower3", "R_Smile", "R_Frown",
                              "R_Wide", "R_Narrow", "R_Cheek", "L_BrowUpper", "L_BrowLower", "L_BrowInner",
                              "L_BrowUpper1", "L_BrowUpper2", "L_BrowUpper3", "L_BrowLower1", "L_BrowLower2",
                              "L_BrowLower3", "L_BrowInner1", "L_BrowInner2", "L_BrowInner3", "L_BrowInner4",
                              "L_LidUpperLower","L_LidUpperUpper", "L_LidLowerUpper", "L_LidLowerLower", "L_LidInnerLower1",
                              "L_LidInnerUpper1", "L_LidInnerUpper2", "L_LidInnerLower3", "L_Smile", "L_Frown",
                              "L_Wide", "L_Narrow", "L_Cheek", "LipUpperUp", "LipLowerLower",
                              "JawOpen", "JawLeft", "JawRight", "JawRotateRight", "JawRotateLeft","LipLeft","LipRight",
                              "LipUp","LipDn"]

        x = 4
        count = 0
        for sel in self.NewCreateList:
            x += 2
            pcg.move(sel, (x, -3, 0))
        pca.blendShape(self.NewCreateList, self.selectgrp, n="FaceBS")

        self.Connect()

    def R_BrowUpper(self):
        pcg.setAttr(self.BrowR[0].translate,(0, 0.1, 0))
        pcg.parent(pcg.duplicate(self.selectgrp,n="R_BrowUpper"), w=1)
        pcg.setAttr(self.BrowR[0].translate, (0, 0, 0))

    def R_BrowLower(self):
        pcg.setAttr(self.BrowR[0].translate,(0, -0.1, 0))
        pcg.parent(pcg.duplicate(self.selectgrp,n="R_BrowLower"), w=1)
        pcg.setAttr(self.BrowR[0].translate, (0, 0, 0))

    def R_BrowInner(self):
        pcg.setAttr(self.BrowR[0].translate,(0.1, 0, 0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_BrowInner"), w=1)
        pcg.setAttr(self.BrowR[0].translate, (0, 0, 0))

    def R_BrowUpper1(self):
        pcg.setAttr(self.BrowRtArc[0].translate, (0.1, 0.15 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_BrowUpper1"), w=1)
        pcg.setAttr(self.BrowRtArc[0].translate, (0, 0, 0))

    def R_BrowUpper2(self):
        pcg.setAttr(self.BrowRtArc[0].translate, (0, 0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_BrowUpper2"), w=1)
        pcg.setAttr(self.BrowRtArc[0].translate, (0, 0, 0))

    def R_BrowUpper3(self):
        pcg.setAttr(self.BrowRtArc[0].translate, (-0.1 ,0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_BrowUpper3"), w=1)
        pcg.setAttr(self.BrowRtArc[0].translate, (0, 0, 0))

    def R_BrowLower1(self):
        pcg.setAttr(self.BrowRtArc[0].translate, (0.1 ,-0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_BrowLower1"), w=1)
        pcg.setAttr(self.BrowRtArc[0].translate, (0, 0, 0))

    def R_BrowLower2(self):
        pcg.setAttr(self.BrowRtArc[0].translate, (0 ,-0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_BrowLower2"), w=1)
        pcg.setAttr(self.BrowRtArc[0].translate, (0, 0, 0))

    def R_BrowLower3(self):
        pcg.setAttr(self.BrowRtArc[0].translate, (-0.1 ,-0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_BrowLower3"), w=1)
        pcg.setAttr(self.BrowRtArc[0].translate, (0, 0, 0))

    def R_BrowInner1(self):
        pcg.setAttr(self.BrowRt05[0].translate, (0.1 ,0 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_BrowInner1"), w=1)
        pcg.setAttr(self.BrowRt05[0].translate, (0, 0, 0))

    def R_BrowInner2(self):
        pcg.setAttr(self.BrowRt03[0].translate, (0.1 ,0 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_BrowInner2"), w=1)
        pcg.setAttr(self.BrowRt03[0].translate, (0, 0, 0))

    def R_BrowInner3(self):
        pcg.setAttr(self.BrowRt03[0].translate, (-0.1 ,0 ,0))
        pcg.setAttr(self.BrowRt05[0].translate, (-0.1 ,0 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_BrowInner3"), w=1)
        pcg.setAttr(self.BrowRt03[0].translate, (0, 0, 0))
        pcg.setAttr(self.BrowRt05[0].translate, (0, 0, 0))

    def R_BrowInner4(self):
        pcg.setAttr(self.BrowRt02[0].translate, (0.1 ,0 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_BrowInner4"), w=1)
        pcg.setAttr(self.BrowRt02[0].translate, (0, 0, 0))

    def R_LidUpperLower(self):
        pcg.setAttr(self.EyelidRtUp[0].translate, (0,-0.16,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_LidUpperLower"), w=1)
        pcg.setAttr(self.EyelidRtUp[0].translate, (0, 0, 0))

    def R_LidUpperUpper(self):
        pcg.setAttr(self.EyelidRtUp[0].translate, (0,0.05,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_LidUpperUpper"), w=1)
        pcg.setAttr(self.EyelidRtUp[0].translate, (0, 0, 0))

    def R_LidLowerUpper(self):
        pcg.setAttr(self.EyelidRtDn[0].translate, (0,-0.16,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_LidLowerUpper"), w=1)
        pcg.setAttr(self.EyelidRtDn[0].translate, (0, 0, 0))

    def R_LidLowerLower(self):
        pcg.setAttr(self.EyelidRtDn[0].translate, (0,0.05,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_LidLowerLower"), w=1)
        pcg.setAttr(self.EyelidRtDn[0].translate, (0, 0, 0))

    def R_LidInnerLower1(self):
        pcg.setAttr(self.EyelidRtUpIn[0].translate, (0 ,-0.1 ,0))
        pcg.setAttr(self.EyelidRtUpOt[0].translate, (0,0.02,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_LidInnerLower1"), w=1)
        pcg.setAttr(self.EyelidRtUpIn[0].translate, (0, 0, 0))
        pcg.setAttr(self.EyelidRtUpOt[0].translate, (0, 0, 0))

    def R_LidInnerUpper1(self):
        pcg.setAttr(self.EyelidRtUpOt[0].translate, (0 ,-0.02 ,0))
        pcg.setAttr(self.EyelidRtUpIn[0].translate, (0 ,0.03 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_LidInnerUpper1"), w=1)
        pcg.setAttr(self.EyelidRtUpOt[0].translate, (0, 0, 0))
        pcg.setAttr(self.EyelidRtUpIn[0].translate, (0, 0, 0))

    def R_LidInnerUpper2(self):
        pcg.setAttr(self.EyelidRtDnIn[0].translate, (0 ,-0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_LidInnerUpper2"), w=1)
        pcg.setAttr(self.EyelidRtDnIn[0].translate, (0, 0, 0))

    def R_LidInnerLower3(self):
        pcg.setAttr(self.EyelidRtDnIn[0].translate, (0, 0.03, 0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_LidInnerLower3"), w=1)
        pcg.setAttr(self.EyelidRtDnIn[0].translate, (0, 0, 0))

    def R_Smile(self):
        pcg.setAttr(self.LipSdkRt[0].translateY,  5)
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_Smile"), w=1)
        pcg.setAttr(self.LipSdkRt[0].translateY,  0)

    def R_Frown(self):
        pcg.setAttr(self.LipSdkRt[0].translateY, -5)
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_Frown"), w=1)
        pcg.setAttr(self.LipSdkRt[0].translateY,  0)

    def R_Wide(self):
        pcg.setAttr(self.LipSdkRt[0].translateX, 10)
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_Wide"), w=1)
        pcg.setAttr(self.LipSdkRt[0].translateX, 0)

    def R_Narrow(self):
        pcg.setAttr(self.LipSdkRt[0].translateX, -5)
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_Narrow"), w=1)
        pcg.setAttr(self.LipSdkRt[0].translateX, 0)

    def R_Cheek(self):
        pcg.setAttr(self.PufferRt[0].translate, (-0.3, -0.2, 0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="R_Cheek"), w=1)
        pcg.setAttr(self.PufferRt[0].translate, (0, 0, 0))

    def L_BrowUpper(self):
        pcg.setAttr(self.BrowL[0].translate,(0, 0.1, 0))
        pcg.parent(pcg.duplicate(self.selectgrp,n="L_BrowUpper"), w=1)
        pcg.setAttr(self.BrowL[0].translate, (0, 0, 0))

    def L_BrowLower(self):
        pcg.setAttr(self.BrowL[0].translate,(0, -0.1, 0))
        pcg.parent(pcg.duplicate(self.selectgrp,n="L_BrowLower"), w=1)
        pcg.setAttr(self.BrowL[0].translate, (0, 0, 0))

    def L_BrowInner(self):
        pcg.setAttr(self.BrowL[0].translate,(0.1, 0, 0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_BrowInner"), w=1)
        pcg.setAttr(self.BrowL[0].translate, (0, 0, 0))

    def L_BrowUpper1(self):
        pcg.setAttr(self.BrowLfArc[0].translate, (0.1, 0.15 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_BrowUpper1"), w=1)
        pcg.setAttr(self.BrowLfArc[0].translate, (0, 0, 0))

    def L_BrowUpper2(self):
        pcg.setAttr(self.BrowLfArc[0].translate, (0, 0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_BrowUpper2"), w=1)
        pcg.setAttr(self.BrowLfArc[0].translate, (0, 0, 0))

    def L_BrowUpper3(self):
        pcg.setAttr(self.BrowLfArc[0].translate, (-0.1 ,0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_BrowUpper3"), w=1)
        pcg.setAttr(self.BrowLfArc[0].translate, (0, 0, 0))

    def L_BrowLower1(self):
        pcg.setAttr(self.BrowLfArc[0].translate, (0.1 ,-0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_BrowLower1"), w=1)
        pcg.setAttr(self.BrowLfArc[0].translate, (0, 0, 0))

    def L_BrowLower2(self):
        pcg.setAttr(self.BrowLfArc[0].translate, (0 ,-0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_BrowLower2"), w=1)
        pcg.setAttr(self.BrowLfArc[0].translate, (0, 0, 0))

    def L_BrowLower3(self):
        pcg.setAttr(self.BrowLfArc[0].translate, (-0.1 ,-0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_BrowLower3"), w=1)
        pcg.setAttr(self.BrowLfArc[0].translate, (0, 0, 0))

    def L_BrowInner1(self):
        pcg.setAttr(self.BrowLf05[0].translate, (0.1 ,0 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_BrowInner1"), w=1)
        pcg.setAttr(self.BrowLf05[0].translate, (0, 0, 0))

    def L_BrowInner2(self):
        pcg.setAttr(self.BrowLf03[0].translate, (0.1 ,0 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_BrowInner2"), w=1)
        pcg.setAttr(self.BrowLf03[0].translate, (0, 0, 0))

    def L_BrowInner3(self):
        pcg.setAttr(self.BrowLf03[0].translate, (-0.1 ,0 ,0))
        pcg.setAttr(self.BrowLf05[0].translate, (-0.1 ,0 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_BrowInner3"), w=1)
        pcg.setAttr(self.BrowLf03[0].translate, (0, 0, 0))
        pcg.setAttr(self.BrowLf05[0].translate, (0, 0, 0))

    def L_BrowInner4(self):
        pcg.setAttr(self.BrowLf02[0].translate, (0.1 ,0 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_BrowInner4"), w=1)
        pcg.setAttr(self.BrowLf02[0].translate, (0, 0, 0))

    def L_LidUpperLower(self):
        pcg.setAttr(self.EyelidLfUp[0].translate, (0,-0.16,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_LidUpperLower"), w=1)
        pcg.setAttr(self.EyelidLfUp[0].translate, (0, 0, 0))

    def L_LidUpperUpper(self):
        pcg.setAttr(self.EyelidLfUp[0].translate, (0,0.05,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_LidUpperUpper"), w=1)
        pcg.setAttr(self.EyelidLfUp[0].translate, (0, 0, 0))

    def L_LidLowerUpper(self):
        pcg.setAttr(self.EyelidLfDn[0].translate, (0,-0.16,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_LidLowerUpper"), w=1)
        pcg.setAttr(self.EyelidLfDn[0].translate, (0, 0, 0))

    def L_LidLowerLower(self):
        pcg.setAttr(self.EyelidLfDn[0].translate, (0,0.05,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_LidLowerLower"), w=1)
        pcg.setAttr(self.EyelidLfDn[0].translate, (0, 0, 0))

    def L_LidInnerLower1(self):
        pcg.setAttr(self.EyelidLfUpIn[0].translate, (0 ,-0.1 ,0))
        pcg.setAttr(self.EyelidLfUpOt[0].translate, (0,0.02,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_LidInnerLower1"), w=1)
        pcg.setAttr(self.EyelidLfUpIn[0].translate, (0, 0, 0))
        pcg.setAttr(self.EyelidLfUpOt[0].translate, (0, 0, 0))

    def L_LidInnerUpper1(self):
        pcg.setAttr(self.EyelidLfUpOt[0].translate, (0 ,-0.02 ,0))
        pcg.setAttr(self.EyelidLfUpIn[0].translate, (0 ,0.03 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_LidInnerUpper1"), w=1)
        pcg.setAttr(self.EyelidLfUpOt[0].translate, (0, 0, 0))
        pcg.setAttr(self.EyelidLfUpIn[0].translate, (0, 0, 0))

    def L_LidInnerUpper2(self):
        pcg.setAttr(self.EyelidLfDnIn[0].translate, (0 ,-0.1 ,0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_LidInnerUpper2"), w=1)
        pcg.setAttr(self.EyelidLfDnIn[0].translate, (0, 0, 0))

    def L_LidInnerLower3(self):
        pcg.setAttr(self.EyelidLfDnIn[0].translate, (0, 0.03, 0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_LidInnerLower3"), w=1)
        pcg.setAttr(self.EyelidLfDnIn[0].translate, (0, 0, 0))

    def L_Smile(self):
        pcg.setAttr(self.LipSdkLf[0].translateY,  5)
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_Smile"), w=1)
        pcg.setAttr(self.LipSdkLf[0].translateY,  0)

    def L_Frown(self):
        pcg.setAttr(self.LipSdkLf[0].translateY, -5)
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_Frown"), w=1)
        pcg.setAttr(self.LipSdkLf[0].translateY,  0)

    def L_Wide(self):
        pcg.setAttr(self.LipSdkLf[0].translateX, 10)
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_Wide"), w=1)
        pcg.setAttr(self.LipSdkLf[0].translateX, 0)

    def L_Narrow(self):
        pcg.setAttr(self.LipSdkLf[0].translateX, -5)
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_Narrow"), w=1)
        pcg.setAttr(self.LipSdkLf[0].translateX, 0)

    def L_Cheek(self):
        pcg.setAttr(self.PufferLf[0].translate, (-0.3, -0.2, 0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="L_Cheek"), w=1)
        pcg.setAttr(self.PufferLf[0].translate, (0, 0, 0))

    def LipUpperUp(self):
        pcg.setAttr(self.LipSdkUp[0].translate, (0, 5, 0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="LipUpperUp"), w=1)
        pcg.setAttr(self.LipSdkUp[0].translate, (0, 0, 0))

    def LipLowerLower(self):
        pcg.setAttr(self.LipSdkDn[0].translate, (0, 5, 0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="LipLowerLower"), w=1)
        pcg.setAttr(self.LipSdkDn[0].translate, (0, 0, 0))

    def JawOpen(self):
        pcg.setAttr(self.Jaw[0].translate, (0, -0.25, 0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="JawOpen"), w=1)
        pcg.setAttr(self.Jaw[0].translate, (0, 0, 0))

    def JawLeft(self):
        pcg.setAttr(self.Jaw[0].translate, (0.1, 0, 0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="JawLeft"), w=1)
        pcg.setAttr(self.Jaw[0].translate, (0, 0, 0))

    def JawRight(self):
        pcg.setAttr(self.Jaw[0].translate, (-0.1, 0, 0))
        pcg.parent(pcg.duplicate(self.selectgrp, n="JawRight"), w=1)
        pcg.setAttr(self.Jaw[0].translate, (0, 0, 0))

    def JawRotateRight(self):
        pcg.setAttr(self.Jaw[0].rotateZ, 10)
        pcg.parent(pcg.duplicate(self.selectgrp, n="JawRotateRight"), w=1)
        pcg.setAttr(self.Jaw[0].rotateZ,  0)

    def JawRotateLeft(self):
        pcg.setAttr(self.Jaw[0].rotateZ, -10)
        pcg.parent(pcg.duplicate(self.selectgrp, n="JawRotateLeft"), w=1)
        pcg.setAttr(self.Jaw[0].rotateZ,  0)

    def LipLeft(self):
        pcg.setAttr(self.LipMain[0].translateX, 0.08)
        pcg.parent(pcg.duplicate(self.selectgrp, n="LipLeft"), w=1)
        pcg.setAttr(self.LipMain[0].translateX, 0)

    def LipRight(self):
        pcg.setAttr(self.LipMain[0].translateX, -0.08)
        pcg.parent(pcg.duplicate(self.selectgrp, n="LipRight"), w=1)
        pcg.setAttr(self.LipMain[0].translateX, 0)

    def LipUp(self):
        pcg.setAttr(self.LipMain[0].translateY, 0.08)
        pcg.parent(pcg.duplicate(self.selectgrp, n="LipUp"), w=1)
        pcg.setAttr(self.LipSdk[0].translateY, 0)

    def LipDn(self):
        pcg.setAttr(self.LipMain[0].translateY, -0.08)
        pcg.parent(pcg.duplicate(self.selectgrp, n="LipDn"), w=1)
        pcg.setAttr(self.LipMain[0].translateY, 0)

    def Connect(self):
        pca.setDrivenKeyframe('FaceBS.JawOpen', cd='Jaw_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.JawOpen', cd='Jaw_ctrl.translateY', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.JawLeft', cd='Jaw_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.JawLeft', cd='Jaw_ctrl.translateX', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.JawRight', cd='Jaw_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.JawRight', cd='Jaw_ctrl.translateX', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.JawRotateLeft', cd='Jaw_ctrl.rotateZ', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.JawRotateLeft', cd='Jaw_ctrl.rotateZ', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.JawRotateRight', cd='Jaw_ctrl.rotateZ', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.JawRotateRight', cd='Jaw_ctrl.rotateZ', v=1, dv=1)

        pca.setDrivenKeyframe('FaceBS.L_Cheek', cd='L_Cheek_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_Cheek', cd='L_Cheek_ctrl.translateX', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.R_Cheek', cd='R_Cheek_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_Cheek', cd='R_Cheek_ctrl.translateX', v=1, dv=1)

        pca.setDrivenKeyframe('FaceBS.LipUpperUp', cd='Up_Mouth_Con_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.LipUpperUp', cd='Up_Mouth_Con_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.LipLowerLower', cd='Dn_Mouth_Con_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.LipLowerLower', cd='Dn_Mouth_Con_ctrl.translateY', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.L_Smile', cd='L_Mouth_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_Smile', cd='L_Mouth_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.L_Frown', cd='L_Mouth_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_Frown', cd='L_Mouth_ctrl.translateY', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.L_Wide', cd='L_Mouth_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_Wide', cd='L_Mouth_ctrl.translateX', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.L_Narrow', cd='L_Mouth_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_Narrow', cd='L_Mouth_ctrl.translateX', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.R_Smile', cd='R_Mouth_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_Smile', cd='R_Mouth_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.R_Frown', cd='R_Mouth_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_Frown', cd='R_Mouth_ctrl.translateY', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.R_Wide', cd='R_Mouth_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_Wide', cd='R_Mouth_ctrl.translateX', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.R_Narrow', cd='R_Mouth_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_Narrow', cd='R_Mouth_ctrl.translateX', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.R_BrowUpper', cd='R_Brown_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowUpper', cd='R_Brown_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.R_BrowLower', cd='R_Brown_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowLower', cd='R_Brown_ctrl.translateY', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.R_BrowInner', cd='R_Brown_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowInner', cd='R_Brown_ctrl.translateX', v=1, dv=-1)

        # 眉毛
        pca.setDrivenKeyframe('FaceBS.R_BrowUpper1', cd='R_BrowInn_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowUpper1', cd='R_BrowInn_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.R_BrowInner1', cd='R_BrowInn_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowInner1', cd='R_BrowInn_ctrl.translateX', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.R_BrowUpper2', cd='R_BrowMid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowUpper2', cd='R_BrowMid_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.R_BrowInner2', cd='R_BrowMid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowInner2', cd='R_BrowMid_ctrl.translateX', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.R_BrowInner3', cd='R_BrowMid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowInner3', cd='R_BrowMid_ctrl.translateX', v=1, dv=1)

        pca.setDrivenKeyframe('FaceBS.R_BrowUpper3', cd='R_BrowOut_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowUpper3', cd='R_BrowOut_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.R_BrowInner4', cd='R_BrowOut_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowInner4', cd='R_BrowOut_ctrl.translateX', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.R_BrowLower1', cd='R_BrowInn_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowLower1', cd='R_BrowInn_ctrl.translateY', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.R_BrowLower2', cd='R_BrowMid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowLower2', cd='R_BrowMid_ctrl.translateY', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.R_BrowLower3', cd='R_BrowOut_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_BrowLower3', cd='R_BrowOut_ctrl.translateY', v=1, dv=-1)
        # 上眼皮
        pca.setDrivenKeyframe('FaceBS.R_LidUpperLower', cd='R_UpEyelid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_LidUpperLower', cd='R_UpEyelid_ctrl.translateY', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.R_LidUpperUpper', cd='R_UpEyelid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_LidUpperUpper', cd='R_UpEyelid_ctrl.translateY', v=1, dv=1)

        pca.setDrivenKeyframe('FaceBS.R_LidInnerUpper1', cd='R_UpEyelid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_LidInnerUpper1', cd='R_UpEyelid_ctrl.translateX', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.R_LidInnerLower1', cd='R_UpEyelid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_LidInnerLower1', cd='R_UpEyelid_ctrl.translateX', v=1, dv=-1)
        # 下眼皮
        pca.setDrivenKeyframe('FaceBS.R_LidLowerUpper', cd='R_LowEyelid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_LidLowerUpper', cd='R_LowEyelid_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.R_LidLowerLower', cd='R_LowEyelid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_LidLowerLower', cd='R_LowEyelid_ctrl.translateY', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.R_LidInnerUpper2', cd='R_LowEyelid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_LidInnerUpper2', cd='R_LowEyelid_ctrl.translateX', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.R_LidInnerLower3', cd='R_LowEyelid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.R_LidInnerLower3', cd='R_LowEyelid_ctrl.translateX', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.L_BrowUpper', cd='L_Brown_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowUpper', cd='L_Brown_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.L_BrowLower', cd='L_Brown_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowLower', cd='L_Brown_ctrl.translateY', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.L_BrowInner', cd='L_Brown_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowInner', cd='L_Brown_ctrl.translateX', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.L_BrowUpper1', cd='L_BrowInn_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowUpper1', cd='L_BrowInn_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.L_BrowInner1', cd='L_BrowInn_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowInner1', cd='L_BrowInn_ctrl.translateX', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.L_BrowUpper2', cd='L_BrowMid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowUpper2', cd='L_BrowMid_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.L_BrowInner2', cd='L_BrowMid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowInner2', cd='L_BrowMid_ctrl.translateX', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.L_BrowInner3', cd='L_BrowMid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowInner3', cd='L_BrowMid_ctrl.translateX', v=1, dv=1)

        pca.setDrivenKeyframe('FaceBS.L_BrowUpper3', cd='L_BrowOut_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowUpper3', cd='L_BrowOut_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.L_BrowInner4', cd='L_BrowOut_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowInner4', cd='L_BrowOut_ctrl.translateX', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.L_BrowLower1', cd='L_BrowInn_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowLower1', cd='L_BrowInn_ctrl.translateY', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.L_BrowLower2', cd='L_BrowMid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowLower2', cd='L_BrowMid_ctrl.translateY', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.L_BrowLower3', cd='L_BrowOut_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_BrowLower3', cd='L_BrowOut_ctrl.translateY', v=1, dv=-1)
        # 上眼皮
        pca.setDrivenKeyframe('FaceBS.L_LidUpperLower', cd='L_UpEyelid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_LidUpperLower', cd='L_UpEyelid_ctrl.translateY', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.L_LidUpperUpper', cd='L_UpEyelid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_LidUpperUpper', cd='L_UpEyelid_ctrl.translateY', v=1, dv=1)

        pca.setDrivenKeyframe('FaceBS.L_LidInnerUpper1', cd='L_UpEyelid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_LidInnerUpper1', cd='L_UpEyelid_ctrl.translateX', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.L_LidInnerLower1', cd='L_UpEyelid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_LidInnerLower1', cd='L_UpEyelid_ctrl.translateX', v=1, dv=-1)
        # 下眼皮
        pca.setDrivenKeyframe('FaceBS.L_LidLowerUpper', cd='L_LowEyelid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_LidLowerUpper', cd='L_LowEyelid_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.L_LidLowerLower', cd='L_LowEyelid_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_LidLowerLower', cd='L_LowEyelid_ctrl.translateY', v=1, dv=-1)

        pca.setDrivenKeyframe('FaceBS.L_LidInnerUpper2', cd='L_LowEyelid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_LidInnerUpper2', cd='L_LowEyelid_ctrl.translateX', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.L_LidInnerLower3', cd='L_LowEyelid_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.L_LidInnerLower3', cd='L_LowEyelid_ctrl.translateX', v=1, dv=-1)
        # 嘴巴总控
        pca.setDrivenKeyframe('FaceBS.LipLeft', cd='C_Mouth_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.LipLeft', cd='C_Mouth_ctrl.translateX', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.LipRight', cd='C_Mouth_ctrl.translateX', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.LipRight', cd='C_Mouth_ctrl.translateX', v=1, dv=-1)
        pca.setDrivenKeyframe('FaceBS.LipUp', cd='C_Mouth_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.LipUp', cd='C_Mouth_ctrl.translateY', v=1, dv=1)
        pca.setDrivenKeyframe('FaceBS.LipDn', cd='C_Mouth_ctrl.translateY', v=0, dv=0)
        pca.setDrivenKeyframe('FaceBS.LipDn', cd='C_Mouth_ctrl.translateY', v=1, dv=-1)


a=FaceCrt()
