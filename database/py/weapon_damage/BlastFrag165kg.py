import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag165kg'
    dbObj.maxRange_m=2153.543213
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=59.274071
    dbObj.fragCharge_kg=51.233952
    dbObj.radCharge_kg=5.927407
    dbObj.fragMetal_kg=54.491978
    dbObj.fragFragment_kg=0.013461
    dbObj.fragSpread=0.300000
    return dbObj
