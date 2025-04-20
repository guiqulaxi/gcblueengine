import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen460kg'
    dbObj.maxRange_m=85.590797
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=322.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=46.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
