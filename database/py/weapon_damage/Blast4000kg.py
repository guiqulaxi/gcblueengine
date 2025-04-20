import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast4000kg'
    dbObj.maxRange_m=198.060135
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=400.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
