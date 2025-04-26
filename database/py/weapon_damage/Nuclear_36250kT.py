# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-36250kT'
    dbObj.maxRange_m=93293.718750
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=39874998272.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=18125000704.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
