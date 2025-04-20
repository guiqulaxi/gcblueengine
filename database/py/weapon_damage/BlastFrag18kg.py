import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag18kg'
    dbObj.maxRange_m=768.957092
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.408715
    dbObj.fragCharge_kg=5.627523
    dbObj.radCharge_kg=0.640871
    dbObj.fragMetal_kg=5.963762
    dbObj.fragFragment_kg=0.002118
    dbObj.fragSpread=0.300000
    return dbObj
