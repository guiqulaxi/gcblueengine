import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast50kg'
    dbObj.maxRange_m=46.032879
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=50.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=5.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
