import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast2350kg'
    dbObj.maxRange_m=165.911575
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2350.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=235.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
