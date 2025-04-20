import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag31kg'
    dbObj.maxRange_m=981.303955
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=11.075308
    dbObj.fragCharge_kg=9.666462
    dbObj.radCharge_kg=1.107531
    dbObj.fragMetal_kg=10.258231
    dbObj.fragFragment_kg=0.003190
    dbObj.fragSpread=0.300000
    return dbObj
