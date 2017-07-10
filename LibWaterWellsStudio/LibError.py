class ErrPython:
    def OsGetCwdFailed():

        print("Error: os.getcwd() failed\n")
    def OsPathJoinFailed():
        print("Error: os.path.join() failed\n")
    def YamlLoadFailed(filePath):
        print(filePath)
        print("Error: yaml file load failed\n")
    def YamlWriteFailed(filePath):
        print(filePath)
        print("Error: yaml file write failed\n")
    def ZipUnpackError(filePath):
        print(filePath)
        print("Error: zip file unpack failed")