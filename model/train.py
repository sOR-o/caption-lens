from data_loader import Flickr8kDatasetHandler 

if __name__ == "__main__":
    handler = Flickr8kDatasetHandler()

    handler.get_data()
    file_paths = handler.check_and_move_files()

            # self.path / 'Flicker8k_Dataset',
            # self.path / 'Flickr8k_text/Flickr8k.lemma.token.txt',
            # self.path / 'Flickr8k_text/Flickr8k.token.txt',
            # self.path / 'Flickr8k_text/CrowdFlowerAnnotations.txt',
            # self.path / 'Flickr8k_text/Flickr8k.token.txt',
            # self.path / 'Flickr8k_text/Flickr_8k.devImages.txt',
            # self.path / 'Flickr8k_text/Flickr_8k.testImages.txt',
            # self.path / 'Flickr8k_text/Flickr_8k.trainImages.txt'

    
    