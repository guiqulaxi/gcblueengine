import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast23.5kg'
    dbObj.maxRange_m=35.799480
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=23.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2.350000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
