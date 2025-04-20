import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis0.9kg'
    dbObj.maxRange_m=734.381409
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.270000
    dbObj.fragCharge_kg=0.342000
    dbObj.radCharge_kg=0.027000
    dbObj.fragMetal_kg=0.288000
    dbObj.fragFragment_kg=0.001834
    dbObj.fragSpread=0.047548
    return dbObj
