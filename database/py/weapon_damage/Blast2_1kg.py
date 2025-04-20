import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast2.1kg'
    dbObj.maxRange_m=16.018070
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.100000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.210000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
