from setuptools import setup, find_packages

setup(name="image_fidelity",
      description="A Radio Astronomy Image Fidelity Examiner.",
      author="Athanaseus Ramaila",
      author_email="aramaila@ska.ac.za",
      packages=find_packages(),
      url='https://github.com/Athanaseus/examine-image-fidelity',
#      home_page='https://github.com/Athanaseus/examine-image-fidelity',
      license="GNU GPL 3",
      classifiers=["Intended Audience :: Developers",
                   "Programming Language :: Python :: 2",
                   "Topic :: Software Development :: Libraries :: Python Modules"],
      platforms=["OS Independent"],
      install_requires=["numpy",
                        "scipy",
                        "astropy",
                        "astLib"],
      entry_points={'console_scripts':
                    ['image_fidelity = image_fidelity.image_fidelity:main']})