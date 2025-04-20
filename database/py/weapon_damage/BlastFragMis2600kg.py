import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis2600kg'
    dbObj.maxRange_m=9821.790039
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=275.776764
    dbObj.fragCharge_kg=1324.148804
    dbObj.radCharge_kg=27.577675
    dbObj.fragMetal_kg=1000.074402
    dbObj.fragFragment_kg=0.305180
    dbObj.fragSpread=0.300000
    return dbObj
