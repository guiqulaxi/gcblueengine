import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1125kg'
    dbObj.maxRange_m=7037.204590
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=142.570023
    dbObj.fragCharge_kg=557.453308
    dbObj.radCharge_kg=14.257002
    dbObj.fragMetal_kg=424.976654
    dbObj.fragFragment_kg=0.146141
    dbObj.fragSpread=0.300000
    return dbObj
