# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK180'
    dbObj.xSpeed_kts=[0.000000,4.298000,15.043000,21.490000]
    dbObj.ySL_dB=[84.970001,89.150734,118.415878,126.777351]
    dbObj.speedMinNL_kts=9.660000
    dbObj.NL_min=48.000000
    dbObj.speedMaxNL_kts=21.490000
    dbObj.NL_max=91.800003
    dbObj.cavitationOffset_kts=13.800000
    dbObj.cavitationSlope_ktsperft=0.009850
    dbObj.cavitationSL_dB=144.777344
    dbObj.snorkelingSL_dB=138.777344
    dbObj.BuildSLTable()
    return dbObj