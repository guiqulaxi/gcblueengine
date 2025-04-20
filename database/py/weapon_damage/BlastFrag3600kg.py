import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3600kg'
    dbObj.maxRange_m=7575.197754
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1295.798096
    dbObj.fragCharge_kg=1116.134644
    dbObj.radCharge_kg=129.579803
    dbObj.fragMetal_kg=1188.067261
    dbObj.fragFragment_kg=0.181996
    dbObj.fragSpread=0.300000
    return dbObj
