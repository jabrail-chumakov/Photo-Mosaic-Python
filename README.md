# Assignment 5 Part 2
Install Matlab, Python 3.6, as well as `cv2` and `numpy`.   

## Description
In this assigment it was required to implement some tasks in warmup part by using MATLAB software and to code script that will create mosaic from different small photos.

## Warmup
Loops and if statements weren't used because it was one of the task's condition. Image coordinate system was used; that is, x indexes the rows from top to bottom and y the columns from left to right.

### Task 1.1
Here a grayscale image of constant intensity 100 were created by setting size of image to `1000 x 1000`. Results can be observed below on the Figure 1:  

![task1](https://user-images.githubusercontent.com/67557966/107941768-67ba6f80-6fb4-11eb-9036-74d1e6041905.jpg)

### Task 1.2
This task required to make a grayscale image with alternating black and white vertical stripes, where each of them is 4 pixels wide. Results can be observed below on the Figure 2:

![Снимок экрана 2021-02-15 173937](https://user-images.githubusercontent.com/67557966/107941999-cc75ca00-6fb4-11eb-9314-cfea6a0f5824.jpg)

### Task 1.3
Here a grayscale image with a ramp intensity distribution, `described by I(x, y) = x/2`, were implemented. Note that it should not be fully gradient cause we have different aim in this task. Thus, results can be observed below:

![Снимок экрана 2021-02-15 174318](https://user-images.githubusercontent.com/67557966/107942352-4f972000-6fb5-11eb-85dc-6d79d6a861ac.jpg)

### Task 1.4
A grayscale image with a Gaussian intensity distribution centered at (128, 128), described by following formula:

![Снимок экрана 2021-02-15 174412](https://user-images.githubusercontent.com/67557966/107942436-6d648500-6fb5-11eb-9a57-7407ce36d863.jpg)

Thus, we need to implement something similar to gradient mask, where white color is centered. Finally, the following figure should appear:

![Снимок экрана 2021-02-15 174605](https://user-images.githubusercontent.com/67557966/107942620-b1f02080-6fb5-11eb-8f8f-d5e65597ee06.jpg)

### Task 1.5
The last task was just to make a color image where the upper left quadrant is `yellow`, the lower left quadrant is `red`, the upper right
quadrant is `green`, and the lower right quadrant is `black`. Results of this task can be observed below:

![Снимок экрана 2021-02-15 174748](https://user-images.githubusercontent.com/67557966/107942790-efed4480-6fb5-11eb-97e3-438bb7f3d758.jpg)


## Main part 
In this part photo mosaic was implemented by using `python`. I implemented this task with different shapes: `circle` and `square`. It can be regulated inside python code. It can take a while in order to render your final photo, cause I used high-quality images for both dataset and input. 

## Good Luck!

