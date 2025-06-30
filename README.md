Quickly normalise any number of audio files without having to open a DAW!

Step 1:
  Ensure you have all requirements in your environment, including having FFmpeg installed in your PATH.
  This tool was designed and tested using FFmpeg version 2025-03-27-git-114fccc4a5-full_build-www.gyan.dev

Step 2:
  Run the 'normalise_selected_wav_files.py' script.
  It will prompt you to enter your desired true-peak value.
  
![image](https://github.com/user-attachments/assets/d0fe1bba-cdfc-440c-9a94-ee947cb41951)

Step 3:
  Select all of the .wav files that you want to normalise.
  
![image](https://github.com/user-attachments/assets/880054dc-63e1-43ab-ad1e-75b32fd5d44b)

Step 4: 
  Profit! Or really just save yourself a big hassle!
  
  ![image](https://github.com/user-attachments/assets/880c9e77-02e6-4393-b824-18edfbdf7d77)

This tool was designed initially to be used in conjunction with AudioKinetic's Wwise. 
The primary use case is as a quick way to normalise/renormalise select audio files or your entire project without breaking any file's link to Wwise.
This means no hassle re-linking and not having to redo any implementation. Just run the tool and it's done.

In order to accomplish this the tool does not natively allow renaming any files in the process.

In the future I plan on adding a GUI as well as several other features to make it more useful in other contexts such as library creation.
