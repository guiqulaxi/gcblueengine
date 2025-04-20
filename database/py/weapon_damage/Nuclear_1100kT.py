import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-1100kT'
    dbObj.maxRange_m=32694.732422
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=1210000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=550000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
