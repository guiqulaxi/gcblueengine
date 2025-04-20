import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast2.4kg'
    dbObj.maxRange_m=16.746401
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.400000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.240000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
