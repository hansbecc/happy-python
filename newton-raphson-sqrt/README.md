### Method Newton Raphson Squater
>It is a mathematic method to calculate the squarter root of a number:  
```math
$X_i = (X^2_0+N)/2*X_0$
```
For example the number **27**:  
The close number for **27** is **25**, because **5x5=25** and **6x6=36**.  

So that **X_0=5**
```math
$X_i = \frac{(5^2+27)}{(2x5)}$
$X_i = \frac{(25 + 27)}{10} = \frac{52}{10} =5.2$
```
Now it is set to ``$X_0=X_i=5.2$`` for the next iteration:
```math
$X_i = \frac{(5.2^2+27)}{(2x5.2)}$
$X_i = \frac{(27.04 + 27)}{10.4} = \frac{54.04}{10.4} =5.196$
```

The result for this the ``$\sqrt{27}=5.196$``



