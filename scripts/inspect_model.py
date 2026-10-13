import keras

model = keras.models.load_model("models/model_cnn.keras")

print("Input shape:", model.input_shape)
print("Output shape:", model.output_shape)
model.summary()
