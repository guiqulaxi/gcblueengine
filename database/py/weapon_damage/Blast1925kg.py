import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1925kg'
    dbObj.maxRange_m=155.248184
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1925.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=192.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
