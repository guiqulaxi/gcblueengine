import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag4.5kg'
    dbObj.maxRange_m=376.496033
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.582905
    dbObj.fragCharge_kg=1.419730
    dbObj.radCharge_kg=0.158290
    dbObj.fragMetal_kg=1.497365
    dbObj.fragFragment_kg=0.000720
    dbObj.fragSpread=0.300000
    return dbObj
