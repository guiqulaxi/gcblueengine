import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1500kg'
    dbObj.maxRange_m=5379.009277
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=539.819641
    dbObj.fragCharge_kg=465.120239
    dbObj.radCharge_kg=53.981964
    dbObj.fragMetal_kg=495.060120
    dbObj.fragFragment_kg=0.086914
    dbObj.fragSpread=0.300000
    return dbObj
