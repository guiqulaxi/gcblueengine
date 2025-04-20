import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir230kg'
    dbObj.maxRange_m=4455.416992
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=38.152508
    dbObj.fragCharge_kg=107.964996
    dbObj.radCharge_kg=3.815251
    dbObj.fragMetal_kg=83.882500
    dbObj.fragFragment_kg=0.054933
    dbObj.fragSpread=0.300000
    return dbObj
