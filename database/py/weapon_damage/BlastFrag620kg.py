import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag620kg'
    dbObj.maxRange_m=3752.108887
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=223.041428
    dbObj.fragCharge_kg=192.305725
    dbObj.radCharge_kg=22.304142
    dbObj.fragMetal_kg=204.652863
    dbObj.fragFragment_kg=0.040865
    dbObj.fragSpread=0.300000
    return dbObj
