import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast7.6kg'
    dbObj.maxRange_m=24.582270
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.600000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.760000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
