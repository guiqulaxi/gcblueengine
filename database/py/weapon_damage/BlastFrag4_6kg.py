import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag4.6kg'
    dbObj.maxRange_m=380.415283
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.618363
    dbObj.fragCharge_kg=1.451091
    dbObj.radCharge_kg=0.161836
    dbObj.fragMetal_kg=1.530546
    dbObj.fragFragment_kg=0.000730
    dbObj.fragSpread=0.300000
    return dbObj
