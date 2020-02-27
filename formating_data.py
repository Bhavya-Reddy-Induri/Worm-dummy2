from __future__ import print_function

from _datetime import datetime
import os
import csv
import xlsxwriter
pi_dict={'10.51.198.127':'1','10.51.197.217':'2','10.50.168.124':'3','10.55.101.245':'4','10.50.168.178':'5','10.49.198.221':'6','10.49.199.64':'7','10.55.101.96':'8',
         '10.48.73.162':'9','10.50.168.97':'10'}
pi_list=['10.51.198.127','10.51.197.217','10.50.168.124','10.55.101.245','10.50.168.178','10.49.198.221','10.49.199.64','10.55.101.96',
         '10.48.73.162','10.50.168.97']
parent_pi=''
parent_dict={}
times_list_split=[]
parent_list=[None]*10
time_dict={}
time_list=[None]*10
root_time=''
#this path is for ebc_wormrun which outputs  total expno files
path = r'/home/tequi/experiment_data/feb19-9amto11am'
ebc_files = os.listdir(path)
print(ebc_files)

for exp_num_folder in  ebc_files:
    #for each exp (expperiment folder) exp_num_folder_path gives its path,  exp_num_folder_files gives the file in it  (11,12 line numbers )
    exp_num_folder_path = os.path.join(path, exp_num_folder)
    print("exp_num_folder_path : " +str(exp_num_folder_path))
    exp_num_folder_files = os.listdir(exp_num_folder_path)
    print("exp_num_folder_files:"+str(exp_num_folder_files))
    #we are splitting exp_num_folder_file to get experiment number exp_no(line14,15 )
    exp_num_folder_split=exp_num_folder.split('_')
    exp_no=exp_num_folder_split[1]
    print("-----------------"+exp_no+"!!!!!!!!")
    for exp_num_folder_file in exp_num_folder_files:
        #for in each exp_num_folder we are retrieving path,
        experiemnts_path = os.path.join(exp_num_folder_path , exp_num_folder_file)
        #print("experiemnts_path :"+ experiemnts_path)
        if(exp_num_folder_file=="experiments"):
            experiments_files = os.listdir(experiemnts_path)
            #print("experiments_files : "+str(experiments_files))
            for experiment_file in experiments_files:
                print("----------experiment file ------------: "+experiment_file)
                node_path = os.path.join(experiment_file, experiemnts_path)
                filename=experiment_file
                filepath=node_path+"/"+filename

                with open(filepath, "r") as file:
                        count = 0
                        count = sum(1 for line in file)
                        if (count <2):
                            file.close()
                        else:
                            file.close()
                            with open(filepath, "r") as file:
                                count = 0
                                count = sum(1 for line in file)
                                if (count < 2):
                                    file.close()
                                else:
                                    file.close()
                                    with open(filepath, "r") as file2:
                                        list1 = []
                                        time_ip_dict = {}
                                        for line2 in file2:
                                            list1.append(line2.strip())
                                        print("list1 : "+str(list1))
                                        infected_pis = [value for value in list1 if value in pi_list]
                                        print("infected pis : "+str(infected_pis))
                                        if infected_pis[0] in pi_dict:
                                            parent_pi = pi_dict[infected_pis[0]]
                                        print("parent_pi : "+parent_pi)
                                        for k in range(1, len(infected_pis)):
                                            parent_dict[infected_pis[k]] = parent_pi
                                        time_ip_dict = {list1[i]: list1[i + 1] for i in range(1, len(list1), 2)}
                                        ip_time_dict = {v: k for k, v in time_ip_dict.items()}
                                        time_dict.update(ip_time_dict)
                        for i in range(0, len(pi_list)):
                            if pi_list[i] in parent_dict:
                                parent_list[i] = parent_dict[pi_list[i]]
                            parent_list[0] = 'root'
                        print(parent_list)
                        for i in range(0, len(pi_list)):
                            if pi_list[i] in time_dict:
                                date_time_str = time_dict[pi_list[i]]
                                # print(date_time_str)
                                # if "EST " in date_time_str:
                                #     date_time_str = date_time_str.replace("EST ", "")
                                #     date_time_obj = datetime.strptime(date_time_str, '%a %d %b %H:%M:%S %Y')
                                # elif "EST" in date_time_str:
                                #     date_time_str = date_time_str.replace("EST ", "")
                                #     date_time_obj = datetime.strptime(date_time_str, '%a %d %b %H:%M:%S %Y')
                                #
                                # else:
                                #     print("utc date string : "+date_time_str)
                                #     date_time_str = date_time_str.replace("UTC ", "")
                                #     date_time_obj = datetime.strptime(date_time_str, '%a %b %d %H:%M:%S %Y')

                                time_list[i] = str(date_time_str)

                        root_time = root_time.replace("_", " ")
                        root_time = root_time[:-7]
                        time_list[0] = root_time
                        print(time_list)
                        merge_list = [sub[item] for item in range(len(time_list)) for sub in [parent_list, time_list]]
                        merge_list.insert(0, exp_no)
                        merge_tuple = tuple(merge_list)
                        insert_data = [merge_tuple]
                        print(insert_data)
    fname = r'/home/tequi/CSV/feb19-9amto11am.csv'
    with open(fname, "a", newline="") as csvfile:
        w = csv.writer(csvfile)
        for x in insert_data:
           w.writerow(x)
    csvfile.close()















