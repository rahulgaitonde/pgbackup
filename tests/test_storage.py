from pgbackup import storage

def test_storong_file_locally():
    """
    Writes content from one file-like to another
    :return:
    """
    infile = tempfile.TemporaryFile()
    infile.write(b'Testing')
    infile.seek(0)

    outfile = tempfile.NamedTemporaryFile(delete=False)
    storage.local(infile,outfile)
    with open(outfile.name, 'rb') as f:
        assert f.read() == b'Testing'
