import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen24kg'
    dbObj.maxRange_m=32.013939
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=16.799999
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2.400000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
