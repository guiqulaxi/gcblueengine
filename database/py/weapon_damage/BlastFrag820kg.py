import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag820kg'
    dbObj.maxRange_m=4216.843262
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=295.034515
    dbObj.fragCharge_kg=254.310318
    dbObj.radCharge_kg=29.503452
    dbObj.fragMetal_kg=270.655151
    dbObj.fragFragment_kg=0.052049
    dbObj.fragSpread=0.300000
    return dbObj
