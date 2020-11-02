from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
from FaceRecognition.classifier import training
class Train_main:
    def train_main(self):
        datadir = './FaceRecognition/pre_img'
        modeldir = './FaceRecognition/model/20170511-185253.pb'
        classifier_filename = './FaceRecognition/class/classifier.pkl'
        print ("Training Start")
        obj=training(datadir,modeldir,classifier_filename)
        get_file=obj.main_train()
        print('Saved classifier model to file "%s"' % get_file)
        print("Tarea Realizada con Exito")
        #buena idea meter un return
        #sys.exit("All Done")
