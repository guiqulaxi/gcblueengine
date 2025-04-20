import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-37000kT'
    dbObj.maxRange_m=93868.632812
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=40699998208.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=18499999744.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
