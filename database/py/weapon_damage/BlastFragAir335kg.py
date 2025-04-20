import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir335kg'
    dbObj.maxRange_m=4895.828613
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=52.462975
    dbObj.fragCharge_kg=159.324677
    dbObj.radCharge_kg=5.246297
    dbObj.fragMetal_kg=123.212341
    dbObj.fragFragment_kg=0.067000
    dbObj.fragSpread=0.300000
    return dbObj
