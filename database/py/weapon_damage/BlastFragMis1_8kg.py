import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1.8kg'
    dbObj.maxRange_m=1086.623413
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.513906
    dbObj.fragCharge_kg=0.701396
    dbObj.radCharge_kg=0.051391
    dbObj.fragMetal_kg=0.584698
    dbObj.fragFragment_kg=0.003565
    dbObj.fragSpread=0.051883
    return dbObj
