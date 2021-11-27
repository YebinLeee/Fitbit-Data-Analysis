# BLEP Fitbit-Data-Analysis
Fitbit을 이용해 얻은 활동량 Time Series(시계열) 데이터 분석

## To-Do
- [ ] 시계열 데이터 numpy 배열로 변환
- [ ] matplotlib을 이용하여 데이터 시각화
- [ ] 데이터 분석

<br>
 <hr>


# Data 

<details> 
  <summary> json data 기본 형식(dataset 일부 추출) </summary>

```
'distance':
             {'activities-distance': [
                      {'dateTime': '2021-11-18',
                       'value': '0'
                       }
                                      ],
              'activities-distance-intraday':
                          {'dataset': [
                                    {'time': '09:00:00', 'value': 0},
                                    {'time': '09:01:00', 'value': 0},
                                    {'time': '09:02:00', 'value': 0},
                                       ],
               'datasetInterval': 1,
               'datasetType': 'minute'
             }
}, 

'calories':
             {
             'activities-calories': [
                         {'dateTime': '2021-11-18',
                          'value': '63.65'
                          }
                                      ],

               'activities-calories-intraday':
                            {'dataset': [
                                   {'level': 0, 'mets': 10, 'time': '09:00:00', 'value': 1.0608},
                                   {'level': 0, 'mets': 10, 'time': '09:01:00', 'value': 1.0608},
                                         ],       
               'datasetInterval': 1,
               'datasetType': 'minute'
              }
},

'steps': 
         {'activities-steps': [
                          {
                          'dateTime': '2021-11-18',
                          'value': '0'
                          }
                               ],
           'activities-steps-intraday':
                            {'dataset': [
                                  {'time': '09:00:00', 'value': 0},
                                  {'time': '09:01:00', 'value': 0},
                                  {'time': '09:59:00', 'value': 0}
                                         ], 
           'datasetInterval': 1,
           'datasetType': 'minute'
                              }
         }
}                
```
</details>

<details>
  <summary> Json raw_data sample </summary>
  
