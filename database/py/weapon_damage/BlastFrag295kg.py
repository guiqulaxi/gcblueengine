import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag295kg'
    dbObj.maxRange_m=2753.322754
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=106.059738
    dbObj.fragCharge_kg=91.543503
    dbObj.radCharge_kg=10.605974
    dbObj.fragMetal_kg=97.396751
    dbObj.fragFragment_kg=0.021818
    dbObj.fragSpread=0.300000
    return dbObj
