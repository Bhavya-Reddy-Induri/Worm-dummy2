from __future__ import print_function
import os
pi_dict={'10.51.198.127':'1','10.51.197.217':'2','10.50.168.124':'3','10.55.101.245':'4','10.50.168.178':'5','10.49.198.221':'6','10.49.199.64':'7','10.55.101.96':'8',
         '10.48.73.162':'9','10.50.168.97':'10'}
pi_list=['10.51.198.127','10.51.197.217','10.50.168.124','10.55.101.245','10.50.168.178','10.49.198.221','10.49.199.64','10.55.101.96',
         '10.48.73.162','10.50.168.97']
p_c_dict={}
#this path is for ebc_wormrun which outputs  total expno
path = '/home/tequi/ebc_wormRun_dummy'
ebc_files = os.listdir(path)
for exp_num_folder in  ebc_files:
    exp_num_folder_path = os.path.join(path, exp_num_folder)
    exp_num_folder_files = os.listdir(exp_num_folder_path)
    exp_num_folder_split=exp_num_folder.split('_')
    exp_no=exp_num_folder_split[1]
    print("-----------------"+exp_no+"!!!!!!!!")
    for exp_num_folder_file in exp_num_folder_files:
        traceroutes_path = os.path.join(exp_num_folder_path , exp_num_folder_file)
        #print(traceroutes_path)
        if(exp_num_folder_file=="traceroutes"):
             traceroute_files = os.listdir(traceroutes_path)
             for traceroute_file in traceroute_files:
                   node_path = os.path.join(traceroute_file, traceroutes_path)
                   filename = traceroute_file
                   filepath = node_path + "/" + filename
                   with open(filepath, "r") as file2:
                       hop = 0
                       hop = sum(1 for line in file2)
                       hop=hop-1
                       file2.close()
                   #print(traceroute_file)
                   trace_name_split=traceroute_file.split('_')
                   #print(trace_name_split)
                   parent_pi=trace_name_split[3]
                   parent_pi=parent_pi[1:]
                   child_pi=trace_name_split[5]
                   child_pi=child_pi[:-4]
                   p_c_dict[child_pi]=parent_pi
                   print("parent_pi: "+parent_pi+"child_pi : "+child_pi+"hop : "+str(hop))




        #         node_path = os.path.join(experiment_file, experiemnts_path)
        #         filename=experiment_file
        #         filepath=node_path+"/"+filename
        #
        #         with open(filepath, "r") as file:
        #                 count = 0
        #                 count = sum(1 for line in file)
        #                 if (count <2):
        #                     file.close()
        #                 else:
        #                     file.close()
        #                     print("---------new node----------")
        #                     with open(filepath, "r") as file2:
        #                          list1 = []
        #                          for line2 in file2:
        #                              list1.append(line2.strip())
        #
        #                          print(list1)
