import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen3100kg'
    dbObj.maxRange_m=161.566818
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2170.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=310.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
