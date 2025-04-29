# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1675kg'
    dbObj.maxRange_m=8293.373047
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=195.828064
    dbObj.fragCharge_kg=840.947937
    dbObj.radCharge_kg=19.582806
    dbObj.fragMetal_kg=638.223999
    dbObj.fragFragment_kg=0.209597
    dbObj.fragSpread=0.300000
    return dbObj
