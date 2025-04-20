import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag270kg'
    dbObj.maxRange_m=2657.572510
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=97.061928
    dbObj.fragCharge_kg=83.792046
    dbObj.radCharge_kg=9.706193
    dbObj.fragMetal_kg=89.146027
    dbObj.fragFragment_kg=0.020334
    dbObj.fragSpread=0.300000
    return dbObj
