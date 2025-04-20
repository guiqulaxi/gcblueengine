import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast27kg'
    dbObj.maxRange_m=37.493431
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=27.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2.700000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
