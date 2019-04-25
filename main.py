import tensorflow as tf

A = tf.constant('Hello World!')

with tf.Session() as sess:
    
    B = sess.run(A)
    print(B)
