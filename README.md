# pre

## libffm数据格式

| train表中          | 附表                             | <field1>: | <index1>:             | <value1>                     |
| ---------------- | ------------------------------ | --------- | --------------------- | ---------------------------- |
| label            |                                | 0/1       |                       |                              |
| clickTime        |                                | 39：       | 39：                   | <clickTime的后四位转成分钟/1440>     |
| conversionTime   |                                |           |                       |                              |
| creativeID       | ```ad表中```                     |           |                       |                              |
|                  | creativeID                     | 10:       | 10<creativeID>:       | 1                            |
|                  | adID                           | 11:       | 11<adID>:             | 1                            |
|                  | camgaignID                     | 12:       | 12<camgaignID>:       | 1                            |
|                  | advertiserID                   | 13:       | 13<advertiserID>:     | 1                            |
|                  | appID --```app_categories表中``` |           |                       |                              |
|                  | appID                          | 14:       | 14<appID>:            | 1                            |
|                  | appCategory                    | 15:       | 15<appCategory>:      | 1/0                          |
|                  | appPlatform                    | 16:       | 16<appPlatform>:      | 1/0                          |
| userID           | ```user表中```                   |           |                       |                              |
|                  | userID                         | 17:       | 17<userID>:           | 1                            |
|                  | age                            | 18:       | 18:                   | <age/80>                     |
|                  | gender                         | 19:       | 19<gender>:           | 1/0                          |
|                  | education                      | 20:       | 20<education>:        | 1/0                          |
|                  | marriageStatus                 | 30:       | 30<marriageStatus>:   | 1/0                          |
|                  | haveBaby                       | 31:       | 31<haveBaby>:         | 1/0                          |
|                  | hometown                       | 32:       | 32<hometown>:         | 1/0                          |
|                  | residence                      | 33:       | 33<residence>:        | 1/0                          |
| positionID       | ```position表中```               |           |                       |                              |
|                  | positionID                     | 34:       | 34<positionID>:       | 1                            |
|                  | sitesetID                      | 35:       | 35<sitesetID>:        | 1                            |
|                  | positionType                   | 36:       | 36<positionType>:     | 1                            |
| connectionType   |                                | 37:       | 37<connectionType>:   | 1/0                          |
| telecomsOperator |                                | 38:       | 38<telecomsOperator>: | 1/0                          |
|                  |                                |           |                       |                              |
| userID           | 用户安装app列表                      |           |                       |                              |
|                  | app28个分类                       | 50:       | 50<appCategory>:      | <installedappsCategory_rate> |
|                  |                                |           |                       |                              |
| userID           | 用户安装流水                         |           |                       |                              |
|                  | app28个分类                       | 60:       | 60<appCategory>:      | <max_tmie/310000>            |




train

```
!label---(0/1)
!clickTime
!conversionTime

!creativeID
!!ad表中
!!!creativeID-----------------------(1:<creativeID>:1)
!!!adID-----------------------------(2:<adID>:1)
!!!camgaignID-----------------------(3:<camgaignID>:1)
!!!advertiserID---------------------(4:<advertiserID>:1)
!!!appID----------------------------(5:<appID>:1)
!!!appID-app_categories表中
!!!!appCategory---(6:<appCategory>:1)
!!!appPlatform----------------------(7:<appPlatform>:1)

!userID
!!user表中
!!!age（input）
!!!gender（input）
!!!education（input）
!!!marriageStatus（input）
!!!haveBaby（input）
!!!hometown（input）
!!!residence（input）
!!user_installedappsCategory表中
!!!用户安装的app类别比例情况（28类）（28个input）
!!user_app_actions表相关
!!!用户app安装时间（待定）

!positionID
!!position表中
!!!positionID（input）
!!!sitesetID（input）
!!!positionType（input）

!connectionType（input）
!telecomsOperator（input）
```



## 一个训练条目


![](./img/train.png)

```mermaid
!label
!clickTime
!conversionTime

!creativeID
!!ad表中
!!!creativeID
!!!adID（input）
!!!camgaignID（input）
!!!advertiserID（input）
!!!appID（input）
!!!appID--app_categories表中
!!!!appCategory（input）
!!!appPlatform（input）

!userID
!!user表中
!!!age（input）
!!!gender（input）
!!!education（input）
!!!marriageStatus（input）
!!!haveBaby（input）
!!!hometown（input）
!!!residence（input）
!!user_installedappsCategory表中
!!!用户安装的app类别比例情况（28类）（28个input）
!!user_app_actions表相关
!!!用户app安装时间（待定）

!positionID
!!position表中
!!!positionID（input）
!!!sitesetID（input）
!!!positionType（input）

!connectionType（input）
!telecomsOperator（input）
```


