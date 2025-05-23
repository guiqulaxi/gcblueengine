# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Oil Tanker durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=1.890000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=1.980000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=2.250000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=2.700000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=3.330000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=4.140000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=5.130000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=6.300000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=7.650000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=9.180000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=10.890000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=13.720000
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*28
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=28.523001
    dbObj.waterBlastEffect[1].damageFactor=0.040000
    dbObj.waterBlastEffect[2].effectLevel=32.597000
    dbObj.waterBlastEffect[2].damageFactor=0.042000
    dbObj.waterBlastEffect[3].effectLevel=37.226002
    dbObj.waterBlastEffect[3].damageFactor=0.043000
    dbObj.waterBlastEffect[4].effectLevel=42.478001
    dbObj.waterBlastEffect[4].damageFactor=0.045000
    dbObj.waterBlastEffect[5].effectLevel=48.433998
    dbObj.waterBlastEffect[5].damageFactor=0.048000
    dbObj.waterBlastEffect[6].effectLevel=55.181000
    dbObj.waterBlastEffect[6].damageFactor=0.050000
    dbObj.waterBlastEffect[7].effectLevel=62.817001
    dbObj.waterBlastEffect[7].damageFactor=0.053000
    dbObj.waterBlastEffect[8].effectLevel=71.452003
    dbObj.waterBlastEffect[8].damageFactor=0.056000
    dbObj.waterBlastEffect[9].effectLevel=81.208000
    dbObj.waterBlastEffect[9].damageFactor=0.059000
    dbObj.waterBlastEffect[10].effectLevel=92.222000
    dbObj.waterBlastEffect[10].damageFactor=0.062000
    dbObj.waterBlastEffect[11].effectLevel=104.644997
    dbObj.waterBlastEffect[11].damageFactor=0.067000
    dbObj.waterBlastEffect[12].effectLevel=118.650002
    dbObj.waterBlastEffect[12].damageFactor=0.071000
    dbObj.waterBlastEffect[13].effectLevel=134.429001
    dbObj.waterBlastEffect[13].damageFactor=0.077000
    dbObj.waterBlastEffect[14].effectLevel=152.201004
    dbObj.waterBlastEffect[14].damageFactor=0.083000
    dbObj.waterBlastEffect[15].effectLevel=172.218994
    dbObj.waterBlastEffect[15].damageFactor=0.091000
    dbObj.waterBlastEffect[16].effectLevel=194.776001
    dbObj.waterBlastEffect[16].damageFactor=0.100000
    dbObj.waterBlastEffect[17].effectLevel=220.225006
    dbObj.waterBlastEffect[17].damageFactor=0.111000
    dbObj.waterBlastEffect[18].effectLevel=249.001999
    dbObj.waterBlastEffect[18].damageFactor=0.125000
    dbObj.waterBlastEffect[19].effectLevel=281.674988
    dbObj.waterBlastEffect[19].damageFactor=0.143000
    dbObj.waterBlastEffect[20].effectLevel=319.028992
    dbObj.waterBlastEffect[20].damageFactor=0.167000
    dbObj.waterBlastEffect[21].effectLevel=362.247009
    dbObj.waterBlastEffect[21].damageFactor=0.200000
    dbObj.waterBlastEffect[22].effectLevel=413.322998
    dbObj.waterBlastEffect[22].damageFactor=0.250000
    dbObj.waterBlastEffect[23].effectLevel=476.147003
    dbObj.waterBlastEffect[23].damageFactor=0.333000
    dbObj.waterBlastEffect[24].effectLevel=560.197021
    dbObj.waterBlastEffect[24].damageFactor=0.500000
    dbObj.waterBlastEffect[25].effectLevel=700.130005
    dbObj.waterBlastEffect[25].damageFactor=1.000000
    dbObj.waterBlastEffect[26].effectLevel=848.812988
    dbObj.waterBlastEffect[26].damageFactor=2.000000
    dbObj.waterBlastEffect[27].effectLevel=1018.692017
    dbObj.waterBlastEffect[27].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*27
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=1500.000000
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=3000.000000
    dbObj.fragEffect[2].damageFactor=0.001270
    dbObj.fragEffect[3].effectLevel=6000.000000
    dbObj.fragEffect[3].damageFactor=0.001790
    dbObj.fragEffect[4].effectLevel=10000.000000
    dbObj.fragEffect[4].damageFactor=0.002310
    dbObj.fragEffect[5].effectLevel=30000.000000
    dbObj.fragEffect[5].damageFactor=0.004010
    dbObj.fragEffect[6].effectLevel=60000.000000
    dbObj.fragEffect[6].damageFactor=0.005670
    dbObj.fragEffect[7].effectLevel=100000.000000
    dbObj.fragEffect[7].damageFactor=0.007320
    dbObj.fragEffect[8].effectLevel=300000.000000
    dbObj.fragEffect[8].damageFactor=0.012680
    dbObj.fragEffect[9].effectLevel=600000.000000
    dbObj.fragEffect[9].damageFactor=0.017930
    dbObj.fragEffect[10].effectLevel=1000000.000000
    dbObj.fragEffect[10].damageFactor=0.023140
    dbObj.fragEffect[11].effectLevel=3000000.000000
    dbObj.fragEffect[11].damageFactor=0.040080
    dbObj.fragEffect[12].effectLevel=6000000.000000
    dbObj.fragEffect[12].damageFactor=0.056690
    dbObj.fragEffect[13].effectLevel=10000000.000000
    dbObj.fragEffect[13].damageFactor=0.073180
    dbObj.fragEffect[14].effectLevel=30000000.000000
    dbObj.fragEffect[14].damageFactor=0.126760
    dbObj.fragEffect[15].effectLevel=60000000.000000
    dbObj.fragEffect[15].damageFactor=0.179260
    dbObj.fragEffect[16].effectLevel=100000000.000000
    dbObj.fragEffect[16].damageFactor=0.231430
    dbObj.fragEffect[17].effectLevel=300000000.000000
    dbObj.fragEffect[17].damageFactor=0.400840
    dbObj.fragEffect[18].effectLevel=600000000.000000
    dbObj.fragEffect[18].damageFactor=0.566870
    dbObj.fragEffect[19].effectLevel=1000000000.000000
    dbObj.fragEffect[19].damageFactor=0.731830
    dbObj.fragEffect[20].effectLevel=3000000000.000000
    dbObj.fragEffect[20].damageFactor=1.267570
    dbObj.fragEffect[21].effectLevel=6000000000.000000
    dbObj.fragEffect[21].damageFactor=1.792610
    dbObj.fragEffect[22].effectLevel=10000000000.000000
    dbObj.fragEffect[22].damageFactor=2.314250
    dbObj.fragEffect[23].effectLevel=30000001024.000000
    dbObj.fragEffect[23].damageFactor=4.008400
    dbObj.fragEffect[24].effectLevel=60000002048.000000
    dbObj.fragEffect[24].damageFactor=5.668740
    dbObj.fragEffect[25].effectLevel=99999997952.000000
    dbObj.fragEffect[25].damageFactor=7.318310
    dbObj.fragEffect[26].effectLevel=299999985664.000000
    dbObj.fragEffect[26].damageFactor=12.675680
    dbObj.radEffect=[pygcb.DamagePoint()]*6
    dbObj.radEffect[0].effectLevel=0.000000
    dbObj.radEffect[0].damageFactor=0.000000
    dbObj.radEffect[1].effectLevel=5000.000000
    dbObj.radEffect[1].damageFactor=0.000000
    dbObj.radEffect[2].effectLevel=25000.000000
    dbObj.radEffect[2].damageFactor=0.400000
    dbObj.radEffect[3].effectLevel=50000.000000
    dbObj.radEffect[3].damageFactor=2.000000
    dbObj.radEffect[4].effectLevel=125000.000000
    dbObj.radEffect[4].damageFactor=5.000000
    dbObj.radEffect[5].effectLevel=250000.000000
    dbObj.radEffect[5].damageFactor=20.000000
    dbObj.internalEffect=[pygcb.DamagePoint()]*10
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.052460
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.104920
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=0.209940
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=0.419680
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=0.839640
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=1.679010
    dbObj.internalEffect[7].effectLevel=64.000000
    dbObj.internalEffect[7].damageFactor=3.358240
    dbObj.internalEffect[8].effectLevel=128.000000
    dbObj.internalEffect[8].damageFactor=6.715890
    dbObj.internalEffect[9].effectLevel=256.000000
    dbObj.internalEffect[9].damageFactor=13.432050
    return dbObj
