# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2200kg'
    dbObj.maxRange_m=6239.046875
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=791.810181
    dbObj.fragCharge_kg=682.126526
    dbObj.radCharge_kg=79.181015
    dbObj.fragMetal_kg=726.063293
    dbObj.fragFragment_kg=0.119418
    dbObj.fragSpread=0.300000
    return dbObj
