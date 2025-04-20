import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-26250kT'
    dbObj.maxRange_m=84683.500000
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=28874999808.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=13125000192.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
