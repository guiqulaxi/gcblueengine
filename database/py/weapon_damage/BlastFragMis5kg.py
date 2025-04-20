import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis5kg'
    dbObj.maxRange_m=1778.333618
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.301532
    dbObj.fragCharge_kg=2.032312
    dbObj.radCharge_kg=0.130153
    dbObj.fragMetal_kg=1.666156
    dbObj.fragFragment_kg=0.008769
    dbObj.fragSpread=0.069637
    return dbObj
