# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag12.5kg'
    dbObj.maxRange_m=638.416504
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.437708
    dbObj.fragCharge_kg=3.916528
    dbObj.radCharge_kg=0.443771
    dbObj.fragMetal_kg=4.145764
    dbObj.fragFragment_kg=0.001570
    dbObj.fragSpread=0.300000
    return dbObj
