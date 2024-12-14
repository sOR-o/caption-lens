import pathlib
import collections
import tensorflow as tf

def get_dataset(path='../dataset/flickr8k/Flickr8k_text.zip'):
    """
    Reads and processes the Flickr8k dataset to create training and testing datasets.

    Parameters:
        path (str): Path where the dataset is stored.

    Returns:
        tuple: A tuple of training and testing datasets.
    """
    path = pathlib.Path(path)
    
    # Read and process captions
    captions = (path / 'Flickr8k.token.txt').read_text().splitlines()
    captions = [cap.split('\t') for cap in captions]
    captions = [(img_path.split('#')[0], cap) for (img_path, cap) in captions]
    
    # Create a dictionary of image paths and their respective captions
    cap_dict = collections.defaultdict(list)
    for img_path, cap in captions:
        cap_dict[img_path].append(cap)
    
    # Read training and testing image paths
    train_imgs_path = (path / 'Flickr_8k.trainImages.txt').read_text().splitlines()
    test_imgs_path = (path / 'Flickr_8k.testImages.txt').read_text().splitlines()
    
    # Create training and testing datasets
    train_caps = [
        (str(path / 'Flicker8k_Dataset' / img_path), cap_dict[img_path]) 
        for img_path in train_imgs_path
    ]
    test_caps = [
        (str(path / 'Flicker8k_Dataset' / img_path), cap_dict[img_path]) 
        for img_path in test_imgs_path
    ]
    
    # Convert to TensorFlow datasets
    train_raw = tf.data.experimental.from_list(train_caps)
    test_raw = tf.data.experimental.from_list(test_caps)

    return train_raw, test_raw