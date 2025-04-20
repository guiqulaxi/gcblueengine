import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen325kg'
    dbObj.maxRange_m=76.240532
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=227.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=32.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
