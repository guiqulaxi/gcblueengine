import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2.4kg'
    dbObj.maxRange_m=266.072662
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.842408
    dbObj.fragCharge_kg=0.758394
    dbObj.radCharge_kg=0.084241
    dbObj.fragMetal_kg=0.799197
    dbObj.fragFragment_kg=0.000458
    dbObj.fragSpread=0.300000
    return dbObj
