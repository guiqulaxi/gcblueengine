import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-3100kT'
    dbObj.maxRange_m=44613.726562
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=3409999872.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=1550000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
