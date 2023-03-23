# Marine Video Kit: A New Marine Video Dataset for Content-based Analysis and Retrieval 
**[Marine Video Kit: A New Marine Video Dataset for Content-based Analysis and Retrieval](https://hkust-vgd.github.io/marinevideokit/)** <br>
Quang-Trung Truong, Tuan-Anh Vu, Tan-Sang Ha, Jakub Lokoč, Yue Him Wong Tim, Ajay Joneja, Sai-Kit Yeung <br>
Oral presentation in MMM2023

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/marine-video-kit-a-new-marine-video-dataset/retrieval-on-mvk)](https://paperswithcode.com/sota/retrieval-on-mvk?p=marine-video-kit-a-new-marine-video-dataset)

This is an implementation for Known-item Search algorithm. We released Marine Video Kit dataset.
For the details, please check the [paper.](https://arxiv.org/pdf/2209.11518.pdf) 


![a](images/example.gif)


## How to run:
Download and copy files, including [manual descriptions](https://drive.google.com/file/d/1OZ6oFByEVWWVCvyL3Aj9ac0zNdpdERpd/view?usp=sharing) and [CLIP](https://www.dropbox.com/s/i9frmwl8nxghr6m/extracted_low_res_images_v2.zip) features to data/

Run the code for KIS task:
```
python KIS.py
```

## Citation

If you are interested in our work for your research, please do cite:

    @inproceedings{MVK,
      title={Marine Video Kit: A New Marine Video Dataset for Content-based Analysis and Retrieval},
      author={Truong, Quang-Trung and Vu, Tuan-Anh and Ha, Tan-Sang and Lokoč, Jakub and Tim,
                Yue Him Wong and Joneja, Ajay and Yeung, Sai-Kit},
      booktitle={MultiMedia Modeling - 29th International Conference, {MMM} 2023,
                Bergen, Norway, January 9-12, 2023}
    }

## License
This repository is released under MIT License (see LICENSE file for details).
