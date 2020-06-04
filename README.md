# DEPRECATED - Moved to [privyfilter](https://github.com/Deamoner/privyfilter) GDPR Privacy Photo Filter
## De-identification of Photos
## Built with :heart: by [Matthew Davis](https://www.linkedin.com/in/tech-lead-matt-davis/) - [linkedin](https://www.linkedin.com/in/tech-lead-matt-davis/) - [github](https://github.com/Deamoner) - [Medium](https://medium.com/@mdavis_71283) - [Youtube](https://www.youtube.com/channel/UCJNZxBqs8ElqouPqAkZLlqg) - [Facebook](https://www.facebook.com/matthewjamesdavis/)
De-identification and Tracking for Photos.

### Use Cases
- GDPR Protection of Photo Sharing Compliance
- Privacy for Machine Learning utilizing Photos
- Ethical Machine Learning - Remove Race/Gender/Skincolor/Generalize

This repo brings the ability for privacy and removing unethical bias from machine learning.
What started out as a fix for GDPR violations, we will focus on testing for racial and other characteristic bias.


### Roadmap

#### v0.1 - Basic Direct Identifier Scrubbing

- Face Detect
- Face Scrub

#### v0.2 - Full Deidentify Photo Process

- Detect other possible identifiers - text etc
- ScrubPIIText
- Pose Detect and Output Data
- Deidentify - Output of only pose and facial feature data in photo

#### v0.3 - Backtest/Unit Test Bias Dataset Creator

- RandomSkincolor
- RandomFaceReplace
- RandomAge


### Methodology

Scrub all identifying and data possible for bias from the dataset keeping a featureset that still allows for useful machine learning.

1. PII Data Check
2. DI(Direct Identifier) Scrubbing - Basic Privacy Preservation
3. Remove Unethical Bias Data - Remove all features but Pose, Facial Expression


### Process for Features

What needs to be done:
1. Scoping - Process, FaceDetect - InProgress Data Science Colab Testing, RandomFaceReplace, FaceScrub, MetaMark, AIMark, GetMetaMark, GetAIMark
2. Test Implementation for AI Model pieces - Colab Notebook of Models with Validation Data
3. Library wrapping and Implementation
4. Library Publish



## Installation - Not working yet

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Privy - Privacy Photo Filter library.

```bash
pip install privyfilter
```

## Usage

```python
from privyfilter.privyfilter import Privyfilter as pf

faces2, img = pf.faceScrub("../TestPics/1Person-Close.jpg")

```

## Deploying Module

```
twine upload dist/*
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
