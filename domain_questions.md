## What is a hard drive?

a high-capacity, self-contained storage device containing a read-write mechanism plus one or more hard disks, inside a sealed unit

## What are the 5 key SMART stats for identifying Hard Drive failures?

1.) SMART 5 – Reallocated_Sector_Count.
2.) SMART 187 – Reported_Uncorrectable_Errors.
3.) SMART 188 – Command_Timeout.
4.) SMART 197 – Current_Pending_Sector_Count.
5.) SMART 198 – Offline_Uncorrectable.


## How should we aggregate stats for those features?

All features are essentially counters for different kinds of errors, taking the max for these values should be sufficient.

## What year should we begin our analysis?

Data is more sparse from 2013 to 2015. Data seems to be robustly filled from 2016 to 2019. Moving forward data from 01-01-2016 to 09-30-2019 will be used.

## What should be our cut off year for early failures?

Research from industry standards provides that the expected life of a hard drive is 5 years. Based on BlackBlaze statistics, failure rates dramatically increase after 3 years. Moving forward an early failure cutoff period of 2.6 years old will be used.

## What is your Elevator Pitch?

Working as a team of 4 members, our goal is to identify early failures in hard drives. We acquired our data from backblaze.com, aggregated 4 years of data into a data frame, and pulled in 5 features which correlated highly with the 169,000 observations of hard drives. During our analysis we selected a cutoff period in years to determine what qualifies as an early failure and from that we could capture takeaways such as top manufacturers and unique models that produced low early failure rates. Finally, we developed a Support Vector Machine model that accurately predicted early failures for new observations 93% of the time.