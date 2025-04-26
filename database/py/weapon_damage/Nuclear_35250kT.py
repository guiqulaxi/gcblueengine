# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-35250kT'
    dbObj.maxRange_m=92514.054688
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=38775001088.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=17624999936.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
