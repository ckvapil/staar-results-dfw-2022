import os
import pandas as pd

schoolids = [220905154,220905002,220901125,57916135,57905353,220901165,220901050,57905206,57905108,57905001,57905125,57905199,57905048,220905150,220905056,57905023,220905049,57905110,57905220,57905039,57905073,57905387,57905360,57905003,57905035,57905386,57905306,57905382,57905362,220905125,57916144,220905129,57905062,220905105,57905028,57905205,220905006,57905163,57905013,57905114,57905185,220905062,57905352,57905045,57905017,57905077,108807087,108807202,108807302,108807086,108807206,108807187,57905202,57905141,57905043,227820301,227820072,57905101,57905107,57905271,57905008,227820030,57905173,57905211,227820303,57916002,227820073,57916143,57916047,227820071,227820302,57905012,57807001,57905059,57905005,57905058,57905181,220905052,57905168,57905055,220905222,220905054,220905115,220905153,220905127,57916104,57916004,57905024,220905016,57905052,220905208,57916044,220901041,220901103,220901002,57905167,57905015,220905009,57905244,57905083,57905240,57905218,57905076,220905134,220905003,57905133,57905060,57905069,57916126,220905187,220905014,220905060,57905068,57905359,57905016,57905116,57905079,57916124,57916114,57905194,57905278,57905054,57905224,57803051,57803017,57905007,57803018,57803103,57916146,57803011,57803010,57803048,57803050,57803016,57803006,57803046,57803003,57803007,57803044,57803111,57803104,57803013,57803043,57803102,57803005,57803012,57803008,57803002,57803107,57803108,57803110,57803105,57803014,57803049,57803109,57803106,57803114,57803004,57803009,57803112,57803047,57905192,57905056,57905135,57905182,57905279,57905233,57803045,57905021,220905051,57905216,57905046,57905049,220905048,57905161,57905303,57905014,220905061,57905301,57905380,57905174,57905171,57905162,57905022,220902046,220919101,220917041,220912113,220912103,220918101,57910001,57910050,57910129,220906001,220916001,220916041,57912041,220907102,220914102,220908202,220908045,220908007,220908201,57907106,57807105,57914049,57914042,57903010,57909119]

def staardata(filename,meetsfield):
    data = pd.read_csv(filename)
    data = data[data["campus"].isin(schoolids)]
    data = data[["year","course","campus","cname",meetsfield]]
    data.rename(columns={meetsfield:"meets"},inplace=True)
    return data

#finaldata = staardata("algebra1.csv","a1_all_meetsgl_rm")
#finaldata = pd.concat([finaldata,staardata("bio.csv","bi_all_meetsgl_rm")])
#finaldata = pd.concat([finaldata,staardata("eng1.csv","e1_all_meetsgl_rm")])
#finaldata = pd.concat([finaldata,staardata("eng2.csv","e2_all_meetsgl_rm")])
#finaldata = pd.concat([finaldata,staardata("ushist.csv","us_all_meetsgl_rm")])
#finaldata.to_csv("eoc.csv")

def staarmiddle(filename,meetsfield,course):
    data = pd.read_csv(filename)
    data = data[data["CAMPUS"].isin(schoolids)]
    data = data[["YEAR","CAMPUS","CNAME",meetsfield]]
    data["COURSE"] = course
    data.rename(columns={meetsfield:"MEETS"},inplace=True)
    return data

finaldata = staarmiddle("grade3.csv","r_all_meetsgl_rm","STAAR - 3rd Reading")
finaldata = pd.concat([finaldata,staarmiddle("grade3.csv","m_all_meetsgl_rm","STAAR - 3rd Math")])
finaldata = pd.concat([finaldata,staarmiddle("grade4.csv","r_all_meetsgl_rm","STAAR - 4th Reading")])
finaldata = pd.concat([finaldata,staarmiddle("grade4.csv","m_all_meetsgl_rm","STAAR - 4th Math")])
finaldata = pd.concat([finaldata,staarmiddle("grade5.csv","r_all_meetsgl_rm","STAAR - 5th Reading")])
finaldata = pd.concat([finaldata,staarmiddle("grade5.csv","m_all_meetsgl_rm","STAAR - 5th Math")])
finaldata = pd.concat([finaldata,staarmiddle("grade5.csv","s_all_meetsgl_rm","STAAR - 5th Science")])
finaldata = pd.concat([finaldata,staarmiddle("grade6.csv","r_all_meetsgl_rm","STAAR - 6th Reading")])
finaldata = pd.concat([finaldata,staarmiddle("grade6.csv","m_all_meetsgl_rm","STAAR - 6th Math")])
finaldata = pd.concat([finaldata,staarmiddle("grade7.csv","r_all_meetsgl_rm","STAAR - 7th Reading")])
finaldata = pd.concat([finaldata,staarmiddle("grade7.csv","m_all_meetsgl_rm","STAAR - 7th Math")])
finaldata = pd.concat([finaldata,staarmiddle("grade8.csv","r_all_meetsgl_rm","STAAR - 8th Reading")])
finaldata = pd.concat([finaldata,staarmiddle("grade8.csv","m_all_meetsgl_rm","STAAR - 8th Math")])
finaldata = pd.concat([finaldata,staarmiddle("grade8.csv","s_all_meetsgl_rm","STAAR - 8th Science")])
finaldata = pd.concat([finaldata,staarmiddle("grade8.csv","h_all_meetsgl_rm","STAAR - 8th Social Studies")])
finaldata.to_csv("3-8s.csv")