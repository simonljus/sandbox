'''
script for working with runkeeper data from zapier
'''
def inputdataToList(key,sep=",",datatype=float):
    return list(map(datatype,input_data[key].split(sep)))
def secondsToMMSS(seconds):
    whole_minutes = int(float(seconds)/60.0)
    whole_seconds=int(seconds) % 60
    seconds_str = ("0" + str(whole_seconds))[-2:]
    minutes_str = ("0" + str(whole_minutes))[-2:]
    return "{}:{}".format(minutes_str,seconds_str)
    
timestamps = inputdataToList("timestamps")
distancestamps = inputdataToList("distancestamps")
longitudes = inputdataToList("longitudes")
latitudes  = inputdataToList("latitudes")
kilometer_timestamp=[0.0]
kilometer_distancestamp=[0.0]
kilometer_total_time=["0:00"]
splits=[]
last_km_stamp =0.0

gps_pos= zip(latitudes,longitudes)
start_pos = gps_pos[0]
end_pos = gps_pos[-1]
pos_at_stamp=[gps_pos[0]]

all_stamps= zip(timestamps,distancestamps)
time_in_seconds = timestamps[-1]
distance_in_meters = distancestamps[-1]

sec_per_km = float(time_in_seconds)/(float(distance_in_meters)/1000.0)
pace= secondsToMMSS(sec_per_km)

for i,(t_i,m_i) in enumerate(all_stamps):
    if m_i >= last_km_stamp + 1000.0:
        pos_at_stamp.append(gps_pos[i])
        delta_distance = float(m_i-last_km_stamp)
        delta_time = float(t_i -kilometer_timestamp[-1])
        s_per_km = float(delta_time)/float(delta_distance/1000.0)
        splits.append(secondsToMMSS(s_per_km))
        kilometer_timestamp.append(float(t_i))
        kilometer_distancestamp.append(float(m_i))
        kilometer_total_time.append(secondsToMMSS(t_i))
        last_km_stamp=m_i
            
return {'m_start_pos':start_pos,
        'm_end_pos':end_pos,
        'm_gps_pos':gps_pos,
        'm_kilometer_time':kilometer_total_time,
        'm_kilometer_distancestamp':kilometer_distancestamp,
        'm_pace':pace,
        'm_seconds_per_kilometer':sec_per_km,
        'm_time':time_in_seconds,
        'm_distance':distance_in_meters,
        'm_splits':splits,
        'm_pos_at_stamp':pos_at_stamp
       }
