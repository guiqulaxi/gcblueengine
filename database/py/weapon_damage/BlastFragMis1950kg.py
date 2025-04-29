# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1950kg'
    dbObj.maxRange_m=8806.605469
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=220.668030
    dbObj.fragCharge_kg=983.888000
    dbObj.radCharge_kg=22.066803
    dbObj.fragMetal_kg=745.443970
    dbObj.fragFragment_kg=0.239385
    dbObj.fragSpread=0.300000
    return dbObj
