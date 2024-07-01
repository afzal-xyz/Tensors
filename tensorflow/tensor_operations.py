import tensorflow as tf

# Creating a tensor
a = tf.constant([2.0, 3.0, 4.0])
b = tf.constant([1.0, 5.0, 6.0])

# Performing tensor operations
c = tf.add(a, b)
d = tf.multiply(a, b)

print("Addition: ", c.numpy())
print("Multiplication: ", d.numpy())
