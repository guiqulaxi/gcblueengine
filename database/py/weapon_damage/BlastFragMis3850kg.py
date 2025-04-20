import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3850kg'
    dbObj.maxRange_m=11276.973633
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=371.086945
    dbObj.fragCharge_kg=1985.608765
    dbObj.radCharge_kg=37.108692
    dbObj.fragMetal_kg=1493.304321
    dbObj.fragFragment_kg=0.416078
    dbObj.fragSpread=0.300000
    return dbObj
