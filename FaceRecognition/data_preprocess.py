from FaceRecognition.preprocess import preprocesses
#para el tkinter eliminar la clase
class DPreprocesses():
    def preproceso(self):
        input_datadir = "./FaceRecognition/train_img"
        output_datadir = "./FaceRecognition/pre_img"

        obj=preprocesses(input_datadir,output_datadir)
        nrof_images_total,nrof_successfully_aligned=obj.collect_data()

        print('Total number of images: %d' % nrof_images_total)
        print('Number of successfully aligned images: %d' % nrof_successfully_aligned)



