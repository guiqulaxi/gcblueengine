import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag27.5kg'
    dbObj.maxRange_m=931.410706
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.818262
    dbObj.fragCharge_kg=8.579492
    dbObj.radCharge_kg=0.981826
    dbObj.fragMetal_kg=9.102246
    dbObj.fragFragment_kg=0.002917
    dbObj.fragSpread=0.300000
    return dbObj
