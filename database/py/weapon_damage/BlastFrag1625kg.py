# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1625kg'
    dbObj.maxRange_m=5548.382812
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=584.817688
    dbObj.fragCharge_kg=503.871552
    dbObj.radCharge_kg=58.481766
    dbObj.fragMetal_kg=536.310791
    dbObj.fragFragment_kg=0.092852
    dbObj.fragSpread=0.300000
    return dbObj
