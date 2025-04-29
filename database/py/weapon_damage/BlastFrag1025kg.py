# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1025kg'
    dbObj.maxRange_m=4610.835449
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=368.829010
    dbObj.fragCharge_kg=317.863983
    dbObj.radCharge_kg=36.882904
    dbObj.fragMetal_kg=338.307007
    dbObj.fragFragment_kg=0.062742
    dbObj.fragSpread=0.300000
    return dbObj
