# SNAG
A multimodal dataset consisting of co-collected eye movements and spoken descriptions during image-inspection task. This dataset was collected with 30 observers inspecting and describing 100 general-domain images while their eye movements and spoken descriptions are recorded. 
We also provide an Image Annotation Software that allows labeling of image regions with words.

![alt text](https://github.com/mvrl-clasp/SNAG/blob/master/images/thesissnagrawdata.jpg "Logo Title Text 1")

# Description of the dataset
The link to the dataset consists of the six folders as described below:
#### 1. SnagImages: 
   This folder consists of the 100 general-domain images used in the data collection process. These images are a subset of the widely known Micorsoft Common Objects in Context (MSCOCO) dataset. License fo the MSCOCO dataset applies to these images.

#### 2. SnagGazeData:
   This folder contains eye movements for 30 observers, each viewing 100 images. It consists of two folders:
   (1) SnagFixation: This folder consists of 3000 csv files named as *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.csv*. Each file contains fixation data for the specific image number as specified by *&lt;Image Number&gt;* for the observer number as specified by *&lt;Observer Number&gt;.csv*.
   
   (2) SnagSaccade: This folder consists of 3000 csv files named as *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.csv*. Each file contains saccade data for the specific image number as specified by *&lt;Image Number&gt;* for the observer number as specified by        *&lt;Observer Number&gt;*.

#### 3. SnagAudioWav:
   This folder consists of 3000 audio files in *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.wav* format, each file corresponding to the spoken descriptions for image number as specified by *&lt;Image Number&gt;* for the observer number as specified by        *&lt;Observer Number&gt;*.
   
#### 4. SnagTranscribedJSON:
   This folder consists of transcriptions for each audio file obtained through IBM Watson ASR. The files are in *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.JSON* format. Each file corresponds to the transcriptions for the image number *&lt;Image Number&gt;* for observer number *&lt;Observer Number&gt;*. 
   
#### 5. SnagTranscribedTXT:
   This folder consists of transcriptions for each audio file in TXT format. The files are in *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.txt* format. Each file corresponds to the transcriptions for the image number *&lt;Image Number&gt;* for observer number *&lt;Observer Number&gt;*.
  
#### 6. SnagTranscribedTXT_Corrected_5Images:
   This folder consists of the manually corrected ASR transcriptions for audio files (for 30 observers) corresponding to 5 images i.e. 150 files in *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.txt* format. 

# Image Annotation Software
This folder contains the Image Annotation User Interface as briefly described in the ACL paper. This software allows a user to boundary around regions in the image and check off words they can be annotated with. For more information, please refer to the README.txt and License.txt file within the folder. 

# Download Dataset
link to the drive where dataset is

# License
Please see License.txt

# Citation and Contact
Please consider citing our paper when you use our dataset or software:

Vaidyanathan, P., Prud'hommeaux, E., Pelz, J. B., and Alm, C. O., SNAG: Spoken Narratives and Gaze Dataset, ACL 2018. 

For any questions about this dataset or software please contact Preethi Vaidyanathan at pxv1621@rit.edu.
