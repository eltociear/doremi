from setuptools import setup, find_packages

setup(name='doremi',
      version='1.0.0',
      description='DoReMi: Data mixture reweighting algorithm',
      url='https://github.com/sangmichaelxie/doremi',
      author='Sang Michael Xie',
      author_email='xie@cs.stanford.edu',
      packages=find_packages('.'),
      install_requires=[
        'tokenizers==0.13.2',
        'transformers==4.27.2',
        'torch==2.0.0',
        'torchvision',
        'datasets==2.10.1',
        'zstandard',
        'accelerate==0.18.0',
        'bitsandbytes==0.37.2',
        'wandb==0.14.0',
        'tqdm',
      ],
)
