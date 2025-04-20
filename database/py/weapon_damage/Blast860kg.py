import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast860kg'
    dbObj.maxRange_m=118.713219
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=860.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=86.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
