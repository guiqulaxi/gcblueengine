import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3100kg'
    dbObj.maxRange_m=10466.055664
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=315.362946
    dbObj.fragCharge_kg=1587.758057
    dbObj.radCharge_kg=31.536295
    dbObj.fragMetal_kg=1196.879028
    dbObj.fragFragment_kg=0.351816
    dbObj.fragSpread=0.300000
    return dbObj
