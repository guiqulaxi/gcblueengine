import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3550kg'
    dbObj.maxRange_m=7535.358398
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1277.798340
    dbObj.fragCharge_kg=1100.634399
    dbObj.radCharge_kg=127.779839
    dbObj.fragMetal_kg=1171.567261
    dbObj.fragFragment_kg=0.179909
    dbObj.fragSpread=0.300000
    return dbObj
