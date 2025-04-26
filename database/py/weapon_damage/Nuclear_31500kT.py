# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-31500kT'
    dbObj.maxRange_m=89444.398438
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=34650001408.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=15749999616.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
