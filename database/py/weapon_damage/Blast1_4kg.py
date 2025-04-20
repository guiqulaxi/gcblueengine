import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1.4kg'
    dbObj.maxRange_m=13.994960
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.400000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.140000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
