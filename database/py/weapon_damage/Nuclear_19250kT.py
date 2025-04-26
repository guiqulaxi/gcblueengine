# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-19250kT'
    dbObj.maxRange_m=77159.468750
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=21174999040.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=9624999936.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
