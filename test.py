from SupportingScripts import filehandle
from SupportingScripts import dataparse
import json
import os
from datetime import datetime, timedelta
def main():
    saveManager = filehandle.FileHandler()
    saveManager.backup()

if __name__ == '__main__':
    main()