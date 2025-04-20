import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-37750kT'
    dbObj.maxRange_m=94435.453125
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=41524998144.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=18875000832.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
