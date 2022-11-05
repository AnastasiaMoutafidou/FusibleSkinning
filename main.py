import sys
import os
import bpy
from timeit import default_timer as timer

class PathsForBlender(object):
    def __init__(self, train_model_paths, test_model_path, file_type, list_of_obj_files_in_folder = [], rignet_model_path = ""):
        self.train_model_paths = train_model_paths
        self.rignet_model_path = rignet_model_path
        self.test_model_path = test_model_path
        self.file_type = file_type
        self.list_of_obj_files_in_folder = list_of_obj_files_in_folder
# remove mesh Cube
if "Cube" in bpy.data.meshes:
    mesh = bpy.data.meshes["Cube"]
    print("removing mesh", mesh)
    bpy.data.meshes.remove(mesh)

file_path = 'C:\\Users\\User\\Desktop\\deep-skinning'
python_packages_path = 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages'
sys.path.append(file_path)
sys.path.insert(0, python_packages_path)

start = timer()

#train_model_path_1 = file_path + '\\animations\\DataSet_Humans\\DataSetOfHumans\\human3.fbx'
#train_model_path_3 = file_path + '\\animations\\DataSet_Humans\\DataSetOfHumans\\human_5.fbx'
#train_model_path_4 = file_path + '\\animations\\DataSet_Humans\\DataSetOfHumans\\human_9.fbx'
#train_model_path_5 = file_path + '\\animations\\DataSet_Animals\\dataset\\animal_3.fbx'
#train_model_path_6 = file_path + '\\animations\\DataSet_Animals\\dataset\\animal_5.fbx'
#train_model_path_7 = file_path + '\\animations\\DataSet_Animals\\dataset\\animal_6.fbx'
#train_model_path_8 = file_path + '\\animations\\DataSet_Animals\\dataset\\animal_7.fbx'
#train_model_path_9 = file_path + '\\animations\\DataSet_Animals\\dataset\\animal_11.fbx'
#train_model_path_10 = file_path + '\\animations\\DataSet_Animals\\dataset\\animal_12.fbx'
#train_model_path_8 = file_path + '\\animations\\DataSet_Animals\\dataset\\animal_13.fbx'

#train_model_path_3 = file_path + '\\animations\\Alien-Animal.fbx'
#train_model_path_4 = file_path + '\\animations\\Dragon.fbx'
#train_model_path_5 = file_path + '\\animations\\Tree_frog.fbx'

train_model_paths = []
#fbx_path = file_path + '\\animations\\DataSet_Animals\\dataset\\animal_'
#for i in range(1, 14):
#    train_model_paths.append(fbx_path+str(i)+".fbx")

#train_model_paths.append(train_model_path_1)
#train_model_paths.append(train_model_path_2)
#train_model_paths.append(train_model_path_3)
#train_model_paths.append(train_model_path_4)
'''train_model_paths.append(train_model_path_5)
train_model_paths.append(train_model_path_6)
train_model_paths.append(train_model_path_7)
#train_model_paths.append(train_model_path_8)
train_model_paths.append(train_model_path_9)
train_model_paths.append(train_model_path_10)
'''
# ANIMALS DATASET
'''for i in range(1, 25):
    if ( i != 8 and i!= 22):
        train_model_paths.append(file_path + '\\animations\\DataSet_Animals\\dataset\\animal_'+str(i)+'.fbx')

# HUMANS DATASET
for i in range(1, 31):
   if ( i != 11 and i != 15and i != 17 and i != 20 and i!= 21 and i != 25  and i != 28 ):
       train_model_paths.append(file_path + '\\animations\\DataSetHumans\\Human_'+str(i)+'.fbx')
'''

human = 'Spiderman'
animal = 'fox'
animal = 'camel-collapse'
rignet_test = 'Spiderman-Rignet-RestPose'
test_model_path = file_path + '\\animations\\DataSetHumans\\'+human+'.fbx'
#test_model_path = file_path + '\\animations\\DataSetHumans\\human_'+str(3)+'.fbx'
#test_model_path = file_path + '\\animations\\DataSet_Animals\\dataset\\lion.fbx'
#test_model_path = file_path + '\\animations\\DataSet_Animals\\dataset\\'+animal+'.fbx'
#rignet_model_path = ""
rignet_model_path = file_path + '\\animations\\DataSetHumans\\'+rignet_test+'.fbx'

#test_model_path = 'C:\\Users\\User\\Desktop\\animations\\DataSet_Animals\\dataset\\'+animal+'\\'
#train_model_paths.append(test_model_path) # for evaluation

#train_model_paths.append(test_model_path) # for Rignet Comparison

import tensorflow_script
import tensorflow_script_without_training
import RigNet
import DeepSkinningRigNet
import RigNetDeepSkinning
import p_center
import imp
import AgglomerativeDeepSkinning

print('\n---------- NEW RUN ----------')
print('\n')

if 'fbx' in test_model_path:
    file_type = 'fbx'
    pathsForBlender = PathsForBlender(train_model_paths, test_model_path, file_type, rignet_model_path=rignet_model_path)
else:
    list_of_obj_files_in_folder = os.listdir(test_model_path)
    file_type = 'obj'
    pathsForBlender = PathsForBlender(train_model_paths, test_model_path, file_type, list_of_obj_files_in_folder, rignet_model_path=rignet_model_path)

imp.reload(tensorflow_script)
imp.reload(tensorflow_script_without_training)
imp.reload(AgglomerativeDeepSkinning)

# for p-center clustering comment tensorflow_scipt.start_tensorflow(...) line and uncomment p_center...

#tensorflow_script.start_tensorflow(pathsForBlender, "General-512-CNN2x8-")
# ENABLE FOR HUMAN
#tensorflow_script_without_training.start_tensorflow_without_training(pathsForBlender, "General-4096-LSTM-23MODELS-With-Numbering  ", human)
# ENABLE FOR ANIMAL
#tensorflow_script_without_training.start_tensorflow_without_training(pathsForBlender, "General-4096-LSTM-23MODELS-With-Numbering  ", animal)

#RigNet.start_rignet(pathsForBlender, human, "RigNet")
DeepSkinningRigNet.start_deepSkinning_rignet(pathsForBlender, human, "General-4096-LSTM-23MODELS-With-Numbering  ")
#RigNetDeepSkinning.start_rignet_deepSkinning(pathsForBlender, human, "General-4096-LSTM-23MODELS-With-Numbering  ")

#p_center.p_center_clustering(pathsForBlender, animal)

print('\n')
print('!!!!! Script successfully finished running !!!!!')
end = timer()
print('time required to run the whole application : ', end - start)
