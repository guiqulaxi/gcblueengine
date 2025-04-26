# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2.6kg'
    dbObj.maxRange_m=1315.425415
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.718729
    dbObj.fragCharge_kg=1.028847
    dbObj.radCharge_kg=0.071873
    dbObj.fragMetal_kg=0.852424
    dbObj.fragFragment_kg=0.005014
    dbObj.fragSpread=0.055748
    return dbObj
