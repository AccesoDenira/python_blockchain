# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    003.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mndhlovu <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/17 18:05:20 by mndhlovu          #+#    #+#              #
#    Updated: 2018/11/17 18:54:08 by mndhlovu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#import libraries first
import numpy as np
import tflearn

#download the titanic dataset
from tflearn.datasets import titanic
titanic.download_dataset('titanic_dataset.csv')
#load the csv file, indicate that the first column represents labels
from tflearn.data_utils import load_csv
data, labels = load_csv('titanic_dataset.csv', target_column=0,
        categorical_labels=True, n_classes=2)
#Preprocessing Function 
def preprocessing(passengers, columns_to_delete):
    for column_to_delete in sorted(columns_to_delete, reverse=True):
        [passanger.pop(column_to_delete) for passanger in passengers]
    for i in range(len(passengers)):
        passangers[i][1] = 1. if passengers[i][1] == 'female' else 0.
    return np.array(passangers, dtype=np.float32)
#ignore the name and ticket
to_ignore=[1, 6]
data = preprocessing(data, to_ignore)
#BUILD THE NEURAL NETWORK WHICH HAS 3 LAYERS
net = tflearn.input_data(shape[None, 6])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net)
#define a model
model = tflearn.DNN(net)
model.fit(data, labels, n_epoch=10, batch_size=16, show_metric=True)
dicaprio = [13, 'Jack Dawson', 'male', 19, 0, 0, 'N/A', 5.0000]
winslet = [1, 'Rose DeWitt Bukater', 'female', 17, 1, 2, 'N\A', 100.0000]
#preprocessing data 
dicaprio, winslet = preprocessing([dicaprio, winslet], to_ignore)
#predict the surviving chances 
pred = model.predict([decaprio, winslet])
print("DiCaprio Survival rate: ", pred[0][1])
print("Winslet Survival rate: ", pred[1][1])
