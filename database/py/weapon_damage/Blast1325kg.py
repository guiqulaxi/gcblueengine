import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1325kg'
    dbObj.maxRange_m=137.091003
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1325.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=132.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
