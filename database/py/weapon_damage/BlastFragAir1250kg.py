import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1250kg'
    dbObj.maxRange_m=7356.644043
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=155.162994
    dbObj.fragCharge_kg=621.557983
    dbObj.radCharge_kg=15.516299
    dbObj.fragMetal_kg=473.278992
    dbObj.fragFragment_kg=0.161034
    dbObj.fragSpread=0.300000
    return dbObj
