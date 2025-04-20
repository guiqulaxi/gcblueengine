import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1175kg'
    dbObj.maxRange_m=4878.697754
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=422.825653
    dbObj.fragCharge_kg=364.366241
    dbObj.radCharge_kg=42.282566
    dbObj.fragMetal_kg=387.808105
    dbObj.fragFragment_kg=0.070665
    dbObj.fragSpread=0.300000
    return dbObj
