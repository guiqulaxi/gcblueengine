import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen16kg'
    dbObj.maxRange_m=27.970530
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=11.200000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=1.600000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
