import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast34kg'
    dbObj.maxRange_m=40.484951
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=34.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=3.400000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
