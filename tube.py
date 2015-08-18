from testtube.helpers import Frosted, Nosetests, Flake8

PATTERNS = (
    (
        r'.*\.py$',
        [Flake8(all_files=True), Frosted(all_files=True)],
        {'fail_fast': True}
    ),
    # Run the test suite whenever proof/, python files, or relevant config
    # files change
    (
        r'(.*setup\.cfg$)|(.*\.py$)|(.*proof/.*)',
        [Nosetests()]
    )
)
