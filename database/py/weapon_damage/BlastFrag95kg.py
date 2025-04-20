import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag95kg'
    dbObj.maxRange_m=1664.449463
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=34.087688
    dbObj.fragCharge_kg=29.524876
    dbObj.radCharge_kg=3.408769
    dbObj.fragMetal_kg=31.387438
    dbObj.fragFragment_kg=0.008242
    dbObj.fragSpread=0.300000
    return dbObj
