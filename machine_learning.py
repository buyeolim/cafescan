import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# �����õ� ������Ű��
np.random.seed(5)

# 1. ������ �غ��ϱ�
dataset = np.loadtxt("./data.csv", delimiter=",")

# 2. �����ͼ� �����ϱ�
x_train = dataset[:700,0:8]
y_train = dataset[:700,8]
x_test = dataset[700:,0:8]
y_test = dataset[700:,8]

# 3. �� �����ϱ�
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 4. �� �н����� �����ϱ�
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 5. �� �н���Ű��
model.fit(x_train, y_train, epochs=3000, batch_size=128)

# 6. �� ���ϱ�
scores = model.evaluate(x_test, y_test)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

#7.saving the model
from keras.models import load_model
model.save('ML.h5')
