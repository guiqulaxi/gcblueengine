import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen1500kg'
    dbObj.maxRange_m=126.872391
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1050.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=150.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
