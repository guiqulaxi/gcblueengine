import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag4.1kg'
    dbObj.maxRange_m=359.885101
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.441201
    dbObj.fragCharge_kg=1.294199
    dbObj.radCharge_kg=0.144120
    dbObj.fragMetal_kg=1.364600
    dbObj.fragFragment_kg=0.000677
    dbObj.fragSpread=0.300000
    return dbObj
