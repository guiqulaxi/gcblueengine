import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen385kg'
    dbObj.maxRange_m=80.665382
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=269.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=38.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
