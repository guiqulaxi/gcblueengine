import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen2250kg'
    dbObj.maxRange_m=145.213013
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1575.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=225.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
