import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen260kg'
    dbObj.maxRange_m=70.780701
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=182.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=26.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
