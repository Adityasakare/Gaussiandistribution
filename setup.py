from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Gaussiandistribution',
  version='0.0.1',
  description='This is juat a Gaussian Distribution (Normal) package that takes two values and calculated mean,  standard derivation.It also calculate two normal distribution values and shows to you.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Aditya Sakare',
  author_email='aditya.sakare16@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='calculator', 
  packages=find_packages(),
  install_requires=['Matplotlib'] 
)