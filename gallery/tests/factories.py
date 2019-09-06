import factory

from gallery.models import Image
from utils.test import mock_image_file


class ImageFactory(factory.DjangoModelFactory):

    class Meta:
        model = Image

    image = factory.LazyFunction(mock_image_file)
