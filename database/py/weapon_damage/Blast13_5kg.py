import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast13.5kg'
    dbObj.maxRange_m=29.765440
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=13.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=1.350000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
