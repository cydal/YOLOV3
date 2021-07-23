import time
import glob
import torch
import os

import glob2
import shutil



def get_image_labels(classes):
  """
  Args:
      classes (list): class names
  Returns:
      all_names (list): image file names - full path
      l_names (list): Labels file names - full path
  """
  all_names = []
  l_names = []

  for f in classes:
    fnames = glob2.glob(os.path.join(f"custom_data100/Images/{f}" , '*.jpg'))
    lnames = glob2.glob(os.path.join(f"custom_data100/Labels/{f}" , '*.txt'))
    all_names.extend(fnames)
    l_names.extend(lnames)

  return([all_names, l_names])


def copy_custom():
  """
  Args:
  """
  _ = [shutil.copy(f, "/content/customdata/images") for f in all_names]
  _ = [shutil.copy(l, "/content/customdata/labels") for l in l_names]


def trim_names(all_names, l_names):
  """
  Args:
      all_names (list): image file names - full path
      l_names (list): Labels file names - full path
  """
  all_names = [f.split("/")[-1] for f in all_names]
  l_names = [l.split("/")[-1] for l in l_names]



def write_to_traintxt(train_path, all_names):
  """
  Args:
      model (torch.nn Model): 
      criterion (criterion) - Loss Function
      device (str): cuda/CPU
      train_loader (DataLoader) - DataLoader Object
      optimizer (optimizer) - Optimizer Object
      scheduler (scheduler) - scheduler object
      EPOCHS (int) - Number of epochs
      use_wandb (bool) - use weights & biases for logging
  Returns:
      results (list): Train/test - Accuracy/Loss 
  """
  file = open(train_path, "a")
  _ = [file.write(f"./data/customdata/images/{f}\n") for f in all_names]
  file.close()