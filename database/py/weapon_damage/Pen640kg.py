import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen640kg'
    dbObj.maxRange_m=95.540321
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=448.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=64.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
