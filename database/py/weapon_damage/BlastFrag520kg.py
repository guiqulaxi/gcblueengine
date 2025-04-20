import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag520kg'
    dbObj.maxRange_m=3476.620850
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=187.045761
    dbObj.fragCharge_kg=161.302826
    dbObj.radCharge_kg=18.704576
    dbObj.fragMetal_kg=171.651413
    dbObj.fragFragment_kg=0.034945
    dbObj.fragSpread=0.300000
    return dbObj
