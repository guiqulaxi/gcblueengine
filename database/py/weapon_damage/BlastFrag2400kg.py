# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2400kg'
    dbObj.maxRange_m=6464.281738
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=863.808044
    dbObj.fragCharge_kg=744.127991
    dbObj.radCharge_kg=86.380806
    dbObj.fragMetal_kg=792.063965
    dbObj.fragFragment_kg=0.128917
    dbObj.fragSpread=0.300000
    return dbObj
