import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-135kT'
    dbObj.maxRange_m=17424.492188
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=148500000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=67500000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
