# GDPR Privacy Photo Filter
De-identification of Photos
De-identification and Tracking for Photos and Enforcement of GDPR.

This repo is the starting library for tracking and scrubbing of photos in the fight against Catfishing as a GDPR violation.


What needs to be done:
1. Scoping - Process, FaceDetect - InProgress Data Science Colab Testing, RandomFaceReplace, FaceScrub, MetaMark, AIMark, GetMetaMark, GetAIMark
2. Test Implementation for AI Model pieces - Colab Notebook of Models with Validation Data
3. Library wrapping and Implementation
4. Library Publish


Tasks:
- [x] Face Detect - Colab Testing - Included in the Notebook folder in the repo.
- [ ] Facescrub - Colab Testing - Simplest De-identification - Simple blur - Commonly available
- [ ] Basic Library Object Implementation
- [ ] MetaMark - Direct Implementation no datascience required
- [ ] getMetaMarks - Direct Implementation
- [ ] run - Runs the scanning for faces, scrubbing, and applies metamarks
- [ ] v0.5 Release - Library can now take photos and auto De-id them
- [ ] getPII - get's all the PII in text on the page
- [ ] scrubPII - Will scrub the PII in the image - simple blur
- [ ] Update run functions configs to utilize all functions
- [ ] v0.8 Release - Automated Privacy Picture Scrubbing with Faces and text - handles most public access scenarios
- [ ] RandomFaceReplace - Synthetic face generation for hidden in plain sight Privacy
- [ ] alterPII - Simple word replacement for hidden in plain sight
- [ ] v0.9 Release - Hidden in plain sight photo de-identification
- [ ] AIMark - Mark through the pixels in a secret method a way to identify the source and downloader of the photo
- [ ] getAIMark - Retreive this secret marking
