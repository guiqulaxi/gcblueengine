import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3000kg'
    dbObj.maxRange_m=10344.865234
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=307.616028
    dbObj.fragCharge_kg=1534.922607
    dbObj.radCharge_kg=30.761604
    dbObj.fragMetal_kg=1157.461304
    dbObj.fragFragment_kg=0.342748
    dbObj.fragSpread=0.300000
    return dbObj
