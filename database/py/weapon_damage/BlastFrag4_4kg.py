import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag4.4kg'
    dbObj.maxRange_m=372.486938
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.547459
    dbObj.fragCharge_kg=1.388361
    dbObj.radCharge_kg=0.154746
    dbObj.fragMetal_kg=1.464180
    dbObj.fragFragment_kg=0.000709
    dbObj.fragSpread=0.300000
    return dbObj
