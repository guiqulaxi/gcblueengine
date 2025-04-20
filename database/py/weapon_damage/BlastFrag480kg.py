import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag480kg'
    dbObj.maxRange_m=3353.645752
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=172.647736
    dbObj.fragCharge_kg=148.901505
    dbObj.radCharge_kg=17.264774
    dbObj.fragMetal_kg=158.450760
    dbObj.fragFragment_kg=0.032469
    dbObj.fragSpread=0.300000
    return dbObj
