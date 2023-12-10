from algorithms.datafly import datafly_anonymize
from .clustering_based import cluster_based_anonymize
from utils.types import AnonMethod
from algorithms.gen_tree import GenTree
import os

__DEBUG = False


def k_anonymize(anon_params):

    if anon_params["name"] == AnonMethod.CLUSTER:
        return cluster_based_anonymize(
            anon_params["value"], 
            anon_params["att_trees"], 
            anon_params["data"], 
            anon_params["qi_index"], 
            anon_params["sa_index"], 
            type_alg='kmember')

    if anon_params["name"] == AnonMethod.DATAFLY:
        return datafly_anonymize(
            anon_params["value"], 
            anon_params["csv_path"], 
            anon_params["qi_names"], 
            anon_params["data_name"], 
            anon_params["dgh_folder"],
            anon_params['res_folder'])
    
def read_tree(path, dataset, ATT_NAMES, QI_INDEX, IS_CAT):
    """read tree from data/tree_*.txt, store them in att_tree
    """
    att_names = []
    att_trees = []
    for t in QI_INDEX:
        att_names.append(ATT_NAMES[t])
    for i in range(len(att_names)):
        if IS_CAT[i]:
            att_trees.append(read_tree_file(path, dataset, att_names[i]))
    return att_trees

def read_tree_file(path, dataset, treename):
    """read tree data from treename
    """
    att_tree = {}
    prefix = os.path.join(path, dataset + '_hierarchy_')
    postfix = ".csv"
    with open(prefix + treename + postfix) as treefile:
        att_tree['*'] = GenTree('*')
        if __DEBUG:
            print("Reading Tree" + treename)
        for line in treefile:
            # delete \n
            if len(line) <= 1:
                break
            line = line.strip()
            temp = line.split(';')
            # copy temp
            temp.reverse()
            for i, t in enumerate(temp):
                isleaf = False
                if i == len(temp) - 1:
                    isleaf = True

                # try and except is more efficient than 'in'
                try:
                    att_tree[t]
                except KeyError:
                    att_tree[t] = GenTree(t, att_tree[temp[i - 1]], isleaf)
        if __DEBUG:
            print("Nodes No. = %d" % att_tree['*'].support)
    return att_tree