# facial_recog_attendance

Initial research on the problem

x university has more than 30,000 students across its campuses in the UK, which is about 10,000 students short of the biggest UK university, University College London. The traditional method of attendance marking is a tedious task in many schools and colleges. It is also an extra burden to the faculties who should mark the attendance by manually calling the names of students which might take about 5 minutes of the entire session. This is time-consuming and there are some chances of proxy attendance. Therefore, many institutes started deploying many other techniques for recording attendance like the use of Radio Frequency Identification (RFID) and fingerprint-based. With the current attendance monitoring system at x University, students use their RFID-equipped ID cards to register for attendance. However, these systems are queue based and easily exploited due to factors like verification. This means a student can give another student their card to register attendance without them being present. 
Face recognition has set an important biometric feature, which can be easily acquirable and is non-intrusive. Face recognition-based systems are relatively oblivious to various facial expressions. The face recognition system consists of two categories: verification and face identification. Face verification is a 1:1 matching process, it compares face images against the template face images and face identification is a 1:N problem that compares query face images. The purpose of this system is to build an attendance system that is based on face recognition techniques. Here the face of an individual will be considered for marking attendance. Nowadays, face recognition is gaining more popularity and has been widely used.
In this project, we will propose a system that detects the students from a live streaming video of a classroom and attendance will be marked if the detected face is found on the database. This new system will consume less time and improve veracity as compared to traditional methods. 

List and identify existing work

A. Face Recognition-based Attendance Management System - Smitha, Pavithra S Hegde, Afshin. 
1. Students of the class must register themselves by entering the required details and then their images will be captured and stored in the dataset. During each session, faces will be detected from live streaming video of the classroom.
2. The faces detected will be compared with images present in the dataset.
3. If a match is found, attendance will be marked for the respective student.
4. At the end of each session, a list of absentees will be mailed to the respective faculty handling the session
Data sets used
A. 60 sapmles taken when a student enters
      Haar-Cascade clasiffier with OpenCV.

Face Recognition and RFID Verified Attendance System - Akbar, Md Sajid, et al
1. The model focuses on how facial recognition incorporated with Radio Frequency Identification (RFID) detects the authorized students and counts as they get in and get out form the classroom.
2. The system keeps an authentic record of every registered student.
3. Attendance is noted only if the ID card and the face is present. 
Pros 
1.	Two-factortor authentication
Cons
1.	Computational time complexity. 
2.	Accuracy not discussed.
3.	20 pictures need to be taken per student.

Face detection
OpenCV Haar Cascade Face Detection – This scans for features that indicates a face like eye brows, nose etc then classifies it as a positive detection. ML method
Pros
1.	Frontal face detection
2.	Quick simple and fast
Cons
1.	Difficult to determine side faces

Dlib HoG face
Takes a histogram and intensity changes of an image.
Notes: This library takes images in BGR mode. ML method.
Pros
1. Detect all sides rotations and tilts of the face 
Cons
1.	Takes more time (upto 1.4 secs from 0.3s) in the image is in smaller scale.

OpenCV Deep learning-based face detection
One of the best face detection algorithms in python
Pros
1.	Very fast detection at 0.03s
Cons
1.	Cant train deeplearning models on OpenCV. Can only import them.

Dlib deep learning based face detection

Pros
1.	More accurate than Hog based

Cons
1.	Need to use Nvidia GPU, otherwise it is very slow. 4.3 seconds at its fastest

Mediapipe Deep learning based face detection (Mediapipe (Blaze face))
One of the fastest models ranging from 200-1000 FPS.
Pros
1.	Detects a face in 0.01s
2.	Considers facial features like eyes, nose, mouth tip etc.

Face recognition 
The face recognition library/model has an accuracy of 99.38%
Finalized approach
With a dataset of stored labelled faces
1.	Encode faces
2.	Detect a face using mediapipe. This includes the process of downscaling or upscaling the image
3.	Use the face_recognition library to identify the face.
4.	Find the person’s name from the encoding. 
Face_recognition

To do
1.	Increase the training sample from 1 to 9 to increase accuracy.
2.	Deploy on the cloud


![image](https://user-images.githubusercontent.com/114836975/195599156-ecd683dd-e26a-4f8e-af32-00d1d8c26dde.png)

Attendance stored in AWS-RDS  
![image](https://user-images.githubusercontent.com/114836975/195632819-a7ecaf4f-6860-479a-82c5-4f9e34f988ce.png)

![image](https://user-images.githubusercontent.com/114836975/195632546-b5107dfd-3350-420a-89e5-29d09bc76cae.png)
![image](https://user-images.githubusercontent.com/114836975/195633431-7624bfcf-ca88-4aa9-94ae-3176e885eec0.png)

