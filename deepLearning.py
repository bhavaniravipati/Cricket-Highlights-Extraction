from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator


def build_mod(h,w):
    clf = Sequential()
    clf.add(Convolution2D(32,(3,3),input_shape = (h,w,3),activation = "relu"))
    clf.add(MaxPooling2D(pool_size = (2,2)))
    clf.add(Flatten())
    clf.add(Dense(activation="relu", units=128))

    clf.add(Dense(activation="sigmoid", units=1))
    clf.compile(optimizer = "adam", loss = "binary_crossentropy",metrics = ["accuracy"])

    return clf

def fit(clf,training_set,test_set):
    clf.fit_generator(training_set,steps_per_epoch = 10, epochs = 10, validation_data = test_set, validation_steps = 10)

def preprocess(h,w,dataset):
    train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)

    test_datagen = ImageDataGenerator(rescale = 1./255)

    training_set = train_datagen.flow_from_directory(dataset+"/training_set",target_size=(h,w),batch_size = 32, class_mode = "binary")

    test_set = test_datagen.flow_from_directory(dataset+"/test_set",target_size=(h,w),batch_size = 32, class_mode = "binary")
    return training_set, test_set

if __name__=="__main__":
    clf=build_mod(64,360)
    train,test=preprocess(64,360,)
    fit(clf,train,test)