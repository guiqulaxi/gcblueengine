# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis29.5kg'
    dbObj.maxRange_m=3130.643311
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.387655
    dbObj.fragCharge_kg=12.851563
    dbObj.radCharge_kg=0.638765
    dbObj.fragMetal_kg=10.260782
    dbObj.fragFragment_kg=0.026582
    dbObj.fragSpread=0.287415
    return dbObj
