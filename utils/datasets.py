def get_oscar_urls(language, shuffled="unshuffled", deduplicated="deduplicated"):
    _BASE_DATA_URL_FORMAT_STR = (
        "https://s3.amazonaws.com/datasets.huggingface.co/oscar/1.0/{shuffled}/{deduplicated}/{language}/")
    _BASE_CHECKSUM_FILE_NAME = "{language}_sha256.txt"
    base_data_url = _BASE_DATA_URL_FORMAT_STR.format(
        shuffled=shuffled, language=language, deduplicated=deduplicated
    )
    checksum_url = base_data_url + _BASE_CHECKSUM_FILE_NAME.format(language=language)
    with fsspec.open(checksum_url, encoding="utf-8") as f:
        data_filenames = [line.decode().split("\t")[0] for line in f if line]
        return [base_data_url + data_filename for data_filename in data_filenames]


def download_urls(urls):
    for url in urls:
        if not os.path.exists(url.split("/")[-1]):
            os.system(f"wget {url}")
