import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-37250kT'
    dbObj.maxRange_m=94058.460938
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=40974999552.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=18624999424.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
