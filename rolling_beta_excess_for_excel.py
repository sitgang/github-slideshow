# -*- coding: utf-8 -*-
#把nnan换成0
import statsmodels.api as sm
from statsmodels import regression
import random as rd
import pandas as pd
import numpy as np
path = "/Users/xuegeng/Documents/JD_Quant/Mission_5_SW_excess/申万1贝塔超额.xlsx"
path2 = "/Users/xuegeng/Documents/JD_Quant/Mission_5_SW_excess/申万2贝塔超额.xlsx"

df = pd.read_excel(path)

col = [u'农林牧渔(申万)', u'采掘(申万)', u'化工(申万)', u'钢铁(申万)', u'有色金属(申万)', u'电子(申万)',
       u'家用电器(申万)', u'食品饮料(申万)', u'纺织服装(申万)', u'轻工制造(申万)', u'医药生物(申万)',
       u'公用事业(申万)', u'交通运输(申万)', u'房地产(申万)', u'商业贸易(申万)', u'休闲服务(申万)',
       u'综合(申万)', u'建筑材料(申万)', u'建筑装饰(申万)', u'电气设备(申万)', u'国防军工(申万)',
       u'计算机(申万)', u'传媒(申万)', u'通信(申万)', u'银行(申万)', u'非银金融(申万)', u'汽车(申万)',
       u'机械设备(申万)']

std_col = [u'沪深300', u'中证800', u'中证500', u'万得全A']

col2 = [u'林业Ⅱ(申万)', u'农产品加工(申万)', u'农业综合Ⅱ(申万)', u'饲料Ⅱ(申万)', u'渔业(申万)',
       u'种植业(申万)', u'畜禽养殖Ⅱ(申万)', u'动物保健Ⅱ(申万)', u'煤炭开采Ⅱ(申万)', u'其他采掘Ⅱ(申万)',u'石油开采Ⅱ(申万)', u'采掘服务Ⅱ(申万)', u'化学纤维(申万)', u'化学原料(申万)', u'化学制品(申万)',
       u'石油化工(申万)', u'塑料Ⅱ(申万)', u'橡胶(申万)', u'钢铁Ⅱ(申万)', u'金属非金属新材料(申万)',
       u'黄金Ⅱ(申万)', u'稀有金属(申万)', u'工业金属(申万)', u'通用机械(申万)', u'仪器仪表Ⅱ(申万)',
       u'专用设备(申万)', u'金属制品Ⅱ(申万)', u'运输设备Ⅱ(申万)', u'半导体(申万)', u'其他电子Ⅱ(申万)',
       u'元件Ⅱ(申万)', u'光学光电子(申万)', u'电子制造Ⅱ(申万)', u'汽车服务Ⅱ(申万)', u'汽车零部件Ⅱ(申万)',
       u'汽车整车(申万)', u'计算机设备Ⅱ(申万)', u'通信设备(申万)', u'白色家电(申万)', u'视听器材(申万)',
       u'饮料制造(申万)', u'食品加工(申万)', u'纺织制造(申万)', u'服装家纺(申万)', u'包装印刷Ⅱ(申万)',
       u'家用轻工(申万)', u'造纸Ⅱ(申万)', u'化学制药(申万)', u'生物制品Ⅱ(申万)', u'医疗器械Ⅱ(申万)',
       u'医药商业Ⅱ(申万)', u'中药Ⅱ(申万)', u'医疗服务Ⅱ(申万)', u'电力(申万)', u'环保工程及服务Ⅱ(申万)',
       u'燃气Ⅱ(申万)', u'水务Ⅱ(申万)', u'港口Ⅱ(申万)', u'公交Ⅱ(申万)', u'航空运输Ⅱ(申万)',
       u'机场Ⅱ(申万)', u'高速公路Ⅱ(申万)', u'航运Ⅱ(申万)', u'铁路运输Ⅱ(申万)', u'物流Ⅱ(申万)',
       u'房地产开发Ⅱ(申万)', u'园区开发Ⅱ(申万)', u'多元金融Ⅱ(申万)', u'银行Ⅱ(申万)', u'券商Ⅱ(申万)',
       u'保险Ⅱ(申万)', u'贸易Ⅱ(申万)', u'一般零售(申万)', u'专业零售(申万)', u'商业物业经营(申万)',
       u'餐饮Ⅱ(申万)', u'景点(申万)', u'酒店Ⅱ(申万)', u'旅游综合Ⅱ(申万)', u'其他休闲服务Ⅱ(申万)',
       u'计算机应用(申万)', u'通信运营Ⅱ(申万)', u'综合Ⅱ(申万)', u'水泥制造Ⅱ(申万)', u'玻璃制造Ⅱ(申万)',
       u'其他建材Ⅱ(申万)', u'房屋建设Ⅱ(申万)', u'装修装饰Ⅱ(申万)', u'基础建设(申万)', u'专业工程(申万)',
       u'园林工程Ⅱ(申万)', u'电机Ⅱ(申万)', u'电气自动化设备(申万)', u'电源设备(申万)', u'高低压设备(申万)',
       u'航天装备Ⅱ(申万)', u'航空装备Ⅱ(申万)', u'地面兵装Ⅱ(申万)', u'船舶制造Ⅱ(申万)', u'营销传播(申万)',
       u'互联网传媒(申万)', u'文化传媒(申万)', u'其他交运设备Ⅱ(申万)']
