import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1.5kg'
    dbObj.maxRange_m=14.320210
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.150000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
