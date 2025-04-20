import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir72.5kg'
    dbObj.maxRange_m=3737.236572
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=14.090648
    dbObj.fragCharge_kg=32.656235
    dbObj.radCharge_kg=1.409065
    dbObj.fragMetal_kg=25.753117
    dbObj.fragFragment_kg=0.038153
    dbObj.fragSpread=0.300000
    return dbObj
