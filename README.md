# Just Keep Spinning
#### Classifying Hard Drive Project


#### Goal
The goal of this project is to determine the reliability of hard drive models and create a model that predicts whether or not a hard drive will fail early. The stakeholders include users of the specific hard drive models in our dataset as well as consumers in the market for a new hard drive. Our project deliverables include a jupyter notebook detailing our process, a handout with best and worst hard drives, and a slide show presentation summarizing our findings for a general audience.  

#### The data
Raw data from 2016 to 2019 is acquired from [Backblaze.com](https://www.backblaze.com/b2/hard-drive-test-data.html#downloading-the-raw-hard-drive-test-data), totaling 18.8 gigabytes. The data is aggregated by serial number. The max values of the top five identified SMART stats for hard drive failures are retrieved for each unique serial number. 

Access the aggegrated data: [Hard Drive Data](https://drive.google.com/file/d/1bOE9kGx77GDPMs97Fl0n_3ZYbGxciQz5/view?usp=sharing)

#### Hypotheses
- The 5 SMART (Self-Monitoring, Analysis and Reporting Technology) stats identified by Backblaze will indicate device hard drive failure
- Hard drive fail rates will vary by model
- Hard drives fail rates will vary by manufacturer

#### Data dictionary
Document containg common terminology used throughout the project, definitions, and notes: [Data dictionary link](https://github.com/sagacious-analytics/hard-drive-project/blob/master/data_dictionary.md)

#### SMART attribute index
Index containing SMART ID number, Attribute Name, and Description: [SMART Attribute Index](https://github.com/sagacious-analytics/hard-drive-project/blob/master/smart_attributes_index.md)

#### Presentation
Tailored for a general audience: [Project Slides](https://docs.google.com/presentation/d/1ZMemmkrWH7btd8O_HNecTcAQqY0VErzuTPsXkBwOdNA/edit#slide=id.g35f391192_00)

