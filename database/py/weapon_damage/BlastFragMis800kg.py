import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis800kg'
    dbObj.maxRange_m=6281.423340
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=108.109749
    dbObj.fragCharge_kg=391.926819
    dbObj.radCharge_kg=10.810975
    dbObj.fragMetal_kg=299.963409
    dbObj.fragFragment_kg=0.114185
    dbObj.fragSpread=0.300000
    return dbObj
