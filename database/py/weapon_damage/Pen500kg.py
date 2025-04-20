import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen500kg'
    dbObj.maxRange_m=88.000618
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=350.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=50.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
