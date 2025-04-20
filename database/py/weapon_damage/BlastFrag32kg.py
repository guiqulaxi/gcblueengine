import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag32kg'
    dbObj.maxRange_m=996.662109
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=11.434525
    dbObj.fragCharge_kg=9.976984
    dbObj.radCharge_kg=1.143452
    dbObj.fragMetal_kg=10.588491
    dbObj.fragFragment_kg=0.003276
    dbObj.fragSpread=0.300000
    return dbObj
