import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1425kg'
    dbObj.maxRange_m=5271.795410
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=512.820923
    dbObj.fragCharge_kg=441.869415
    dbObj.radCharge_kg=51.282089
    dbObj.fragMetal_kg=470.309692
    dbObj.fragFragment_kg=0.083270
    dbObj.fragSpread=0.300000
    return dbObj
