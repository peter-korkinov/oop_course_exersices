import math

PAGE_MAX_SIZE = 4


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @staticmethod
    def from_photos_count(photos_count):
        return PhotoAlbum(math.ceil(photos_count / PAGE_MAX_SIZE))

    def add_photo(self, label):
        for page in range(self.pages):
            if len(self.photos[page]) < PAGE_MAX_SIZE:
                self.photos[page].append(label)
                return f'{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}'
        return 'No more free slots'

    def display(self):
        divisor = '-----------'  # 11 dashes
        output = [divisor]

        for page in self.photos:
            page_repr = []
            for slot in page:
                page_repr.append('[]')
            output.append(' '.join(page_repr))
            output.append(divisor)

        return '\n'.join(output)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
