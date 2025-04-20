import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1400kg'
    dbObj.maxRange_m=5235.050781
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=503.821350
    dbObj.fragCharge_kg=434.119110
    dbObj.radCharge_kg=50.382133
    dbObj.fragMetal_kg=462.059540
    dbObj.fragFragment_kg=0.082042
    dbObj.fragSpread=0.300000
    return dbObj
