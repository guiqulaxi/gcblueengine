import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag345kg'
    dbObj.maxRange_m=2925.414551
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=124.055878
    dbObj.fragCharge_kg=107.046082
    dbObj.radCharge_kg=12.405588
    dbObj.fragMetal_kg=113.898041
    dbObj.fragFragment_kg=0.024632
    dbObj.fragSpread=0.300000
    return dbObj
