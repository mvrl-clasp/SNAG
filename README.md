# SNAG
SNAG is a multimodal dataset consisting of co-collected eye movements and spoken descriptions produced during an image-inspection task. This dataset was collected from 30 observers whose eye movements and spoken descriptions were recorded as they inspected and describing 100 general-domain images. We also provide an image annotation tool (RegionLabeler) for manually labeling image regions with words. This dataset and the annotation tool were collected and developed by a group of researchers associated with the [Multidisciplinary Vision Research Lab](http://mvrl.cis.rit.edu/) and [Computational Linguistics and Speech Processing Lab](https://www.rit.edu/clasp/) at Rochester Institute of Technology.

![Raw data](https://raw.githubusercontent.com/mvrl-clasp/SNAG/master/thesissnagrawdata.jpg)


# Description of the dataset
The dataset consists of six folders as described below:
#### 1. SnagImages: 
   This folder consists of the 100 general-domain images used in the data collection process. These images are a subset of the widely known Micorsoft Common Objects in Context (MSCOCO) dataset. The license for the MSCOCO dataset (REF) applies to these images. To see an example click: [1.jpg](https://drive.google.com/file/d/1XvpJmHR01N0qPkSRWpjguUBTEDBF14Ie/view?usp=sharing)

#### 2. SnagGazeData:
   This folder contains eye movements for 30 observers, each viewing 100 images. It contains two folders:
   
   (1) SnagFixation: This folder contains 3000 csv files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.csv*. Each file contains fixation data for the indicated image number and observer number. Click here to see an example: [Aud1_Obs31.csv](https://drive.google.com/file/d/1J-yTCRIoXEXceBaj_PSTxO3gDOhivIiN/view?usp=sharing).fixation.csv
   
   (2) SnagSaccade: This folder contains 3000 csv files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.csv*. Each file contains saccade data for the indicated image number and observer number. Click here to see an example: [Aud1_Obs31.csv](https://drive.google.com/file/d/1F9ILSbyidEMKAp8k4yqm7nXLrN9yrsAd/view?usp=sharing).saccade.csv

#### 3. SnagAudioWav:
   This folder contains 3000 audio files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.wav*. Each file contains spoken descriptions for the indicated image number and observer number. Click to hear an example: [Aud1_Obs31.wav](https://drive.google.com/open?id=1cJodyWb6s1ecIOPFFF9rNPoYEohpjSBq)
   
#### 4. SnagTranscribedJSON:
   This folder contains transcriptions of each audio file obtained with IBM Watson automatic speech recognition. The files are named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.json*. Each file contains the transcriptions for the indicated image number and observer number. Click to see an example: [Aud1_Obs31.json](https://drive.google.com/file/d/1hEWgUPyS1UJfDXRGS_8hPLT_nVrsOw82/view?usp=sharing)
   
#### 5. SnagTranscribedTXT:
   This folder contains transcriptions for each audio file in TXT format. The files are named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.txt*. Each file contains the transcriptions for the indicated image number and observer number. Click to see an example: [Aud1_Obs31.txt](https://drive.google.com/file/d/1HxzHcqpmAyjXhZ__fsqOWh5vVbZQ-A9_/view?usp=sharing)
  
#### 6. SnagTranscribedTXT_Corrected_5Images:
   This folder contains the manually corrected ASR transcriptions for audio files (for 30 observers) corresponding to 5 images i.e. 150 files named *Aud&lt;Image Number&gt;_Obs&lt;Observer Number&gt;.txt*. Each file contains the manually corrected transcription for the indicated image number and observer number. Click to see an example: [Aud1_Obs31.txt](https://drive.google.com/file/d/1FyVYpoDv77gyz1OzICRYsu95wIazL0EN/view?usp=sharing).corrected

# RegionLabeler: Image Region Annotation Software
This folder contains RegionLabeler, the image annotation user interface as briefly described in the ACL paper. This software allows a user to draw boundary around regions in the image and check off words they can be annotated with. For more information, please refer to the README.txt within the folder. 

# Downloads 
[SNAG Dataset](https://drive.google.com/drive/folders/1P-K7kLjEp7hBUCZG53YHCqYO08Z6zdvy?usp=sharing)

[RegionLabeler](https://drive.google.com/drive/folders/1e6ZMmMNd52WPLEwmJ-s8pNzXS0IN17VH?usp=sharing)

# License
[SNAGLicense.pdf](https://drive.google.com/file/d/1oyhkPnFniqBuh0UJoJ-l9U-70UEbI6rR/view?usp=sharing)

[RegionLabelerLicense.pdf](https://drive.google.com/file/d/1LpmSMNu1s0S8U3-EcYB3ANvS9K0n2wHd/view?usp=sharing)

# Citation and Contact
Please cite our paper when you use this dataset or the image anotation software:

Vaidyanathan, P., Prud'hommeaux, E., Pelz, J. B., and Alm, C. O., SNAG: Spoken Narratives and Gaze Dataset, Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, Vol 2, pp. 132-137 or the following bibtex:

@InProceedings{P18-2022,
  author = 	"Vaidyanathan, Preethi  
		and Prud'hommeaux, Emily T.		
		and Pelz, Jeff B.		
		and Alm, Cecilia O.",		
  title = 	"SNAG: Spoken Narratives and Gaze Dataset",  
  booktitle = 	"Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",  
  year = 	"2018",  
  publisher = 	"Association for Computational Linguistics",  
  pages = 	"132--137",  
  location = 	"Melbourne, Australia",  
  url = 	"http://aclweb.org/anthology/P18-2022"  
}


For any questions about this dataset or software please contact Preethi Vaidyanathan at pxv1621@rit.edu.
