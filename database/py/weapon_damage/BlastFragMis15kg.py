import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis15kg'
    dbObj.maxRange_m=2648.919678
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.498169
    dbObj.fragCharge_kg=6.367887
    dbObj.radCharge_kg=0.349817
    dbObj.fragMetal_kg=5.133944
    dbObj.fragFragment_kg=0.019015
    dbObj.fragSpread=0.140625
    return dbObj
