import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Su-17M2 W2'
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
    dbObj.childClassList=['FAB-100','FAB-250','FAB-500','Kh-23','Kh-25ML','Kh-25MP','Kh-29L','PTB 1150','PTB-600','PTB-800','S-24B 240mm','S-25C 266mm','S-25OF 266mm','S-3K 160mm','S-5K Rocket','S-5M Rocket','S-8B 80mm','S-8K 80mm']
    dbObj.childCapacityList=[4,2,2,2,2,2,2,2,2,2,2,2,2,7,64,64,40,40]
    dbObj.childLoadTime_s=[360.000000,240.000000,240.000000,360.000000,360.000000,360.000000,360.000000,300.000000,300.000000,300.000000,240.000000,240.000000,240.000000,240.000000,240.000000,240.000000,240.000000,240.000000]
    dbObj.childCycleTime_s=[0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.150000,0.100000,0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
