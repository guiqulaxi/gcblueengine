import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3250kg'
    dbObj.maxRange_m=10642.145508
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=326.834900
    dbObj.fragCharge_kg=1667.110107
    dbObj.radCharge_kg=32.683491
    dbObj.fragMetal_kg=1256.055054
    dbObj.fragFragment_kg=0.365238
    dbObj.fragSpread=0.300000
    return dbObj
