import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2.6kg'
    dbObj.maxRange_m=279.730255
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.912434
    dbObj.fragCharge_kg=0.821711
    dbObj.radCharge_kg=0.091243
    dbObj.fragMetal_kg=0.865855
    dbObj.fragFragment_kg=0.000488
    dbObj.fragSpread=0.300000
    return dbObj
