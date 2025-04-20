import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast115kg'
    dbObj.maxRange_m=60.746811
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=115.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=11.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
