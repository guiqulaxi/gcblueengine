import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='127 mm/54 (5in) LW'
    dbObj.natoClass=''
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=0.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName=''
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=0.000000
    dbObj.height_m=0.000000
    dbObj.childClassList=['127mm mk 127 HE-CVT EX-175','127mm mk 127 HE-CVT mk 67','127mm mk 80 HE-PD EX-175','127mm mk 80 HE-PD mk 67']
    dbObj.childCapacityList=[20,20,20,20]
    dbObj.childLoadTime_s=[20.000000,20.000000,20.000000,20.000000]
    dbObj.childCycleTime_s=[2.727300,2.727300,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
