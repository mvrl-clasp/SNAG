# SNAG
SNAG is a multimodal dataset consisting of co-collected eye movements and spoken descriptions produced during an image-inspection task. This dataset was collected from 30 observers whose eye movements and spoken descriptions were recorded as they inspected and describing 100 general-domain images. We also provide an image annotation tool (RegionLabeler) for manually labeling image regions with words. This dataset and the annotation tool were collected and developed by a group of researchers associated with the [Multidisciplinary Vision Research Lab](http://mvrl.cis.rit.edu/) and [Computational Linguistics and Speech Processing Lab](https://www.rit.edu/clasp/) at Rochester Institute of Technology.

![Raw data](https://github.com/mvrl-clasp/SNAG/blob/master/thesissnagrawdata.jpg "Logo Title Text 1")

# Description of the dataset
The dataset consists of six folders as described below:
#### 1. SnagImages: 
   This folder contains of the 100 general-domain images used in the data collection process. These images are a subset of the widely known Micorsoft Common Objects in Context (MSCOCO) dataset. The license for the MSCOCO dataset (REF) applies to these images. To see an example click: [40.jpg](https://drive.google.com/file/d/1QKfN_0N2uv4duNgoGB9U2SY-i6yhWyDT/view?usp=sharing)

#### 2. SnagGazeData:
   This folder contains eye movements for 30 observers, each viewing 100 images. It contains two folders:
   (1) SnagFixation: This folder contains 3000 csv files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.csv*. Each file contains fixation data for the indicated image number and observer number. Click here to see an example: [Aud12_Obs9.csv](https://drive.google.com/file/d/1eODq9g_db25N2MCheBrNlnPaDRYIzIUc/view?usp=sharing)
   
   (2) SnagSaccade: This folder contains 3000 csv files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.csv*. Each file contains saccade data for the indicated image number and observer number. Click here to see an example: [Aud12_Obs9.csv](https://drive.google.com/file/d/1Q8DzY0zTglwr-Zy5voBMll9l9BZWbhYs/view?usp=sharing)

#### 3. SnagAudioWav:
   This folder contains 3000 audio files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.wav*. Each file contains spoken descriptions for the indicated image number and observer number. Click to hear an example: [Aud4_Obs3.wav](https://drive.google.com/file/d/13WGdCpKT4ZAKDodF3xw0pBgzWATVC8WO/view?usp=sharing)
   
#### 4. SnagTranscribedJSON:
   This folder contains transcriptions of each audio file obtained with IBM Watson automatic speech recognition. The files are named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.json*. Each file contains the transcriptions for the indicated image number and observer number. Click to see an example: [Aud4_Obs3.json](https://drive.google.com/file/d/1Str3ysFcGGI_9z5zyRZG86dbfbjuh8IO/view?usp=sharing)
   
#### 5. SnagTranscribedTXT:
   This folder contains transcriptions for each audio file in TXT format. The files are named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.txt*. Each file contains the transcriptions for the indicated image number and observer number. Click to see an example: [Aud4_Obs3.txt](https://drive.google.com/file/d/1CLEH67j0cgphdDSZ0gfXACau2b6BGyKH/view?usp=sharing)
  
#### 6. SnagTranscribedTXT_Corrected_5Images:
   This folder contains the manually corrected ASR transcriptions for audio files (for 30 observers) corresponding to 5 images i.e. 150 files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.txt*. Each file contains the manually corrected transcription for the indicated image number and observer number. Click to see an example: [Aud1_Obs31.txt](https://drive.google.com/file/d/1ohj1VzksMl_F35HZLgBMu5vMSIfjhFPq/view?usp=sharing)

# Download Dataset
[SNAG Dataset](https://drive.google.com/drive/folders/1P-K7kLjEp7hBUCZG53YHCqYO08Z6zdvy?usp=sharing)

# RegionLabeler: Image Region Annotation Software
This folder contains RegionLabeler, the image annotation user interface as briefly described in the ACL paper. This software allows a user to draw boundary around regions in the image and check off words they can be annotated with. For more information, please refer to the README.txt and License.txt file within the folder. 

Download:

[RegionLabeler](https://drive.google.com/drive/folders/1e6ZMmMNd52WPLEwmJ-s8pNzXS0IN17VH?usp=sharing)

# License
Please see License.txt

# Citation and Contact
Please cite our paper when you use this dataset or the image anotation software:

Vaidyanathan, P., Prud'hommeaux, E., Pelz, J. B., and Alm, C. O., SNAG: Spoken Narratives and Gaze Dataset, ACL 2018. 

For any questions about this dataset or software please contact Preethi Vaidyanathan at pxv1621@rit.edu.
