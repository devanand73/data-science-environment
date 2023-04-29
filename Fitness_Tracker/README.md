## FITNESS TRACKER Data Science Project Template

   ![fitness_tracker](https://lh5.googleusercontent.com/9YDtFVnvKLpKvLmz8xlnV8Gj7Xlby1WZpl79ReYqSzak80t5m5NuhGJaWOtUBqRJdMkgbZ05saDnGCBelSXH9t2EH848Evf1iSS4TnmluRD29QgjVd4Z8fMwkQVMkwachvMLzqCGy4a98sHUlFgowzdzXJuLixtkJ1hKF9L7et5FnM3kdzI5YVy9d4vH9w)


You can use this template to structure your Python data science projects. It is based on [Cookie Cutter Data Science](https://github.com/daveebbelaar/data-science-template

## Fitness Tracker Project Goal

Create Python scripts to process, visualize, and model accelerometer and gyroscope data to create a machine learning model that can classify barbell exercises and count repetitions.

## The quantified self
• The quantified self is any individual engaged in the self-tracking of any kind of biological, physical, behavioral, or environmental information. The self-tracking is driven by a certain goal of the individual, with a desire to act upon the collected information — Hoogendoorn, M., & Funk, B. (2018). Machine learning for the quantified self. On the art of learning from sensory data.

# Following steps performed to Solve the project goal

. Converting raw data, reading CSV files, splitting data, cleaning
  Read all the separate raw CSV files, process them, and merge them into a single DataFrame

• Visualizing data, plotting time series data

• Outlier detection, Chauvenet’s criterion, local outlier factor

• Feature engineering, frequency, low pass filter, PCA, clustering

• Predictive modelling, Naive Bayes, SVMs, random forest, neural network

• Counting repetitions, creating a custom algorithm

##                   LESSON LEARNT
## what are Anaconda channels?
   Anaconda is a software tool that helps people with data science and machine learning. It has a package manager called conda that lets people easily install and update different tools. Channels are places where people can find these tools. Anaconda provides default channels, but people can also make their own or use third-party channels. Channels help make sure all the tools work together and can be specified in different ways in conda. They help manage package dependencies and ensure compatibility between packages.

   ## 5 conda environment commands?
#    conda env create -f environment.yml-
    create a new enviroment
#    conda env update --file environment.yml --prune
     tells conda to remove any packages that are no longer needed or are outdated from the environment.
#    conda env export --name tracking-barbell-exercises > environment.yml
     conda will export a list of all the packages and dependencies installed in the "tracking-barbell-exercises" environment and save it in an "environment.yml" file. 
#    conda env remove --name tracking-barbell-exercises
     remove an environment as part of cleaning up.
#    conda env list
     List all conda environments

#    understanding motion sensor data callected as csv file "A-bench-heavy_MetaWear_2019-01-14T14.22.49.165_C42732BE255C_Accelerometer_12.500Hz_1.4.4.csv"?
row : epoch (ms),time (01:00),elapsed (s),x-axis (g),y-axis (g),z-axis (g)
1547473786995,2019-01-14T14:49:46.995,0.000,-0.290,0.887,-0.102
"epoch (ms)": The first number, 1547473786995, is the timestamp of the measurement in milliseconds since a fixed point in time.
"time (01:00)": The second value, 2019-01-14T14:49:46.995, represents the time of the measurement in the format of year-month-dayThour:minute:second.millisecond, with the time zone being GMT+1 (Central European Time).
"elapsed (s)": The third value, 0.000, is the time elapsed since the start of the measurement in seconds. Since this is the first measurement, the elapsed time is 0.
"x-axis (g)": The fourth value, -0.290, is the acceleration in the x-axis direction in units of gravitational acceleration (g). A negative value indicates that the device is accelerating in the negative x-axis direction.
"y-axis (g)": The fifth value, 0.887, is the acceleration in the y-axis direction in units of gravitational acceleration (g). A positive value indicates that the device is accelerating in the positive y-axis direction.
"z-axis (g)": The sixth value, -0.102, is the acceleration in the z-axis direction in units of gravitational acceleration (g). A negative value indicates that the device is accelerating in the negative z-axis direction.
In summary, this line of data indicates that at the time of 2019-01-14T14:49:46.995 GMT+1, the device was not moving in the x-axis direction but was moving in the y-axis direction with an acceleration of 0.887g and was moving in the negative z-axis direction with an acceleration of -0.102g.

![supervised Learning](https://secure-res.craft.do/v2/VDcx9pyWxusPMveFX3m6KG6HXbjF2gSLkdV3zTrPX8WYRfVmzkPGH8xsArzbWQYDtj738Tte7qX57uaD9Mnm81v5yLyScsYimJrtnyuxJucWzsEH8kLx2utFpSdVnJPZkYqEWGfhw72jwCDfjQWQKgnsfcyY3HfwavJgvNhBiJ2oBULfvMd2rd2j8cBDPmwodMKAXXTWAMJXBgwmRj8BX7ZNK833tFrJsr1oCb8yCBzpRTwuciqgmDDo14K8sdL9yfvp7tEHrxoZLANCiX1HDroaB6LPwgLYmFxZjtjYcXb35HDWby/Image.jpg)


# type of data collected?
   we have 2 csv file collection 1.accelerometer and 2.gyroscope data in all 3 axis x,y and z
   and their values can be negative or positive based on excercise movement pull/push
   csv file name indicates if data collected is of accelerometer or gyroscope and also type of exercise individual is performing.
   filename iteself holds information like excersise-type,data source[accelerometer/gyroscope],timestamp.
   2 type of values are captured
   elapsed time :-time taken for a exercise routine in seconds.and number of repititions.
   limb movement in [x,y,z] : direction of movement of limb data in x,y and z axis are collected.

#  what data we have and how to process it?
   csv data is in both structured and ubstructured format. we can use data that is part of file name to classify and label data like exercise type,sensor type etc to combine both accelerometer and gyroscope data to single dataframe before proceeding.

 #  [what is supervised learning?](https://www.tibco.com/reference-center/what-is-supervised-learning/)
