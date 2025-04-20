import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag22kg'
    dbObj.maxRange_m=844.813660
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.843766
    dbObj.fragCharge_kg=6.870823
    dbObj.radCharge_kg=0.784377
    dbObj.fragMetal_kg=7.285411
    dbObj.fragFragment_kg=0.002475
    dbObj.fragSpread=0.300000
    return dbObj
