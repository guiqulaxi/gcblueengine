import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis330kg'
    dbObj.maxRange_m=4875.447266
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=51.802338
    dbObj.fragCharge_kg=156.865112
    dbObj.radCharge_kg=5.180233
    dbObj.fragMetal_kg=121.332558
    dbObj.fragFragment_kg=0.066411
    dbObj.fragSpread=0.300000
    return dbObj
