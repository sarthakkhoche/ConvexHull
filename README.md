# Convex Hull

Implementation of the O(n<sup>3</sup>) algorithm and the Jarvis March Algorithm to compute the convex hull of n points in the plane. Comparing the performance of the two algorithms for different values of n. 

## Slow Algorithm

To run the algorithm, in your terminal, enter

```
$ python3 -B algo1.py
```

A grid interface will appear initially. Select coordinates as inputs and close the interface once you are done selecting. The algorithm will start running as soon as you close the interface, wait till the program outputs **Done!** and open *./slowalgo/output.gif* to see the visualization

![Alt_Text_1](https://github.com/sarthakkhoche/CompGeo_Project/blob/master/results/r3.gif)

And to see just the convex hull visualization (without visualization of pair checks), open *./slowalgo/output/output.gif*

![Alt_Text_2](https://github.com/sarthakkhoche/CompGeo_Project/blob/master/results/r4.gif)

## Jarvis March Algorithm

To run the algorithm, in your terminal, enter

```
$ python3 -B algo2.py
```

A grid interface will appear initially. Select coordinates as inputs and close the interface once you are done selecting. The algorithm will start running as soon as you close the interface, wait till the program outputs **Done!** and open *./jm/output.gif* to see the visualization

![Alt_Text_3](https://github.com/sarthakkhoche/CompGeo_Project/blob/master/results/r1.gif)

PS - Initially, the alogorithm is run on some random inputs and consequently both the directories already exist along with the outputs. If you want to run it on your given inputs, just re-run the code with your inputs from the interface.

## Performance Analysis

| Algorithm   | Value of n  | Time taken (in seconds) |
| ----------- | ----------- | ----------------------- |
| Slow Algo   | 10          | 5.91                    |
| Slow Algo   | 15          | 18.39                   |
| Slow Algo   | 30          | 161.02                  |
| Jarvis March| 10          | 5.86                    |
| Jarvis March| 15          | 7.86                    |
| Jarvis March| 30          | 29.58                   |

Clearly, an exponential increase in slow algo can be observed. Hence for a higher number of points n, Jarvis March algorithm outperforms the slow algorithm!
