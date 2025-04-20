import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Spad Wing Root x2'
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
    dbObj.childClassList=['1250 liter tank','50mm (2in) FFAR Rockets','5in HVAR','600 liter tank','GP MC 1000','GP MC 1900','GP MC 250','GP MC 500','M117','M118','Mk 16 Zuni FFAR','Mk 71 Zuni WAFAR']
    dbObj.childCapacityList=[2,38,6,2,2,2,2,2,2,2,8,8]
    dbObj.childLoadTime_s=[240.000000,360.000000,240.000000,240.000000,240.000000,240.000000,240.000000,240.000000,240.000000,240.000000,300.000000,300.000000]
    dbObj.childCycleTime_s=[0.200000,0.100000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
