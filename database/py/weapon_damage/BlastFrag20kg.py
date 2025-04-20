import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag20kg'
    dbObj.maxRange_m=808.493286
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.126116
    dbObj.fragCharge_kg=6.249256
    dbObj.radCharge_kg=0.712612
    dbObj.fragMetal_kg=6.624628
    dbObj.fragFragment_kg=0.002300
    dbObj.fragSpread=0.300000
    return dbObj
