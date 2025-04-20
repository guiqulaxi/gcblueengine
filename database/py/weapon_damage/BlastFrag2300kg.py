import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2300kg'
    dbObj.maxRange_m=6353.488770
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=827.809082
    dbObj.fragCharge_kg=713.127258
    dbObj.radCharge_kg=82.780907
    dbObj.fragMetal_kg=759.063660
    dbObj.fragFragment_kg=0.124192
    dbObj.fragSpread=0.300000
    return dbObj
