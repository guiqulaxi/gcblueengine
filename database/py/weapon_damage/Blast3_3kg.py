import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast3.3kg'
    dbObj.maxRange_m=18.619850
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.300000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.330000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
