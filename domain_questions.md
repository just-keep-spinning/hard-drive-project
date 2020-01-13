## What is a hard drive?

a high-capacity, self-contained storage device containing a read-write mechanism plus one or more hard disks, inside a sealed unit

## What are the 5 key SMART stats for identifying Hard Drive failures?

SMART 5 – Reallocated_Sector_Count.
SMART 187 – Reported_Uncorrectable_Errors.
SMART 188 – Command_Timeout.
SMART 197 – Current_Pending_Sector_Count.
SMART 198 – Offline_Uncorrectable.


## How should we aggregate stats for those features?

All features are essentially counters for different kinds of errors, taking the max for these values should be sufficient.

## What year should we begin our analysis?

Data seems to be robustly filled from 2016 forward. It is more sparse beginning in 2015. We should use 01-01-2016

## What should be our cut off year for early failures?

Reading for industry standards the expected life of a hard drive is 5 years.
based on BlackBlaze statistic failure rates dramatically increase after 3 years.

## What is your Elevator Pitch?

In a team of four, my project partners and I utilized data provided by BackBlaze, to identify the primary drivers of early failures in hard drives. Together we developed a model to predict early failures using information found in the data. We then used our findings to make recommendations on hard drive reliability based on a given drives model type, manufacturer, and other criteria.
