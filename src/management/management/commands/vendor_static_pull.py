import helpers

import logging
from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

logging.basicConfig(filename="staticfile_downloads.log", level=logging.ERROR)

STATICFILES_VENDOR_DIR =  getattr(settings, 'STATICFILES_VENDOR_DIR')

# TODO make this a .json elsewhere
VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map",
}

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Downloading vendor static files")
        completed_url = []

        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            try:
                dl_success = helpers.download_to_local(url, out_path)
                if dl_success:
                    completed_url.append(url)
            except Exception as e:
                logging.error(f"Error downloading {url}: {e}")
                self.stdout.write(self.style.ERROR(f'Error downloading {url}'))
                
        if set(completed_url) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS('Successfully updated all vendor static files.')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Vendor files were not updated.')
            )
