# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:27:17 2021

@author: 이예빈
"""

import pandas as pd
import json
import numpy as np

'''
메인 함수 : 파일 입출력, data 파일 json 포맷으로 변환
'''

def main():
    df = pd.read_csv('C:/22CCHS_2.csv')     # csv 파일 읽기
    df.to_json('C:/22CCHS_2.json')          # json 파일로 변환
    
    # json 파일 읽어 data에 저장
    with open('C:/22CCHS_2.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    json_data = json.dumps(data['data'], indent='\t')    # 문자열 형식으로 변환
    
    data = data['data']     # 'data' 부분만 추출
    
    f.close()
    
    return data


'''
시간, 거리/칼로리/걸음수 정보 모두 출력
'''    
    
def all_data(start, end):
    
    for i in range(start,end):
        # print("<< ", i, ">>" ,end='\n\n')
    
        
        ex_data=data[f'{i}']
        ex_data = ex_data.replace('\'', '\"')   # json 포맷 변환을 위해 '를 "로 변환
        jsonData = json.loads(ex_data)          # json 포맷으로 변환
        
        date = jsonData['distance']['activities-distance'][0]['dateTime'] # 날짜
        
        distance_data = jsonData['distance']['activities-distance-intraday']['dataset']     # 모든 distance 데이터셋
        calories_data = jsonData['calories']['activities-calories-intraday']['dataset']     # 모든 calories 데이터셋
        steps_data = jsonData['steps']['activities-steps-intraday']['dataset']              # 모든 steps 데이터셋
        
        print("=============== ", date, '(', i, ')', ' =============== ', end='\n\n') # 날짜 출력
    
        # 1분 간격으로 시간당 총 60개의 데이터 출력
        for i in range(len(distance_data)):

            print(i)
            print("time : ", distance_data[i]['time'])
            print("distance data : ", distance_data[i]['value'])
            print("calories data : " ,calories_data[i]['level'], calories_data[i]['mets'], calories_data[i]['value'])
            print("steps data : " ,steps_data[i]['value'])
         
            print("------------------------------\n")
            
            

        # print("==================================================\n")
        

def brief_data(start, end):
    for i in range(start,end):
        ex_data=data[f'{i}']
        ex_data = ex_data.replace('\'', '\"')   # json 포맷 변환을 위해 '를 "로 변환
        jsonData = json.loads(ex_data)          # json 포맷으로 변환
        
        date = jsonData['distance']['activities-distance'][0]['dateTime'] # 날짜
        
        distance_data = jsonData['distance']['activities-distance-intraday']['dataset']     # 모든 distance 데이터셋
        calories_data = jsonData['calories']['activities-calories-intraday']['dataset']     # 모든 calories 데이터셋
        steps_data = jsonData['steps']['activities-steps-intraday']['dataset']              # 모든 steps 데이터셋
        
        print("\n=============== ", date, '(', i, ')', ' =============== ', end='\n\n') # 날짜 출력
    
        # 1분 간격으로 시간당 총 60개의 데이터 출력
        for i in range(len(distance_data)):
            print(distance_data[i]['time'] , ' - ' , distance_data[i]['value'], calories_data[i]['level'], calories_data[i]['mets'], calories_data[i]['value'],steps_data[i]['value'])

        

'''
raw_data 출력
'''

def raw_data(start,end):
    for i in range(12,29):
        print("<< ", i, ">>")

        ex_data=data[f'{i}']
        ex_data = ex_data.replace('\'', '\"')
        jsonData = json.loads(ex_data)
        
        time = 0
        while time<60:
            print(jsonData['distance']['activities-distance-intraday']['dataset'][time])
            print(jsonData['calories']['activities-calories-intraday']['dataset'][time])
            print(jsonData['steps']['activities-steps-intraday']['dataset'][time])
            time+=1
            print()
        print("==================================================\n")
   

'''
distance 정보 
'''

def distance_data(start,end):

    for i in range(15,300):
        print("<< ", i, ">>") 

        ex_data=data[f'{i}']
        ex_data = ex_data.replace('\'', '\"')
        jsonData = json.loads(ex_data)
        if len(ex_data) > 100:
            target_data = jsonData['distance']['activities-distance-intraday']['dataset']
            for dataset in target_data:
                print(dataset)
        print('\n====================================\n\n')





data=main()         # 파일 입출력, 데이터 dictionary를 json 포맷으로 변환하여 얻은 data
brief_data(12,38)     # distance, calories, steps 시간대로 모두 출력


# raw_data(12,29)
# distance_data(12,29)