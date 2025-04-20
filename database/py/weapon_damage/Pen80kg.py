import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen80kg'
    dbObj.maxRange_m=47.803280
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=56.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=8.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
