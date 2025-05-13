@REM IF NOT EXISTS "..\hhnk-theedi-tools"
@REM htt = "pip install --no-build-isolation --no-deps --disable-pip-version-check -e ../hhnk-threedi-tools"

IF NOT EXIST "..\hhnk-threedi-tools" (
    git clone https://github.com/threedi/hhnk-threedi-tools/ ..\hhnk-threedi-tools
)
pip install --no-build-isolation --no-deps --disable-pip-version-check -e ../hhnk-threedi-tools