```json
{'distance': {'activities-distance': [{'dateTime': '2021-04-07', 'value': '0'}], 'activities-distance-intraday': {'dataset': [{'time': '09:00:00', 'value': 0}, {'time': '09:01:00', 'value': 0}, {'time': '09:02:00', 'value': 0}, {'time': '09:03:00', 'value': 0}, {'time': '09:04:00', 'value': 0}, {'time': '09:05:00', 'value': 0}, {'time': '09:06:00', 'value': 0}, {'time': '09:07:00', 'value': 0}, {'time': '09:08:00', 'value': 0}, {'time': '09:09:00', 'value': 0}, {'time': '09:10:00', 'value': 0}, {'time': '09:11:00', 'value': 0}, {'time': '09:12:00', 'value': 0}, {'time': '09:13:00', 'value': 0}, {'time': '09:14:00', 'value': 0}, {'time': '09:15:00', 'value': 0}, {'time': '09:16:00', 'value': 0}, {'time': '09:17:00', 'value': 0}, {'time': '09:18:00', 'value': 0}, {'time': '09:19:00', 'value': 0}, {'time': '09:20:00', 'value': 0}, {'time': '09:21:00', 'value': 0}, {'time': '09:22:00', 'value': 0}, {'time': '09:23:00', 'value': 0}, {'time': '09:24:00', 'value': 0}, {'time': '09:25:00', 'value': 0}, {'time': '09:26:00', 'value': 0}, {'time': '09:27:00', 'value': 0}, {'time': '09:28:00', 'value': 0}, {'time': '09:29:00', 'value': 0}, {'time': '09:30:00', 'value': 0}, {'time': '09:31:00', 'value': 0}, {'time': '09:32:00', 'value': 0}, {'time': '09:33:00', 'value': 0}, {'time': '09:34:00', 'value': 0}, {'time': '09:35:00', 'value': 0}, {'time': '09:36:00', 'value': 0}, {'time': '09:37:00', 'value': 0}, {'time': '09:38:00', 'value': 0}, {'time': '09:39:00', 'value': 0}, {'time': '09:40:00', 'value': 0}, {'time': '09:41:00', 'value': 0}, {'time': '09:42:00', 'value': 0.0028}, {'time': '09:43:00', 'value': 0}, {'time': '09:44:00', 'value': 0}, {'time': '09:45:00', 'value': 0}, {'time': '09:46:00', 'value': 0}, {'time': '09:47:00', 'value': 0}, {'time': '09:48:00', 'value': 0}, {'time': '09:49:00', 'value': 0}, {'time': '09:50:00', 'value': 0}, {'time': '09:51:00', 'value': 0}, {'time': '09:52:00', 'value': 0}, {'time': '09:53:00', 'value': 0}, {'time': '09:54:00', 'value': 0}, {'time': '09:55:00', 'value': 0}, {'time': '09:56:00', 'value': 0}, {'time': '09:57:00', 'value': 0}, {'time': '09:58:00', 'value': 0}, {'time': '09:59:00', 'value': 0}], 'datasetInterval': 1, 'datasetType': 'minute'}}, 'calories': {'activities-calories': [{'dateTime': '2021-04-07', 'value': '67.04'}], 'activities-calories-intraday': {'dataset': [{'level': 0, 'mets': 11, 'time': '09:00:00', 'value': 1.16688}, {'level': 0, 'mets': 11, 'time': '09:01:00', 'value': 1.16688}, {'level': 0, 'mets': 10, 'time': '09:02:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:03:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:04:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:05:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:06:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:07:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:08:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:09:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:10:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:11:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:12:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:13:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:14:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:15:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:16:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:17:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:18:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:19:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:20:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:21:00', 'value': 1.0608}, {'level': 0, 'mets': 11, 'time': '09:22:00', 'value': 1.16688}, {'level': 0, 'mets': 10, 'time': '09:23:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:24:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:25:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:26:00', 'value': 1.0608}, {'level': 0, 'mets': 11, 'time': '09:27:00', 'value': 1.16688}, {'level': 0, 'mets': 10, 'time': '09:28:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:29:00', 'value': 1.0608}, {'level': 0, 'mets': 11, 'time': '09:30:00', 'value': 1.16688}, {'level': 0, 'mets': 10, 'time': '09:31:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:32:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:33:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:34:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:35:00', 'value': 1.0608}, {'level': 0, 'mets': 11, 'time': '09:36:00', 'value': 1.16688}, {'level': 0, 'mets': 10, 'time': '09:37:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:38:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:39:00', 'value': 1.0608}, {'level': 0, 'mets': 11, 'time': '09:40:00', 'value': 1.16688}, {'level': 0, 'mets': 11, 'time': '09:41:00', 'value': 1.16688}, {'level': 1, 'mets': 22, 'time': '09:42:00', 'value': 2.33376}, {'level': 0, 'mets': 10, 'time': '09:43:00', 'value': 1.0608}, {'level': 0, 'mets': 10, 'time': '09:44:00', 'value': 1.0608}, {'level': 0, 'mets': 11, 'time': '09:45:00', 'value': 1.16688}, {'level': 0, 'mets': 11, 'time': '09:46:00', 'value': 1.16688}, {'level': 0, 'mets': 11, 'time': '09:47:00', 'value': 1.16688}, {'level': 0, 'mets': 11, 'time': '09:48:00', 'value': 1.16688}, {'level': 0, 'mets': 10, 'time': '09:49:00', 'value': 1.0608}, {'level': 0, 'mets': 11, 'time': '09:50:00', 'value': 1.16688}, {'level': 0, 'mets': 11, 'time': '09:51:00', 'value': 1.16688}, {'level': 0, 'mets': 10, 'time': '09:52:00', 'value': 1.0608}, {'level': 0, 'mets': 11, 'time': '09:53:00', 'value': 1.16688}, {'level': 0, 'mets': 10, 'time': '09:54:00', 'value': 1.0608}, {'level': 0, 'mets': 11, 'time': '09:55:00', 'value': 1.16688}, {'level': 0, 'mets': 11, 'time': '09:56:00', 'value': 1.16688}, {'level': 0, 'mets': 11, 'time': '09:57:00', 'value': 1.16688}, {'level': 0, 'mets': 11, 'time': '09:58:00', 'value': 1.16688}, {'level': 0, 'mets': 11, 'time': '09:59:00', 'value': 1.16688}], 'datasetInterval': 1, 'datasetType': 'minute'}}, 'steps': {'activities-steps': [{'dateTime': '2021-04-07', 'value': '4'}], 'activities-steps-intraday': {'dataset': [{'time': '09:00:00', 'value': 0}, {'time': '09:01:00', 'value': 0}, {'time': '09:02:00', 'value': 0}, {'time': '09:03:00', 'value': 0}, {'time': '09:04:00', 'value': 0}, {'time': '09:05:00', 'value': 0}, {'time': '09:06:00', 'value': 0}, {'time': '09:07:00', 'value': 0}, {'time': '09:08:00', 'value': 0}, {'time': '09:09:00', 'value': 0}, {'time': '09:10:00', 'value': 0}, {'time': '09:11:00', 'value': 0}, {'time': '09:12:00', 'value': 0}, {'time': '09:13:00', 'value': 0}, {'time': '09:14:00', 'value': 0}, {'time': '09:15:00', 'value': 0}, {'time': '09:16:00', 'value': 0}, {'time': '09:17:00', 'value': 0}, {'time': '09:18:00', 'value': 0}, {'time': '09:19:00', 'value': 0}, {'time': '09:20:00', 'value': 0}, {'time': '09:21:00', 'value': 0}, {'time': '09:22:00', 'value': 0}, {'time': '09:23:00', 'value': 0}, {'time': '09:24:00', 'value': 0}, {'time': '09:25:00', 'value': 0}, {'time': '09:26:00', 'value': 0}, {'time': '09:27:00', 'value': 0}, {'time': '09:28:00', 'value': 0}, {'time': '09:29:00', 'value': 0}, {'time': '09:30:00', 'value': 0}, {'time': '09:31:00', 'value': 0}, {'time': '09:32:00', 'value': 0}, {'time': '09:33:00', 'value': 0}, {'time': '09:34:00', 'value': 0}, {'time': '09:35:00', 'value': 0}, {'time': '09:36:00', 'value': 0}, {'time': '09:37:00', 'value': 0}, {'time': '09:38:00', 'value': 0}, {'time': '09:39:00', 'value': 0}, {'time': '09:40:00', 'value': 0}, {'time': '09:41:00', 'value': 0}, {'time': '09:42:00', 'value': 4}, {'time': '09:43:00', 'value': 0}, {'time': '09:44:00', 'value': 0}, {'time': '09:45:00', 'value': 0}, {'time': '09:46:00', 'value': 0}, {'time': '09:47:00', 'value': 0}, {'time': '09:48:00', 'value': 0}, {'time': '09:49:00', 'value': 0}, {'time': '09:50:00', 'value': 0}, {'time': '09:51:00', 'value': 0}, {'time': '09:52:00', 'value': 0}, {'time': '09:53:00', 'value': 0}, {'time': '09:54:00', 'value': 0}, {'time': '09:55:00', 'value': 0}, {'time': '09:56:00', 'value': 0}, {'time': '09:57:00', 'value': 0}, {'time': '09:58:00', 'value': 0}, {'time': '09:59:00', 'value': 0}], 'datasetInterval': 1, 'datasetType': 'minute'}}}
```
  
