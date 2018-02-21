#the baseline percentage is 15% which was recorded at Bryce National Park. 
baseline=15
#the minimum detectable effect is 5% as a percentage of 15%
minimum_detectable_effect=100*5/15
print minimum_detectable_effect

#using the sample size calculator on the optimizely website 'https://www.optimizely.com/sample-size-calculator/', we attained a sample size of 520
sample_size_per_variant=520
#yellowstone needs approximately 1 week to attain the required number of samples
yellowstone_weeks_observing=520/507
print yellowstone_weeks_observing
#bryce needs approximately 2 weeks to attain the required number of samples
bryce_weeks_observing=520/250
print bryce_weeks_observing
