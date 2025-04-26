# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3600kg'
    dbObj.maxRange_m=11023.752930
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=352.951477
    dbObj.fragCharge_kg=1852.698975
    dbObj.radCharge_kg=35.295147
    dbObj.fragMetal_kg=1394.349487
    dbObj.fragFragment_kg=0.395336
    dbObj.fragSpread=0.300000
    return dbObj
