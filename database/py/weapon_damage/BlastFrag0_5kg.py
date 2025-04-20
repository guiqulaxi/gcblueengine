import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag0.5kg'
    dbObj.maxRange_m=133.612564
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.180000
    dbObj.fragCharge_kg=0.155000
    dbObj.radCharge_kg=0.018000
    dbObj.fragMetal_kg=0.165000
    dbObj.fragFragment_kg=0.000219
    dbObj.fragSpread=0.300000
    return dbObj
