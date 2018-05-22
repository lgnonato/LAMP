# LAMP
The Local Affine Multidimensional Projection (LAMP) technique is a versatile method to map multidimensional data into a visual space. LAMP bears the a number of interesting properties:

1. LAMP has been designed to make use of a set of control points to drive the mapping process. If the position of the contol points change the mapping changes accordingly. However, you can also use LAMP without any control points (see control_points_free.py);
2. LAMP is also able to handle streaming data (since the control points are fixed);
3. It is stable, that is, small perturbations in the data results in small perturbation in the mapping. 


PS. LAMP can only handle Cartesian data.

```python
class Lamp(Xdata = None, control_points = None, weights = None, 
           label=False, scale=True, dim = 2)
```

Parameters:

__Xdata__: N x K matrix where N is the number of instances and K is the dimension of the data (number of attributes)

__control_points__: M x (dim + 1) matrix where M is the number of control points and dim is the dimension of the visual space (default dim=2). The last column of the control_points matrix must contain the ids of the control points in the Xdata matrix

__weights__: N x M matrix where weights[i,j] is the weight between Xdata[i] and control_point[j]. Default (weights=None) is the inverse of the Euclidean distance

__label__: when True assumes the last column of Xdata as labels

__scale__: apply a transformation in the control points before accomplish the mapping. Produce better projections when the original and control points coordiantes have very different scales (default scale=True)

__dim__: dimension of the image space (default dim=2_