</details>
<br>


### 1. raw data (CSV File)
- 2021.04.07 09:00:00 ~ 2021.11.18 09:00:00


![image](https://user-images.githubusercontent.com/71310074/143684509-72c29569-38d4-400a-8c66-a6c9872f819e.png)
![image](https://user-images.githubusercontent.com/71310074/143684558-ffd2f3c3-6437-4c8a-985c-03d281315ad0.png)
![image](https://user-images.githubusercontent.com/71310074/143684571-44b62484-f1a8-4482-a0ea-5d13ecb13d73.png)


### 2. data (dictionary) 형식
<img src= "https://user-images.githubusercontent.com/71310074/143681059-f47078f5-2277-4aa8-ae79-0f2cd1b75aa9.png" width="600">

## 3. json Data (json) 형식
<img src = "https://user-images.githubusercontent.com/71310074/143681372-fe0ba8ab-d5e4-404d-b8bb-24a87701435f.png" width="600">
<br>

<details>
  <summary> calories data (dictionary) </summary>
 

![image](https://user-images.githubusercontent.com/71310074/143681392-2ae6a477-ea25-4f46-b372-8462a92b8579.png)

![image](https://user-images.githubusercontent.com/71310074/143681399-62fe858f-0f6b-4eac-929d-2cef22050ca1.png)

![image](https://user-images.githubusercontent.com/71310074/143681407-2e31645b-fe62-4e96-918e-7bc093261821.png)

![image](https://user-images.githubusercontent.com/71310074/143681416-e31fed29-a7d1-4d03-b706-2064cce6eb88.png)

![image](https://user-images.githubusercontent.com/71310074/143681423-4af9c762-c011-404a-8a10-4bd868988b29.png)


</details>

<details>
  <summary> distance data (dictionary) </summary>
  
  ![image](https://user-images.githubusercontent.com/71310074/143681472-9f9dc46c-f7ac-4f3f-91d7-ea90ec4d60fc.png)
  ![image](https://user-images.githubusercontent.com/71310074/143681489-6f4ec487-d4d8-4c2f-8703-bcec36cffa39.png)
![image](https://user-images.githubusercontent.com/71310074/143681495-609dbb9b-26e8-457d-88c2-e7d8b201aaef.png)
![image](https://user-images.githubusercontent.com/71310074/143681508-3cd941d0-f065-4149-a1dc-e35182dd4356.png)
![image](https://user-images.githubusercontent.com/71310074/143681520-0d8b2eb3-05c6-4266-b3bb-cb34e2184563.png)
![image](https://user-images.githubusercontent.com/71310074/143681526-23951758-29ef-4920-ac29-41d2e7c35ffe.png)
![image](https://user-images.githubusercontent.com/71310074/143681536-33ad03c7-22a5-40ad-8e64-c03af020b894.png)
![image](https://user-images.githubusercontent.com/71310074/143681543-07538def-0c64-421f-bb18-b7c976c14ae4.png)
![image](https://user-images.githubusercontent.com/71310074/143681548-54f3aa5e-bba2-482a-9e9b-b1d48686888f.png)

  
  
</details>

<details>
  <summary> steps data (dictionary) </summary>
  
  ![image](https://user-images.githubusercontent.com/71310074/143681564-decf842b-5259-4390-abac-525d90dbd876.png)

  ![image](https://user-images.githubusercontent.com/71310074/143681573-359c550b-81d7-41b3-bb29-361091ac55c2.png)
![image](https://user-images.githubusercontent.com/71310074/143681579-823e67d8-0e71-4e83-8ce5-4bfe67a984a6.png)
![image](https://user-images.githubusercontent.com/71310074/143681586-338293d6-b529-4606-b7bf-bc1475e2f41e.png)
![image](https://user-images.githubusercontent.com/71310074/143681595-c625032c-4152-4b81-b802-64580a4b3947.png)
![image](https://user-images.githubusercontent.com/71310074/143681599-8d47d6a6-2376-46a8-acb3-7aa6e8607d79.png)

  
</details>
  

<hr>

# Results
- dateTime, data index, time(1분 간격)
- distance(value), calories(level, mets, value), steps(value)

<img src = "https://user-images.githubusercontent.com/71310074/143682247-adfa36b8-60a1-4516-bed2-2df17dedd40b.png" width="350">
<br>

- time - distance(value), calories(level, mets, value), steps(value)
<img src = "https://user-images.githubusercontent.com/71310074/143686335-5d6a0adb-02a1-4fbf-bdc4-3b0b4bf8ddab.png" width="350">
<img src = "https://user-images.githubusercontent.com/71310074/143686402-f449455c-f225-4ead-823e-d76ea1fcd7a0.png" width="350">


