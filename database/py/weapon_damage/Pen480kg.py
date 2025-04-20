import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen480kg'
    dbObj.maxRange_m=86.812462
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=336.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=48.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
