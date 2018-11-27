import tensorflow as tf

# tf.enable_eager_execution();
# print(tf.reduce_sum(tf.random_normal([1000, 1000])))

x1 = tf.constant(5)
x2 = tf.constant(6)
result = tf.multiply(x1, x2)
# print(result)

with tf.Session() as sess:
    output = sess.run(result)
    print(output)

print(output)

