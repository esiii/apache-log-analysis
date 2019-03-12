import os
from test import process


path = input("请输入待分析日志路径：")     #获取文件夹目录
path_list = []
for (root,dirs,files) in os.walk(path):
    for filename in files:
        f = os.path.join(root,filename)
        path_list.append(f)



res_path = []
for i in path_list:

    n = i.split("/")
    if(n[len(n)-1] != '.DS_Store'):
        i = i
        res_pa = n[len(n) - 1]
        res_root_pa = "../"
        res_path1 = "../result/" + "result_" + res_pa + '.csv'
        res_path2 = "../result/" + "res_log_" + res_pa + '.csv'
        # print(i,res_path1,res_path2)
        process(i, res_path1, res_path2)
    else:
        pass


