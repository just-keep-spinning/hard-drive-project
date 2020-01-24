| Term             | Definition | Notes|
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Hard Drive       | A high-capacity, self-contained storage device containing a read-write mechanism plus one or more hard disks, inside a sealed unit. Also called hard disk drive.| Backblaze implements several different models of hard drives with varying capacities.|
| Reliability      | A low reliablity is a hard drive that fails before A boolean classification of low reliability or high reliability based on drive failure rate and lifespan| |
| Failure          | Contains a “0” if the drive is active. Contains a “1” if this is the last day the drive was operational before failing.| |
| Early Failure    | A failure which occurs in a hard drive where age in years is less than 2.6 years old, contains a "1" if the drive is an early failure.| Calculated drive age in years from the feature (SMART_9: Power-On-Hours) / 365 / 24 |
| SMART Attributes | SMART (Self-Monitoring, Analysis and Reporting Technology) is a monitoring system included in hard drives used to detect and report various indicators of drive reliability with the intent of anticipating imminent hardware failures. | There are several SMART attributes in the data. Detailed information on each attribute can be found in our smart_attributes_index.md |
| Serial Number    | The manufacturer-assigned serial number of the drive.| |
| Model            | The manufacturer-assigned model number of the drive.| |
| Manufacturer     | The manufacturer/company that built the hard drive. The manufacturer information is derived from the model number through additional research.| |
| Capacity Terabytes    | The drive capacity (amount of storage) measured in bytes.| Converted bytes to terabytes using the following calculation: capacity_bytes / 1,000,000,000,000|
|Uncorrectable Sector Count| The total count of uncorrectable errors when reading/writing a sector. A rise in the value of this attribute indicates defects of the disk surface and/or problems in the mechanical subsystem. | |
|Current Pending Sector Count| Count of "unstable" sectors (waiting to be remapped, because of unrecoverable read errors). If an unstable sector is subsequently read successfully, the sector is remapped and this value is decreased. | |
|Command Timeout   | The count of aborted operations due to HDD timeout. Normally this attribute value should be equal to zero. | |
|Reported Uncorrectable Errors| The count of errors that could not be recovered using hardware ECC. | |
|Reallocated Sectors Count| The raw value represents a count of the bad sectors that have been found and remapped.  | |
|Drive Age In Years| Numeric value in years of a hard drive's age | Calculated drive age in years using the feature (SMART_9: Power-On-Hours) / 365 / 24 |