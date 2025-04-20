import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen180kg'
    dbObj.maxRange_m=62.623089
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=126.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=18.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
