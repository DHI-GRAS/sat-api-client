import os

import vcr

here = os.path.abspath(os.path.dirname(__file__))

my_vcr = vcr.VCR(
    path_transformer=vcr.VCR.ensure_suffix('.yaml'),
    record_mode='once',
    cassette_library_dir=os.path.join(here, 'fixtures', 'cassettes'))
