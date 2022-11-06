# Deep Skinning (DS), FESAM, RIGNET LBS & Fusible Skinning Schemes (RIGNET-DS, DS-RIGNET)

This project runs with:
- Python 3.5.3
- Tensorflow 1.14.0
- Cuda Toolkit 10.0.130
- Blender 2.79.b (some other devices had some incompatibilites with Cuda & Tensorflow GPU)

How to train and run:

  Training: Select the models that you want our network models (LSTM, CNN or LSTM-CNN-Hybrid) in tensorflow_script.py (change network=....)
            You could change batch_size and epochs, as well. For training, you should always use start_tensorflow function in main.py.
            
  Use a pre-trained model: In order to use pre-trained network models you could use tensorflow_script_without_training script's called start_tensorflow and provide
                           the pre-trained model's name via main.py (.h5 files have been extracted from the above procedure).
                           
  P-Center: You are additionally able to use P-Center algorithm as the proxy bone estimation which is feasible by using in main.py the function p_center_clustering of
            p_center.py script. There you should also provide the number of bones (clusters). For comparison purposes of Deep Skinning with FESAM in both tensorflow_script
            & tensorflow_script_without_training we are calculating the number of bones that our network models decide.
 
  RIGNET-DS & DS-RIGNET: Furtheremore, we have implemented a fusible skinning LBS scheme in which we combine two LBS-schemes to one.
						 In this case, we could either use Deep Skinning's information on top of Rignet (using RIGNET's weights) or Rignet's
						 information on top of Deep Skinning (using Deep Skinning's weights).
						 *Note: for RIGNET methods we have to checkout & use RIGNET method first from here: https://github.com/zhan-xu/RigNet
						 so that we have constructed the input RIGNET's LBS schemes or fusible combinations using it. An example of such input is given
						 in animations/DatasetHumans folder.
  
  <img src="https://user-images.githubusercontent.com/75429282/200162925-59cd82b8-8225-4556-a93d-ee31d3a0d58a.png" width="600">
  <img src="https://user-images.githubusercontent.com/75429282/200162805-3ad68a5f-3a10-4d53-9f7a-df2943194420.PNG" width="600">
  <img src="https://user-images.githubusercontent.com/75429282/200162806-e8bfd5f9-64fd-4580-8f37-09b78e3d1e44.png" width="600">
  
  
  Plugin for Blender: Moreover, we have created a plugin for Blender for Show/Hide 3D models imported for training, 
                      link/unlink our method's output, change FPS of output animations & reload an empty scene for user's convenience.

  ![alt text](https://github.com/AnastasiaMoutafidou/DeepSkinning/blob/master/Plugin.PNG?raw=true)
