import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis4.9kg'
    dbObj.maxRange_m=1763.897095
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.277943
    dbObj.fragCharge_kg=1.990038
    dbObj.radCharge_kg=0.127794
    dbObj.fragMetal_kg=1.632019
    dbObj.fragFragment_kg=0.008635
    dbObj.fragSpread=0.068906
    return dbObj
