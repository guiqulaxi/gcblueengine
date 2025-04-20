import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag450kg'
    dbObj.maxRange_m=3259.449219
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=161.849335
    dbObj.fragCharge_kg=139.600449
    dbObj.radCharge_kg=16.184933
    dbObj.fragMetal_kg=148.550217
    dbObj.fragFragment_kg=0.030642
    dbObj.fragSpread=0.300000
    return dbObj