std_col2 = [u'沪深300', u'中证800', u'中证500', u'万得全A']

col_len = 32
col_len2 = 107

df = df.set_index(u'日期')[-(244+40):]
window = 24

data = np.array(df)

def excel_array_to_df(data,colu,idx):

    df = pd.DataFrame(data,columns = colu,index = idx)
    df  = df.rolling(82).sum().dropna()    
    data_p = np.array(df)
    return data_p

def linreg(df,col1,col2):
    df = (df/df.shift(1)-1)[[col1,col2]].dropna()
    y = np.array(df[col1])
    x = np.array(df[col2])
    try:
        x = sm.add_constant(x)
    except:
        return np.nan
 
    model = regression.linear_model.OLS(y,x).fit()
    try:
        rr =  model.params[1]
        return rr
    except:
        return np.nan

def excess_rt(df,col1,col2):
    df = (df/df.shift(1)-1)[[col1,col2]].dropna()
    x = np.array(df[col1])
    y = np.array(df[col2])
    
    return np.mean(y-x)

def raw_df_volatility(df):
    df = (df/df.shift(1)-1)
    return df.rolling(window).std()

def cal(fc):
    betas = []
    col_names = []
    
    for x in list(df.columns[:-4]):
        
        for y in list(df.columns[-4:]):
            s  = []
            for i in range(len(df)-window):
                result  = fc(df.iloc[i:i+window],x, y)
                sb = pd.Series(result, index=[df.index[i+window]])
                
                s.append(sb)
                
            s = pd.concat(s)
            betas.append(s)
            nm = x + "_" +  y
            col_names.append(nm)
    
    dfs = pd.DataFrame(betas).T
    dfs.columns = col_names
    dfs = dfs[dfs.index.year ==2017]
    return dfs

def cal_corr(df):
    betas = []
    col_names = []
    df = (df/df.shift(1)-1)
    count = 0
    for x in list(df.columns):
        count+=1
        for y in list(df.columns):
            s  = []
            for i in range(len(df)-window):
                df2 = df.iloc[i:i+window]
                xx = np.array(df2[x])
                yy = np.array(df2[y])
                
                result  = np.corrcoef(xx,yy)[0][1]
                
                sb = pd.Series(result, index=[df.index[i+window]])
                
                s.append(sb)
                
            s = pd.concat(s)
            betas.append(s)
            nm = x + "_" +  y
            col_names.append(nm)
    
    dfs = pd.DataFrame(betas).T
    dfs.columns = col_names
    #dfs = dfs[dfs.index.year ==2017]
    return dfs

#dfs = cal(linreg)
#dfs.to_excel("/Users/xuegeng/Documents/JD_Quant/Mission_5_SW_excess/SW2_Beta.xlsx")
#dfs = cal(excess_rt)
#dfs.to_excel("/Users/xuegeng/Documents/JD_Quant/Mission_5_SW_excess/SW2_Exc.xlsx")