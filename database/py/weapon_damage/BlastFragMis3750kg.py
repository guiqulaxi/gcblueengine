import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3750kg'
    dbObj.maxRange_m=11177.864258
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=363.882294
    dbObj.fragCharge_kg=1932.411743
    dbObj.radCharge_kg=36.388229
    dbObj.fragMetal_kg=1453.705933
    dbObj.fragFragment_kg=0.407886
    dbObj.fragSpread=0.300000
    return dbObj
