import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt','r', encoding='utf-8') as req_file:
    requirements = req_file.read()
    requirements = requirements.split('\n')

setuptools.setup(
    name="yolov5facedetector",
    version="1.0.2",
    author="BenedictusAryo",
    author_email="benedictusaryo@outlook.com",
    description="Packaged version YOLOv5 Face Detector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={'yolov5facedetector': ['models/*.yaml']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6.0',
    install_requires=requirements
)