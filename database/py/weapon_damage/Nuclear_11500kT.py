import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-11500kT'
    dbObj.maxRange_m=66110.335938
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=12650000384.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=5750000128.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
