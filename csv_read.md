
# 特征

1. 广告特征,

2. 用户特征

3. 上下文特征

## ad.csv

camgaignID          (推广计划id)
adID                (广告id, 单个推广计划下可能有多个)
creativeID          (素材id, 一条广告下可以有多个素材)
advertiserID        (账户id)
appID               (appid, 广告推广页面的链接地址, 点击后想要展示给用户的页面, 多个推广计划)
appPlatform         (app平台, 同一个appID只会属于一个平台)



## app_categories.csv

appID   
appCategory     (app分类, 百位表示一级类目, 十位个位表示二级类目)



## user.csv

userID  
age     
gender  
education   
marrigeStatus       (单身, 新婚, 已婚, 未知)
haveBaby    
hometown            (籍贯, 千位百位表示省份, 十位个位表示城市)
residence           (常住地)


## user_installedapps.csv 

> 用户app安装列表

userID  appID

## position.csv

positionID      (广告曝光的具体位置)
sitesetID       (站点集合ID, 如qq空间)
positionType    (广告位类型)


## test.csv

instanceID  label   clickTime   userID  positionID  
creativeID  (素材ID)
connectionType(联网方式) 
telecomsOperator(运营商)


## train.csv

> 广告点击日志

label               点击后发生转化, 1 表示发生转化
clickTime           点击时间
conversionTime      (label为1才有回流转化时间)
creativeID  
userID  
positionID  
connectionType  
telecomsOperator




## user_app_actions.csv 

> 用户app安装流水文件, 从第一天0点到第31天0点

userID 
installTime  
appID


