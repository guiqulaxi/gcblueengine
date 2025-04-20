import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen90kg'
    dbObj.maxRange_m=49.715462
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=63.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=9.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
