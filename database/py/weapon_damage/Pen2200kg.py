import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen2200kg'
    dbObj.maxRange_m=144.130371
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1540.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=220.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
