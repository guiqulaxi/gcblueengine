import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir190kg'
    dbObj.maxRange_m=4339.589355
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=32.412567
    dbObj.fragCharge_kg=88.591621
    dbObj.radCharge_kg=3.241257
    dbObj.fragMetal_kg=68.995811
    dbObj.fragFragment_kg=0.051994
    dbObj.fragSpread=0.300000
    return dbObj
