from SupportingScripts import filehandle

def main():
    saveManager = filehandle.FileHandler()
    saveManager.export()
    saveManager.delete()
    saveManager.swap()

if __name__ == '__main__':
    main()