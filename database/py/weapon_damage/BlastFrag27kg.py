import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag27kg'
    dbObj.maxRange_m=924.227661
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.638715
    dbObj.fragCharge_kg=8.424191
    dbObj.radCharge_kg=0.963871
    dbObj.fragMetal_kg=8.937095
    dbObj.fragFragment_kg=0.002879
    dbObj.fragSpread=0.300000
    return dbObj
