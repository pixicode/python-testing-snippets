from unittest.mock import Mock
from complex_app import ComplexApp
import os
import shutil


OUTPUT_DIR = "./output"


def setup_module():
    # Create the directory for our test output.
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def teardown_module():
    # Remove the test output directory.
    shutil.rmtree(OUTPUT_DIR)


def test_given_app_when_download_text_then_get_expected_results():

    # GIVEN
    # Mock the return value for the webscraper.
    mock_webscraper = Mock()
    mock_webscraper.scrape = Mock(return_value="Python 4.0 announced. Learn python programming today!")
    app = ComplexApp(mock_webscraper)

    # WHEN
    scraped_keywords = app.extract_keywords()

    # THEN
    mock_webscraper.scrape.assert_called()
    assert scraped_keywords is not None
    assert scraped_keywords["python"] == 2
    assert scraped_keywords["programming"] == 1


def test_given_app_when_scrape_to_file_then_file_exists():

    # GIVEN
    # Mock the return value for 'extract keywords'.
    app = ComplexApp(Mock())
    app.extract_keywords = Mock(return_value={"python": 2, "programming": 3})

    # WHEN
    output_path = os.path.join(OUTPUT_DIR, "test_case_2_output.txt")
    app.scrape_to_file(output_path)

    # THEN
    assert os.path.exists(output_path)