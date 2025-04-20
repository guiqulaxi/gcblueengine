import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1425kg'
    dbObj.maxRange_m=140.453140
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1425.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=142.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
