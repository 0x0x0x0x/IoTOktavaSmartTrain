import tensorflow as tf

model_dir = 'dataset_fotky'
saved_model_dir = 'dataset_fotky'

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)