import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1975kg'
    dbObj.maxRange_m=8850.740234
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=222.876602
    dbObj.fragCharge_kg=996.915588
    dbObj.radCharge_kg=22.287661
    dbObj.fragMetal_kg=755.207825
    dbObj.fragFragment_kg=0.242054
    dbObj.fragSpread=0.300000
    return dbObj
