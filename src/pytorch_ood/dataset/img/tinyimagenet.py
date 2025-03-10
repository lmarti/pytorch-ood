import logging
from os.path import exists, join

from torchvision.datasets import ImageFolder, VisionDataset
from torchvision.datasets.utils import download_and_extract_archive

log = logging.getLogger(__name__)


class TinyImageNet(VisionDataset):
    """
    Small Version of the ImageNet with images of size :math:`64 \\times 64` from 200 classes used by
    Stanford. Each class has 500 images for training.

    .. image :: https://production-media.paperswithcode.com/datasets/Tiny_ImageNet-0000001404-a53923c3_XCrVSGm.jpg
        :width: 400px
        :alt: Textured Dataset
        :align: center


    This dataset is often used for training, but not included in Torchvision.

    :see Website: http://cs231n.stanford.edu/

    """

    url = "http://cs231n.stanford.edu/tiny-imagenet-200.zip"
    dir_name = "tiny-imagenet-200"
    tgz_md5 = "90528d7ca1a48142e341f4ef8d21d0de"
    filename = "tiny-imagenet-200.zip"
    subsets = ["train", "val", "test"]

    def __init__(self, root, subset, download=False, transform=None, target_transform=None):
        super(TinyImageNet, self).__init__(
            root, target_transform=target_transform, transform=transform
        )

        self.subset = subset

        if download:
            self.download()

        if not self._check_integrity():
            raise RuntimeError(
                "Dataset not found or corrupted." + " You can use download=True to download it"
            )

        if subset not in self.subsets:
            raise ValueError(f"Invalid subset: {subset}. Possible values are {self.subsets}")

        self.data = ImageFolder(root=join(self.root, self.dir_name, self.subset))

    def download(self):
        if self._check_integrity():
            log.debug("Files already downloaded and verified")
            return
        download_and_extract_archive(self.url, self.root, filename=self.filename, md5=self.tgz_md5)

    def _check_integrity(self):
        return exists(join(self.root, self.dir_name))

    def __getitem__(self, index: int):
        """
        Args:
            index (int): Index

        Returns:
            tuple: (image, target) where target is index of the target class.
        """
        img, target = self.data[index]

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self):
        return len(self.dataset)


if __name__ == "__main__":
    ds = TinyImageNet(root="/home/ki/datasets/", subset="train", download=True)
    print(ds[0])
