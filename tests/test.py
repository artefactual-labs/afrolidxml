import tempfile
from pathlib import Path

from xsd_validator import XsdValidator

from afrolidxml.predictions import predicted_languages_to_xml


def test_valid_xml():
    predicted_langs = {
        "zul": {"score": 39.95, "name": "Isizulu", "script": "Latin"},
        "xho": {"score": 30.49, "name": "Isixhosa", "script": "Latin"},
        "nbl": {"score": 11.4, "name": "IsiNdebele", "script": "Latin"},
    }

    with tempfile.NamedTemporaryFile(mode="w") as file:
        # Generate XML representation and write to temp file
        xml = predicted_languages_to_xml(predicted_langs)
        file.write(xml)
        file.flush()

        # Test to make sure XML file exists
        assert Path(file.name).is_file()

        # Test to make sure XML file is populated
        assert Path(file.name).stat().st_size > 0

        # Test validity of XML
        validator = XsdValidator("tests/fixtures/languages.xsd")
        validator.assert_valid(file.name)
