import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-11250kT'
    dbObj.maxRange_m=65675.859375
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=12375000064.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=5624999936.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
