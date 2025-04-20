import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2100kg'
    dbObj.maxRange_m=6120.698242
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=755.811340
    dbObj.fragCharge_kg=651.125793
    dbObj.radCharge_kg=75.581131
    dbObj.fragMetal_kg=693.062866
    dbObj.fragFragment_kg=0.114594
    dbObj.fragSpread=0.300000
    return dbObj
