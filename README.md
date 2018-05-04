# SNAG
SNAG is a multimodal dataset consisting of co-collected eye movements and spoken descriptions produced during an image-inspection task. This dataset was collected from 30 observers whose eye movements and spoken descriptions were recorded as they inspected and describing 100 general-domain images. We also provide an image annotation tool (LINK) for manually labeling image regions with words. This dataset and the annotation tool were collected and developed by a group of researchers associated with the Multidisciplinary Vision Research Lab [mvrl](http://mvrl.cis.rit.edu/) and Computational Linguistics and Speech Processing Lab (https://www.rit.edu/clasp/) at Rochester Institute of Technology.

![alt text](https://github.com/mvrl-clasp/SNAG/blob/master/thesissnagrawdata.jpg "Logo Title Text 1")

# Description of the dataset
The dataset consists of six folders as described below:
#### 1. SnagImages: 
   This folder contains of the 100 general-domain images used in the data collection process. These images are a subset of the widely known Micorsoft Common Objects in Context (MSCOCO) dataset. The license for the MSCOCO dataset (REF) applies to these images.

#### 2. SnagGazeData:
   This folder contains eye movements for 30 observers, each viewing 100 images. It contains two folders:
   (1) SnagFixation: This folder contains 3000 csv files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.csv*. Each file contains fixation data for the indicated image number and observer number.
   
   (2) SnagSaccade: This folder contains 3000 csv files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.csv*. Each file contains saccade data for the indicated image number and observer number.

#### 3. SnagAudioWav:
   This folder contains 3000 audio files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.wav*. Each file contains spoken descriptions for the indicated image number and observer number. 
   
#### 4. SnagTranscribedJSON:
   This folder contains transcriptions of each audio file obtained with IBM Watson automatic speech recognition. The files are named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.JSON*. Each file contains the transcriptions for the indicated image number and observer number.
   
#### 5. SnagTranscribedTXT:
   This folder contains transcriptions for each audio file in TXT format. The files are named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.txt*. Each file contains the transcriptions for the indicated image number and observer number.
  
#### 6. SnagTranscribedTXT_Corrected_5Images:
   This folder contains the manually corrected ASR transcriptions for audio files (for 30 observers) corresponding to 5 images i.e. 150 files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.txt*. Each file contains the manually corrected transcription for the indicated image number and observer number. 

# Download Dataset
https://drive.google.com/drive/folders/1P-K7kLjEp7hBUCZG53YHCqYO08Z6zdvy?usp=sharing

# Image Annotation Software
This folder contains the Image Annotation User Interface as briefly described in the ACL paper. This software allows a user to boundary around regions in the image and check off words they can be annotated with. For more information, please refer to the README.txt and License.txt file within the folder. 
To download the software click on the link below:
https://drive.google.com/open?id=1P-K7kLjEp7hBUCZG53YHCqYO08Z6zdvy

# License
Please see License.txt

# Citation and Contact
Please cite our paper when you use this dataset or the image anotation software:

Vaidyanathan, P., Prud'hommeaux, E., Pelz, J. B., and Alm, C. O., SNAG: Spoken Narratives and Gaze Dataset, ACL 2018. 

For any questions about this dataset or software please contact Preethi Vaidyanathan at pxv1621@rit.edu.
