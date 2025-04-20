import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis18kg'
    dbObj.maxRange_m=2787.336914
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.116864
    dbObj.fragCharge_kg=7.695424
    dbObj.radCharge_kg=0.411686
    dbObj.fragMetal_kg=6.187712
    dbObj.fragFragment_kg=0.021047
    dbObj.fragSpread=0.166736
    return dbObj
