import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2.7kg'
    dbObj.maxRange_m=286.228973
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.947503
    dbObj.fragCharge_kg=0.853331
    dbObj.radCharge_kg=0.094750
    dbObj.fragMetal_kg=0.899166
    dbObj.fragFragment_kg=0.000502
    dbObj.fragSpread=0.300000
    return dbObj
