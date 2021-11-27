# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:27:17 2021

@author: 이예빈
"""

import pandas as pd
import json
 

'''
메인 함수 : 파일 입출력, data 파일 json 포맷으로 변환
'''

def main():
    df = pd.read_csv('C:/22CCHS_2.csv')
    df.to_json('C:/22CCHS_2.json')
    
    with open('C:/22CCHS_2.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    json_data = json.dumps(data['data'], indent='\t')    
    
    data = data['data']
    
    f.close()


'''
시간, 거리/칼로리/걸음수 정보 모두 출력
'''    
    
def all_data(start, end):
    for i in range(start,end):
        print("<< ", i, ">>" ,end='\n\n')
        integer = i
        time = 0
        ex_data=data[f'{integer}']
        ex_data = ex_data.replace('\'', '\"')
        jsonData = json.loads(ex_data)
        distance_data = jsonData['distance']['activities-distance-intraday']['dataset']
        calories_data = jsonData['calories']['activities-calories-intraday']['dataset']
        steps_data = jsonData['steps']['activities-steps-intraday']['dataset']
    
        for i in range(len(distance_data)):
            print(i)
            print("time : ", distance_data[i]['time'])
            print("distance data : ", distance_data[i]['value'])
            print("calories data : " ,calories_data[i]['level'], calories_data[i]['mets'], calories_data[i]['value'])
            print("steps data : " ,steps_data[i]['value'])
            print("------------------------------\n")
            
        print("==================================================\n")
    


'''
raw_data 출력
'''

def raw_data(start,end):
    for i in range(12,29):
        print("<< ", i, ">>")
        integer = i
        time = 0
        ex_data=data[f'{integer}']
        ex_data = ex_data.replace('\'', '\"')
        jsonData = json.loads(ex_data)
        while time<=30:
            print(jsonData['distance']['activities-distance-intraday']['dataset'][time])
            print(jsonData['calories']['activities-calories-intraday']['dataset'][time])
            print(jsonData['steps']['activities-steps-intraday']['dataset'][time])
            time+=30
            print()
        print("==================================================\n")
   

'''
distance 정보 
'''

def distance_data(start,end):

    for i in range(15,300):
        print("<< ", i, ">>") 
        integer = i
        ex_data=data[f'{integer}']
        ex_data = ex_data.replace('\'', '\"')
        jsonString = json.loads(ex_data)
        if len(ex_data) > 100:
            target_data = jsonString['distance']['activities-distance-intraday']['dataset']
            for dataset in target_data:
                print(dataset)
        print('\n====================================\n\n')





main()              # 파일 입출력, 데이터 dictionary를 json 포맷으로 변환
all_data(12,15)     # distance, calories, steps 시간대로 모두 출력

# raw_data(12,29)
# distance_data(12,29)