import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir33kg'
    dbObj.maxRange_m=3200.626953
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.054262
    dbObj.fragCharge_kg=14.437159
    dbObj.radCharge_kg=0.705426
    dbObj.fragMetal_kg=11.508579
    dbObj.fragFragment_kg=0.027799
    dbObj.fragSpread=0.300000
    return dbObj
