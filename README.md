# GDPR Privacy Photo Filter
## De-identification of Photos
## Built with :heart: by [Matthew Davis](https://www.linkedin.com/in/tech-lead-matt-davis/) - [linkedin](https://www.linkedin.com/in/tech-lead-matt-davis/) - [github](https://github.com/Deamoner) - [Medium](https://medium.com/@mdavis_71283) - [Youtube](https://www.youtube.com/channel/UCJNZxBqs8ElqouPqAkZLlqg) - [Facebook](https://www.facebook.com/matthewjamesdavis/)
De-identification and Tracking for Photos and Enforcement of GDPR.

This repo is the starting library for tracking and scrubbing of photos in the fight against Catfishing as a GDPR violation.


What needs to be done:
1. Scoping - Process, FaceDetect - InProgress Data Science Colab Testing, RandomFaceReplace, FaceScrub, MetaMark, AIMark, GetMetaMark, GetAIMark
2. Test Implementation for AI Model pieces - Colab Notebook of Models with Validation Data
3. Library wrapping and Implementation
4. Library Publish


Tasks:
- [x] Face Detect - Colab Testing - Included in the Notebook folder in the repo.
- [X] Facescrub - Colab Testing - Simplest De-identification - Simple blur - Commonly available
- [ ] Basic Library Object Implementation
- [ ] Training data for accuracy data - added dataset aquisition colab notebook
- [ ] v0.1 Release for George Floyd Implementation
- [ ] Location and Meta Information Scrub
- [ ] Race Scrub
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


## Installation - Not working yet

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Privy - Privacy Photo Filter library.

```bash
pip install privy
```

## Usage

```python
import privy

(faces, private-photo) = privy.processFile(imgPath)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
